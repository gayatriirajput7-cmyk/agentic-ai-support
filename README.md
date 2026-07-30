# 🤖 Agentic AI Customer Support System

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![LangGraph](https://img.shields.io/badge/LangGraph-Stateful_Agents-orange)](https://langchain-ai.github.io/langgraph/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-FF4B4B.svg)](https://streamlit.io/)
[![Groq](https://img.shields.io/badge/Model-Llama--3.3-green)](https://groq.com/)

> A stateful, dynamic AI support agent that doesn't just answer questions—it executes Python functions to resolve user queries in real-time.

**🔴 [Try the Live Demo Here](https://agentic-ai-support-nqgs2y6os4vnhxbvneoccm.streamlit.app/))**

## 🚀 Overview

Most LLM wrappers fail because they are stateless and incapable of taking action. This project solves that by implementing an **Agentic Workflow** using LangGraph and Groq's high-speed Llama-3 model.

Instead of relying solely on pre-trained knowledge, this agent is equipped with custom Python tools (simulated database queries) that it autonomously decides to execute based on user intent.

### ✨ Key Features
*   **Tool Calling & Execution:** The LLM autonomously triggers local Python functions to fetch live data (e.g., retrieving order status via an ID).
*   **Stateful Memory:** Utilizes LangGraph's `MemorySaver` to retain context across the entire conversation thread, allowing the user to reference prior turns naturally.
*   **Lightning Fast Inference:** Powered by Groq's specialized inference engine for instantaneous tool-calling and response generation.
*   **Interactive UI:** Fully deployed on Streamlit Cloud for seamless user interaction without needing terminal access.

---

## 🏗️ Architecture

The system is built on a cyclic graph architecture. The LLM evaluates the conversational state, decides if a tool is needed, pauses to wait for tool execution, and then resumes to formulate a final response.

mermaid
graph TD
    A[User Input via Streamlit] --> B{LangGraph Agent}
    B -->|Requires Tool| C[Execute Python Function]
    C -->|Return Result| B
    B -->|Final Formulated Response| D[Update State & UI]
    B <--> E[(MemorySaver / Checkpointer)]
    B <--> F(Groq: Llama-3.3-70b)

##Installation
Clone the repository:

##Bash
git clone [https://github.com/gayatriirajput-cmyk/agentic-ai-support.git](https://github.com/gayatriirajput-cmyk/agentic-ai-support.git)
cd agentic-ai-support
Set up the virtual environment:

##Bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

##Bash
pip install -r requirements.txt

##Running the App
Bash
streamlit run app.py
