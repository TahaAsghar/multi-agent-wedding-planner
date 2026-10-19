# Multi-Agent Wedding Planner

A wedding planner with a [Streamlit](https://streamlit.io/) UI and a CLI. You describe the event; a LangChain supervisor agent delegates web research to two subagents, then synthesizes a plan.

The model is [Ollama](https://ollama.com/) `llama3.2`. Subagents search the web with [Tavily](https://tavily.com/).

## How it works

```
You (wedding brief)
        │
        ▼
Streamlit UI  or  CLI
        │
        ▼
   MainAgent (planner)
        │
        ├── assign_to_subagent1 ──► SubAgent1 ──► Tavily search
        └── assign_to_subagent2 ──► SubAgent2 ──► Tavily search
        │
        ▼
  Combined wedding plan
```

1. You enter a structured brief (UI) or free-text requirements (CLI).
2. The **MainAgent** breaks those requirements into research questions and assigns them to **SubAgent1** and **SubAgent2**.
3. Each subagent uses the `search_web` tool (Tavily) and returns findings.
4. The main agent reviews all results and produces one coherent plan. It is instructed not to invent vendor details or prices.

## Prerequisites

- Python **3.14+**
- [uv](https://docs.astral.sh/uv/) for dependency management
- [Ollama](https://ollama.com/) running locally, with the `llama3.2` model:

  ```bash
  ollama pull llama3.2
  ```

- A [Tavily](https://tavily.com/) API key
- For the Streamlit UI: an `OPENAI_API_KEY` in `.env`, Streamlit secrets, or the sidebar (the generate button stays disabled until both OpenAI and Tavily keys are present). The agents themselves still use Ollama via `llm.py`.

## Setup

```bash
git clone <repo-url>
cd multi-agent-wedding-planner
uv sync
```

Create a `.env` file in the project root:

```
TAVILY_API_KEY=your_tavily_api_key
OPENAI_API_KEY=your_openai_api_key
```

## Run the Streamlit UI

Start Ollama, then:

```bash
uv run streamlit run app_ui.py
```

The app opens in the browser. You can:

- Fill in the **Wedding Brief** (couple, location, date, guests, budget, style, priorities, must-haves, constraints, traditions)
- Load a sample brief from the sidebar
- Generate a plan once API keys are ready
- Review the latest plan, the input brief, and the agent architecture
- Download the plan as Markdown
- See recent runs in the sidebar

You can also paste keys in the sidebar instead of using `.env`.

## Run the CLI

```bash
uv run python main.py
```

When prompted, enter requirements such as:

```text
Outdoor wedding in Austin, TX, 120 guests, $25k budget, spring 2027, Mexican-American food, live mariachi
```

The agent logs progress (subagent assignments) and prints the final plan.

## Project layout

| File | Role |
|------|------|
| `app_ui.py` | Streamlit UI: brief form, status, results, Markdown export |
| `main.py` | CLI entry point; builds and invokes the main agent |
| `agents.py` | Subagents and `assign_to_subagent1` / `assign_to_subagent2` tools |
| `tools.py` | Tavily `search_web` tool |
| `llm.py` | Shared `ChatOllama` client (`llama3.2`, temperature `0`) |
| `prompts.py` | Main agent system prompt and user kickoff message |

## Configuration

To use a different Ollama model, change `llm.py`:

```python
llm = ChatOllama(model="llama3.2", temperature=0)
```
