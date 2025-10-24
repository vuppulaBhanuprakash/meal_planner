# Nutritional Meal Suggesting AI

An end-to-end meal planning assistant built with [CrewAI](https://github.com/crewAIInc/crewAI).  
The crew orchestrates multiple LLM-powered agents to craft a culturally aware meal plan, derive a matching grocery list, and summarize nutritional insights tailored to the user.

## Key Capabilities
- Generates personalized meal plans using the latest request and stored user preferences.
- Suggests grocery lists with substitutions for hard-to-find ingredients.
- Produces at-a-glance nutritional breakdowns to stay aligned with health goals.
- Formats everything into a human-friendly summary ready for sharing.

## Prerequisites
- Python 3.12 or newer (3.11 works in practice but 3.12+ matches the project configuration).
- [`uv`](https://docs.astral.sh/uv/getting-started/installation/) for dependency and virtualenv management.
- An OpenAI API key with access to the GPT-4o mini family (set in `.env`).

## Quick Start

1. **Install dependencies with uv**
   ```bash
   uv sync
   ```
   This creates `.venv/` and installs everything declared in `pyproject.toml`.

2. **Activate the virtual environment**
   ```bash
   source .venv/bin/activate
   ```

3. **Configure API access**
   - Copy `ai_meal_planner/.env` (or create your own).
   - Set `OPENAI_API_KEY=<your-openai-key>` and update `MODEL` if needed.

4. **Run the crew**
   ```bash
   cd ai_meal_planner
   crewai run
   ```
   The CLI will execute the sequential crew defined in `src/ai_meal_planner/crew.py`.

## Project Layout

```
.
├── ai_meal_planner/
│   ├── knowledge/               # Domain knowledge used by agents
│   ├── src/ai_meal_planner/
│   │   ├── config/              # YAML definitions for agents & tasks
│   │   ├── crew.py              # Crew composition
│   │   └── main.py              # Entry point (loads env, kicks off crew)
│   └── pyproject.toml           # Crew package metadata (installed via uv sync)
├── pyproject.toml               # Root project metadata
└── uv.lock                      # Locked dependency versions
```

## Customizing The Experience
- **Adjust prompts** by editing `src/ai_meal_planner/config/agents.yaml` or `tasks.yaml`.
- **Swap models** by changing `MODEL` in `.env` or per-agent `llm` values in the YAML.
- **Extend knowledge** with additional files under `ai_meal_planner/knowledge/`.
- **Integrate outputs** by consuming the Markdown files in `outputs/` or modifying `output_formatting_task`.

## Troubleshooting
- Make sure the virtual environment is active before running `crewai run`.
- If you see `ModuleNotFoundError`, re-run `uv sync` inside the project root.
- Invalid API credentials will surface as `401`/`403` errors during inference; re-check `.env`.

Enjoy crafting nutrition-aware meal plans with your CrewAI-powered assistant!
