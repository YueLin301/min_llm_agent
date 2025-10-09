# from min_llm_agent import min_llm_agent_class, print_all_supported_platforms, print_all_supported_accessible_models, print_accessible_models

# ============================================================================================================================

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.min_llm_agent.min_llm_agent import *
from src.min_llm_agent.min_llm_agent import (
    min_llm_agent_class,
    init_client,
    print_all_supported_platforms,
    print_all_supported_accessible_models,
    print_accessible_models,
)

# ============================================================================================================================


def print_models():

    # print_all_supported_platforms()
    print_all_supported_accessible_models()

    # supported_platform_name_list = ["OpenAI", "Grok", "DeepSeek", "Gemini", "Ali"]
    # print_accessible_models("Grok", id_only=True)


def demo1_query_single():

    # default parameters: model_name="gpt-4o-mini"
    llm_agent = min_llm_agent_class()

    question = "What is the capital of France?"
    response = llm_agent(question)

    print(f"Model: {llm_agent.model_name}\nQuestion: {question}\nAnswer: {response}")
    llm_agent.print_memory()


def demo1a_query_single_memoryless():

    llm_agent = min_llm_agent_class()

    question = "What is the capital of France?"
    response = llm_agent(question, with_memory=False)

    print(f"Model: {llm_agent.model_name}\nQuestion: {question}\nAnswer: {response}")
    llm_agent.print_memory()


def demo2_query_multiple():

    llm_agent = min_llm_agent_class()

    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {
            "role": "user",
            "content": "1+1=?",
        },
        {
            "role": "user",
            "content": "1+2=?",
        },
    ]
    response = llm_agent(messages)

    print(f"Model: {llm_agent.model_name}\nMessages: {messages}\nAnswer: {response}")
    llm_agent.print_memory()


def demo2a_more_keywords():

    llm_agent = min_llm_agent_class()

    messages = [
        {
            "role": "system",
            "content": "Extract the event information. Output in JSON format, including the event name, date, and participants.",
        },
        {
            "role": "user",
            "content": "Alice and Bob are going to a science fair on Friday.",
        },
    ]
    response = llm_agent(messages, response_format={"type": "json_object"}, temperature=0.5)

    print(f"Model: {llm_agent.model_name}\nMessages: {messages}\nAnswer: {response}")
    llm_agent.print_memory()


def demo3_interact():

    llm_agent = min_llm_agent_class()
    llm_agent.interact()


def demo4_memory_management():

    from pprint import pprint

    llm_agent = min_llm_agent_class()

    response = llm_agent("1+1=?")
    response = llm_agent("1+2=?", with_memory=False)
    llm_agent.print_memory()

    print("|" * 50)
    llm_agent.reset_memory()
    print("Reset memory...")
    response = llm_agent("1+3=?")
    llm_agent.print_memory()

    print("|" * 50)
    print("Set memory...")
    llm_agent.set_memory([{"role": "system", "content": "You are a self-interested and rational player."}])
    llm_agent.print_memory()

    print("|" * 50)
    response = llm_agent("You are playing a coordination game. State your strategy in only a sentence.", role="user")
    print("Get memory and pprint...")
    memory = llm_agent.get_memory()
    pprint(memory)

    print("|" * 50)
    print("Append memory...")
    llm_agent.append_memory({"role": "user", "content": "1+4=?"})
    llm_agent.print_memory()


def demo5_gui_interact():

    agent = min_llm_agent_class()
    agent.interact(mode="GUI")


if __name__ == "__main__":

    # print_models()

    # demo1_query_single()
    # demo1a_query_single_memoryless()
    # demo2_query_multiple()
    # demo2a_more_keywords()
    # demo3_interact()
    # demo4_memory_management()
    demo5_gui_interact()
