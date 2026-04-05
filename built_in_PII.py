from langchain.agents import create_agent
from langchain_groq import ChatGroq
from langchain.agents.middleware import PIIMiddleware
from langchain_core.tools import tool
import os
from dotenv import load_dotenv
load_dotenv()

groq_key=os.getenv('GROQ_API_KEY')
os.environ['GROQ_API_KEY']=groq_key

@tool
def dummyTool(query):
    """Fetch customer record based on query."""
    return f"Customer record found for query: {query}"

# Agent with PII Middleware
agent = create_agent(
    model=ChatGroq(model='llama-3.1-8b-instant'),
    tools=[dummyTool],
    middleware=[
            PIIMiddleware(
            "email",
            strategy="redact",
            apply_to_input=True,
        ),
        
        PIIMiddleware(
            "credit_card",
            strategy="mask",
            apply_to_input=True,
        ),        

    ],
)

result = agent.invoke({
    "messages": [{
        "role": "user",
        "content": (
            "My email is john.doe@example.com and my card is "
            "5105-1051-0510-5100. Can you help me?"
        )
    }]
})

print("=== Agent Response ===")
print(result["messages"][-1].content)