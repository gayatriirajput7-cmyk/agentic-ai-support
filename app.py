import streamlit as st
from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver

# 1. Page Configuration
st.set_page_config(page_title="AI Support Agent", page_icon="🤖")
st.title("🤖 Customer Support Agent")
st.write("Ask me about your order status! (Try order IDs: 123, 456, 789)")

# 2. Define the Tool (Same as before)
def get_order_status(order_id: str) -> str:
    """Use this tool to find the shipping status of an order using its order ID."""
    fake_database = {
        "123": "Shipped - arriving Tuesday.",
        "456": "Processing - waiting for inventory.",
        "789": "Delivered on Monday."
    }
    if order_id in fake_database:
        return f"Order {order_id} status: {fake_database[order_id]}"
    else:
        return f"Sorry, I could not find order {order_id}."

# 3. Setup Session State (Memory for the web browser)
# We need to store the agent and the chat history so it doesn't reset on every click
if "agent" not in st.session_state:
    # Initialize the Groq model
    # Streamlit Cloud will securely inject the API key using st.secrets
    llm = ChatGroq(
        model="llama-3.3-70b-versatile", 
        api_key=st.secrets["GROQ_API_KEY"]
    )
    memory = MemorySaver()
    st.session_state.agent = create_react_agent(llm, tools=[get_order_status], checkpointer=memory)

if "messages" not in st.session_state:
    st.session_state.messages = []

# Thread config for memory
config = {"configurable": {"thread_id": "streamlit_session_1"}}

# 4. Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. Handle User Input
if prompt := st.chat_input("What is your order number?"):
    # Add user message to state and display it
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Call the LangGraph Agent
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            inputs = {"messages": [("user", prompt)]}
            # Run the agent and get the final response
            for chunk in st.session_state.agent.stream(inputs, config=config, stream_mode="values"):
                final_response = chunk["messages"][-1].content
            
            st.markdown(final_response)
            
    # Add assistant response to state
    st.session_state.messages.append({"role": "assistant", "content": final_response})