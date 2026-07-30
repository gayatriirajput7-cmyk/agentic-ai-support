import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent
# 1. NEW: Import MemorySaver from langgraph
from langgraph.checkpoint.memory import MemorySaver

load_dotenv()

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

tools = [get_order_status]
llm = ChatGroq(model="llama-3.3-70b-versatile")

# 2. NEW: Initialize the memory saver
memory = MemorySaver()

# 3. NEW: Pass the memory to the agent when creating it
agent_executor = create_react_agent(llm, tools, checkpointer=memory)

print("🤖 Support Agent is running with MEMORY! Type 'exit' to quit.\n")

# We create a random thread ID for this specific terminal session.
# In a real app, this would be the user's logged-in session ID.
config = {"configurable": {"thread_id": "session_001"}}

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
        
    inputs = {"messages": [("user", user_input)]}
    
    # 4. NEW: We must pass the `config` so the agent knows WHICH memory to look up
    for chunk in agent_executor.stream(inputs, config=config, stream_mode="values"):
        final_message = chunk["messages"][-1]
        
    print(f"\nAgent: {final_message.content}\n")