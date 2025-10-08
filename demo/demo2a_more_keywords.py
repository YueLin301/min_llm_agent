import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from src.min_llm_agent.min_llm_agent import min_llm_agent_class

if __name__ == "__main__":

    llm_agent = min_llm_agent_class(platform_name="OpenAI", model_name="gpt-4o-mini")

    messages = [
        {"role": "system", "content": "Extract the event information. Output in JSON format, including the event name, date, and participants."},
        {"role": "user", "content": "Alice and Bob are going to a science fair on Friday."},
    ]

    response = llm_agent(messages, response_format={"type": "json_object"}, temperature=0.5)

    print(f"Messages: {messages}")
    print(f"Answer by model {llm_agent.model_name}: {response}")

    llm_agent.print_memory()
