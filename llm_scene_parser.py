import openai, json, pathlib, os

PROMPT_PATH = pathlib.Path(__file__).parent / "data" / "prompts" / "parser_prompt.txt"
PROMPT_TEXT = PROMPT_PATH.read_text(encoding="utf-8")

def parse_problem(text: str, model="gpt-3.5-turbo-0125", temperature: float = 0.1) -> dict:
    """Call OpenAI chat model to produce scene graph JSON."""
    messages = [
        {"role": "system", "content": PROMPT_TEXT},
        {"role": "user", "content": text.strip()}
    ]
    resp = openai.ChatCompletion.create(
        model=model,
        temperature=temperature,
        messages=messages,
        response_format={"type":"json_object"}
    )
    return json.loads(resp.choices[0].message.content)