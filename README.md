# Vim AI Assistant (Offline Copilot with Ollama)

> A lightweight, offline, privacy-respecting AI coding assistant integrated directly into your terminal Vim.  
> Powered by [Ollama](https://ollama.com/) and local models like `mistral`, `llama3`, and `codellama`.  
> No internet. No telemetry. 100% local.

---

## Features

- Trigger the assistant with `\a` while selecting code in **visual mode**
- Preview AI-generated code with **`vimdiff`**
- Accept or reject changes interactively
- Automatically replaces selected code if approved
- Displays a detailed explanation in a vertical split (formatted as comments)
- Smart comment formatting based on filetype (`//`, `#`, etc.)
- Works entirely offline — no OpenAI or cloud APIs required

---

## Requirements

- [Vim](https://www.vim.org) 8+  
- [Ollama](https://ollama.com) running locally
- Python 3.8+
- Python packages: `requests`

---

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/agace/vim-ai-assistant.git
cd vim-ai-assistant
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Install and run a local AI model
Make sure Ollama is installed and running.
Then install a model (e.g. mistral):

```bash
ollama pull mistral
ollama serve
```
> You can replace `mistral` with any compatible model like `llama3`, `codellama`, etc.
Just make sure the `MODEL` variable in `assistant.py` matches the model you pulled. Ollama currently supports a variety of LLMs, a full list is available here:
https://ollama.ai/library

### 4. Add the Vim integration

```bash
cat .vimrc-snippet >> ~/.vimrc
```

Then reload Vim:

```vim
:source ~/.vimrc
```

##  How to Use

1. Open a file in Vim
2. Select a block of code in visual mode
3. Press `\a`
4. Enter a custom instruction (e.g. `"simplify this"`, `"optimize performance"`, `"fix and explain"`)
5. You’ll see:
- A **diff** preview side-by-side (via vimdiff)
- Press `y` to accept the changes
- Press `n` to cancel and leave the code untouched
6. After confirming, an explanation opens in a vertical split with comments


## Configuration


- **Change the AI model**:
  Edit the `MODEL` variable in `assistant.py` to use a different local model (e.g., `llama3`, `codellama`).

- **Customize the keybinding**:
  The default keybinding is `\a` in visual mode. You can change it in your `.vimrc`:
  
```vim
vnoremap <leader>a :<C-U>call AIHelper()<CR>
```
- **Customizing the Prompt**:
To change how the assistant behaves, edit `prompt.txt`.  
This is the system message sent to the AI, it controls formatting, tone, and expectations.

- **Change the temp file location (optional)**:
You can edit `assistant.py` or `AIHelper()` in `.vimrc-snippet` to change where input/output files are written.

## Troubleshooting

- **Nothing happens after pressing `\a`**  
  Ensure you’re in visual mode and have selected code. Then press `\a`.

- **Error: command not found: ollama**  
  Ollama must be installed and running. See: [https://ollama.com](https://ollama.com)

- **Model not found**  
  Make sure you’ve run `ollama pull mistral` (or your desired model), and that `assistant.py` uses the correct name.
