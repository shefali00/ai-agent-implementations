# AI Agent Implementations using LangChain

This repository contains multiple **AI agent implementations**
built using **LangChain** and modern Large Language Models (LLMs).

Each implementation demonstrates how agents reason,
interact with external systems, and execute tasks autonomously.

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/ai-agent-implementations.git
cd ai-agents-implementation
```

### 2. Create Virtual Environment

```bash

Create a Python virtual environment:

python -m venv venv

Activate the environment:

Windows

venv\Scripts\activate

Mac / Linux

source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Configure Environment Variables

```bash
Create a .env file in the project root.

You can copy from .env.example:

cp .env.example .env

Add your API keys:

GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```
### 5. Run an Agent

```bash
Example:

python agents/basic_single_agent.py
Tech Stack

LangChain

Groq LLM

Tavily Search API

Python
```
### Purpose

This repository serves as a collection of practical examples
for understanding and building AI agents using modern frameworks.
