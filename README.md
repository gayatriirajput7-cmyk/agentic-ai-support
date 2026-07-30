# agentic-ai-support
A stateful AI customer support agent using LangGraph and Llama-3.
# 🤖 Agentic AI Customer Support System

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![LangGraph](https://img.shields.io/badge/LangGraph-Stateful_Agents-orange)](https://langchain-ai.github.io/langgraph/)
[![Llama-3](https://img.shields.io/badge/Model-Llama--3.3--70b-green)](https://groq.com/)

> A stateful, dynamic AI support agent that doesn't just answer questions—it executes code to solve them.

## 🚀 Overview

Most AI customer support wrappers fail because they are stateless and incapable of taking action. This project solves that by implementing an **Agentic Workflow** using LangGraph and Groq's Llama-3 model. 

Instead of relying solely on pre-trained knowledge, this agent is equipped with custom Python tools (simulated database queries) that it autonomously decides to execute based on user intent. It also utilizes short-term memory checkpointers to maintain strict conversational context across multiple turns.

### ✨ Key Features
*   **Tool Calling:** The LLM autonomously triggers local Python functions to fetch live data (e.g., `get_order_status`).
*   **Stateful Memory:** Utilizes LangGraph's `MemorySaver` to retain context across the entire session thread, preventing the "goldfish memory" problem of basic chatbots.
*   **High-Speed Inference:** Powered by Groq's specialized inference engine for near-instantaneous Llama-3 responses.

---

## 🏗️ Architecture

*(Note: Create a simple flowchart in draw.io showing: User -> LangGraph -> Llama-3 -> Tools, and replace this text with the image link)*
`![Architecture Diagram](./architecture.png)`

The system is built on a cyclic graph architecture where the LLM evaluates the state, decides if a tool is needed, pauses to wait for tool execution, and then resumes to formulate a final natural language response.

---

## 💻 Quick Start

Follow these steps to run the agent locally on your machine.

### Prerequisites
*   Python 3.10 or higher
*   A free API key from [Groq](https://console.groq.com/)

### Installation

1. **Clone the repository:**
  
  # cd agentic-ai-support
