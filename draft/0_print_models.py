import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.min_llm_agent.min_llm_agent import *

print_all_supported_platforms()
# print_all_supported_accessible_models()

# supported_platform_name_list = ["OpenAI", "Grok", "DeepSeek", "Gemini", "Ali"]
print_accessible_models("OpenAI", id_only=True)