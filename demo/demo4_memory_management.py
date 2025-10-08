import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.min_llm_agent.min_llm_agent import min_llm_agent_class
from LyPythonToolbox import lyprint_separator
from pprint import pprint

if __name__ == "__main__":
    llm_agent = min_llm_agent_class(platform_name="OpenAI", model_name="gpt-4o-mini")

    response = llm_agent("1+1=?")
    response = llm_agent("1+2=?", with_memory=False)
    llm_agent.print_memory()
    
    lyprint_separator("|")
    llm_agent.reset_memory()
    print("Reset memory...")
    response = llm_agent("1+3=?")
    llm_agent.print_memory()
    
    lyprint_separator("|")
    print("Set memory...")
    llm_agent.set_memory([{"role": "system", "content": "You are a self-interested and rational player."}])
    llm_agent.print_memory()

    lyprint_separator("|")
    response = llm_agent("You are playing a coordination game. State your strategy in only a sentence.", role="user")
    print("Get memory and pprint...")
    memory = llm_agent.get_memory()
    pprint(memory)

    lyprint_separator("|")
    print("Append memory...")
    llm_agent.append_memory({"role": "user", "content": "1+4=?"})
    llm_agent.print_memory()