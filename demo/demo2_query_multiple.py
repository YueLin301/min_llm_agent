import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.min_llm_agent import min_llm_agent_class

if __name__ == "__main__":

    llm_agent = min_llm_agent_class(platform_name="OpenAI", model_name="gpt-4o-mini")

    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {
            "role": "user",
            "content": "What is the capital of France?",
        }
    ]
    response = llm_agent(messages)

    print(f"Messages: {messages}")
    print(f"Answer by model {llm_agent.model_name}: {response}")
    
    # llm_agent.print_memory(memory_item_separator="/")
    llm_agent.print_memory()