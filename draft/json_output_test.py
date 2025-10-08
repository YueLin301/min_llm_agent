from min_llm_agent import init_client
from pydantic import BaseModel

# platform_name = "OpenAI"
# model_name = "gpt-4o-mini"

# platform_name = "Grok"
# model_name = "grok-code-fast-1-0825"

platform_name = "DeepSeek"
model_name = "deepseek-chat"

# platform_name = "Gemini"
# model_name = "gemini-2.0-flash-001"

# platform_name = "Ali"
# model_name = "qwen-flash-2025-07-28"


if __name__ == "__main__":

    client = init_client(platform_name)

    # only openai supports the structured output
    output_full = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": "Extract the event information. Output in JSON format, including the event name, date, and participants."},
            {"role": "user", "content": "Alice and Bob are going to a science fair on Friday."},
        ],
        response_format={"type": "json_object"},
    )

    output_text = output_full.choices[0].message.content
    print(output_text)
