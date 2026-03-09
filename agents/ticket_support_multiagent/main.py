from dotenv import load_dotenv
load_dotenv()

from supervisor_agent import supervisor_agent
from memory.support_memory import memory

ticket = """
Customer paid for premium plan but account still shows free plan.
This is urgent because the customer cannot access features.
"""

print("\n--- Agent Execution Flow ---\n")

# Stream execution to show tool usage

for step in supervisor_agent.stream(
{"messages": [{"role": "user", "content": ticket}]}
):
    if "model" in step:
        msgs = step["model"]["messages"]

        if msgs:
            last_message = msgs[-1]

            # Print tool calls cleanly
            if hasattr(last_message, "tool_calls") and last_message.tool_calls:
                for tool_call in last_message.tool_calls:
                    print(f"Supervisor → calling tool: {tool_call['name']}")
    

# Run agent normally to get final response

result = supervisor_agent.invoke(
{"messages": [{"role": "user", "content": ticket}]}
)

final_response = ""

for msg in result["messages"]:
    if hasattr(msg, "name") and msg.name == "create_response":
        final_response = msg.content
print("\n--- Final Response ---\n")

if final_response:
    print(final_response)
else:
    print(result["messages"][-1].content)
# Save conversation to memory

memory.save_context(
{"input": ticket},
{"output": final_response}
)
