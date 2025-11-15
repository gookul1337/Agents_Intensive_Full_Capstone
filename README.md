# Agents Intensive — Capstone Project (Full Build)

**Title:** Cooperative Multi-Agent Research & Writing System (Capstone)
**Author:** Your Name
**Date:** 2025-11-15

## Project Overview
This repository contains a capstone-ready multi-agent system that demonstrates a full pipeline:
- **PlannerAgent**: decomposes user tasks into sub-tasks.
- **ResearchAgent**: retrieves & summarizes evidence (stubbed / plugin hooks).
- **WriterAgent**: composes final deliverable using research outputs.
- **ReviewerAgent**: validates correctness, style, and safety.
- **Orchestrator**: runs the multi-agent workflow, logs chain-of-thought, and produces a final answer.

The system is designed to be extendable: integrate a real retriever (FAISS/Chroma), LLM APIs (OpenAI/Gemini), or web search tools easily.

## Highlights (what to include in the final submission)
- Problem statement & motivation
- Architecture diagram (in README or report)
- End-to-end demo (Flask web UI + CLI)
- Automated tests verifying agent interactions
- Deployment guide (Cloud Shell, Cloud Run, Docker)
- Evaluation: test cases and metrics (accuracy, reviewer approval rate)

## Quick start (Cloud Shell / Linux)
```bash
# clone your repo first, then run:
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
# Run demo server
python3 src/app.py
```
Then Web Preview -> port 5000 (Cloud Shell) or open http://localhost:5000 locally.

## Files of interest
- `src/agents/` — agent implementations
- `src/orchestrator.py` — runner & orchestration logic
- `src/app.py` — Flask demo UI + API
- `src/tools.py` — tool interfaces (search, summarize) + stubs
- `notebooks/demo.ipynb` — (stub) instructions for interactive demo
- `docs/` — deployment and evaluation guide

## How this meets capstone criteria
- Clear problem statement, pipeline, and evaluation plan.
- Modularity: easy to replace tools with real APIs.
- Reproducible: setup scripts, tests, and Dockerfile included.

Replace placeholder API keys and implement real connectors for best grading results.
