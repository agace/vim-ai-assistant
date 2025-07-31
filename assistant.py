#!/usr/bin/env python3

import sys
import requests
import os

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "mistral"

def commentify(text, comment_prefix):
    return '\n'.join(f"{comment_prefix} {line}" for line in text.strip().splitlines())

def detect_comment_prefix(filetype):
    return {
        'py': '#',
        'js': '//',
        'ts': '//',
        'java': '//',
        'c': '//',
        'cpp': '//',
        'rs': '//',
        'go': '//',
        'sh': '#',
        'rb': '#',
    }.get(filetype, '//')


def load_prompt_template():
  with open(os.path.join(os.path.dirname(__file__), "prompt.txt"), "r") as f:
    return f.read()

def main():
    prompt = sys.stdin.read().strip()
    if not prompt:
        print("No code or instruction provided.")
        return

    filetype = os.getenv("VIM_FILETYPE", "")
    comment_prefix = detect_comment_prefix(filetype)
     
    base_prompt = load_prompt_template()
    full_prompt = f"{base_prompt.strip()}\\### Instruction and Code:\n{prompt}"

    full_prompt += f"\n\n### Instruction and Code:\n{prompt}"

    response = requests.post(OLLAMA_URL, json={
        "model": MODEL,
        "prompt": full_prompt,
        "stream": False
    })

    if response.status_code != 200:
        print(f"Error: {response.status_code} - {response.text}")
        return

    raw_output = response.json()["response"]

    # Split by markers
    parts = raw_output.split("<<<EXPLANATION>>>")
    code = parts[0].split("<<<CODE>>>")[-1].strip() if "<<<CODE>>>" in parts[0] else ""
    explanation = parts[1].strip() if len(parts) > 1 else ""

    # Write files
    with open("/tmp/ai_code.txt", "w") as f:
        f.write(code)

    with open("/tmp/ai_explanation.txt", "w") as f:
        f.write(commentify(explanation, comment_prefix + '\n'))

if __name__ == "__main__":
    main()

