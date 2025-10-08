from min_llm_agent import min_llm_agent_class

if __name__ == "__main__":
    llm_agent = min_llm_agent_class(platform_name="OpenAI", model_name="gpt-4o-mini")
    llm_agent.interact()