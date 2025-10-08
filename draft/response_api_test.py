from min_llm_agent import init_client

# platform_name = "OpenAI"
# model_name = "gpt-4o-mini"

# platform_name = "Grok"
# model_name = "grok-code-fast-1-0825"

# platform_name = "DeepSeek"
# model_name = "deepseek-chat"

# platform_name = "Gemini"
# model_name = "gemini-2.0-flash-001"

platform_name = "Ali"
model_name = "qwen-flash-2025-07-28"


if __name__ == "__main__":
    client = init_client(platform_name)

    # only openai supports the response api
    response = client.responses.create(
        model=model_name,
        input="Tell me a three sentence bedtime story about a unicorn.",
    )
    print(response.output_text)
