import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from src.min_llm_agent.min_llm_agent import min_llm_agent_class
# from min_llm_agent import min_llm_agent_class

platform_name = "OpenAI"
model_name = "gpt-4o-mini"

# platform_name = "Grok"
# model_name = "grok-code-fast-1-0825"

# platform_name = "DeepSeek"
# model_name = "deepseek-chat"

# platform_name = "Gemini"
# model_name = "gemini-2.0-flash-001"

# platform_name = "Ali"
# model_name = "qwen-flash-2025-07-28"


if __name__ == "__main__":

    llm_agent = min_llm_agent_class(platform_name=platform_name, model_name=model_name)

    question = "What is the capital of France?"
    response = llm_agent(question)

    print(f"Question: {question}")
    print(f"Answer by model {llm_agent.model_name}: {response}")

    llm_agent.print_memory()
