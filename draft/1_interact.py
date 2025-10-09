import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.min_llm_agent.min_llm_agent import min_llm_agent_class

if __name__ == "__main__":

    model_name="gpt-5"

    llm_agent = min_llm_agent_class(platform_name="OpenAI", model_name=model_name)
    llm_agent.interact()