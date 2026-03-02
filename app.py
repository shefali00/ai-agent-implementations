from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults

# Load environment variables
load_dotenv()

# Initialize LLM (Groq)
model = ChatGroq(
    model="llama3-70b-8192"
)

# Define Tool
tools = [
    TavilySearchResults()
]

# Create Agent
agent = create_agent(
    model=model,
    tools=tools,
    system_prompt="You are a helpful AI agent."
)

# Run Agent
response = agent.invoke({
    "messages": [
        {
            "role": "user",
            "content": "Latest developments in AI agents"
        }
    ]
})

print(response)
