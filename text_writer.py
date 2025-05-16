import openai, pathlib, json, os

PROMPT_PATH = pathlib.Path(__file__).parent / "data" / "prompts" / "rewrite_prompt.txt"
TEMPLATE = PROMPT_PATH.read_text()

def rewrite(scene: dict, original: str, model="gpt-3.5-turbo", temperature=0.4):
    filled = TEMPLATE.replace("{{SCENE_JSON}}", json.dumps(scene, indent=0))                     .replace("{{ORIGINAL}}", original.strip())
    resp = openai.ChatCompletion.create(
        model=model,
        temperature=temperature,
        messages=[{"role":"user", "content":filled}]
    )
    return resp.choices[0].message.content.strip()