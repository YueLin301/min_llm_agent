from min_llm_agent import (
    min_llm_agent_class,
    init_client,
    print_all_supported_platforms,
    print_all_supported_accessible_models,
    print_accessible_models,
)

# default parameters: model_name="gpt-4o-mini"
llm_agent = min_llm_agent_class()

llm_agent.interact(mode="terminal")