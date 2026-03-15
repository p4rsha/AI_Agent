# AI Agent

A CLI-based AI agent built with Python and the Gemini API, developed as part of the Boot.dev AI agent course.

## Project Structure
- `main.py` — entry point, handles CLI input and Gemini API calls
- `functions/` — tools the agent can use (get file info, read files)
- `calculator/` — test project used by the agent
- `config.py` — shared configuration (MAX_CHARS limit)

## Usage
```sh
uv run main.py "your prompt here"
uv run main.py "your prompt here" --verbose
```