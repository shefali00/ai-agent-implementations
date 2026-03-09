
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from tools.classification_tool import classify_ticket
from tools.priority_tool import detect_priority
from tools.response_tool import create_response
from dotenv import load_dotenv
load_dotenv()
llm = ChatGroq(model="llama-3.3-70b-versatile")

supervisor_agent = create_agent(
    model=llm,
    tools=[
        classify_ticket,
        detect_priority,
        create_response
    ],
    system_prompt = """
You are a supervisor agent managing customer support.

Follow this workflow strictly:

Classify the ticket using classify_ticket

Determine priority using detect_priority

Generate the final message using create_response

IMPORTANT RULES:

Only call tools to perform tasks.

The final answer MUST come from create_response.

Do NOT generate your own response.

Stop immediately after create_response returns.
"""
)
