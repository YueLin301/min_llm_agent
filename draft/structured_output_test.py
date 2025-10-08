from min_llm_agent import init_client
from pydantic import BaseModel

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

    class CalendarEvent(BaseModel):
        name: str
        date: str
        participants: list[str]

    client = init_client(platform_name)

    # only openai supports the structured output
    completion = client.chat.completions.parse(
        model=model_name,
        messages=[
            {"role": "system", "content": "Extract the event information."},
            {"role": "user", "content": "Alice and Bob are going to a science fair on Friday."},
        ],
        response_format=CalendarEvent,
    )

    event = completion.choices[0].message.parsed
    print(event)
