from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

load_dotenv()

@tool
def calculator(a: float, b: float)->str:
    """"A simple calculator tool that is useful for adding two numbers."""
    print(f"Calculating the sum of {a} and {b}")
    return f"The sum of {a} and {b} is {a + b}"

def main():
    # Initialize the model and agent
    model = ChatOpenAI(model="gpt-4o", temperature=0)
    tools = [calculator]  # Define your tools here if any
    agent = create_react_agent(model=model, tools=tools)

    print("Welcome to the Simple AI Agent. Type 'exit' to quit.")
    # Interactive loop
    while True:
        # Get user input
        user_input = input("\nYou: ").strip()
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        # Process input and stream response
        print("\nAgent: ", end='')

        for chunk in agent.stream(
            {"messages": [HumanMessage(content=user_input)]}
        ):
            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk["agent"]["messages"]:
                    print(message.content, end='')
        print()  # For newline after the response

if __name__ == "__main__":
    main()