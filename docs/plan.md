# Capstone Project Plan

## Goal
Build a modular multi-agent system that can take a natural language task, decompose it, gather evidence, synthesize an answer, and validate it.

## Evaluation
- Create a small testset of 10 prompts and desired outputs.
- Measure Reviewer approval rate, length, and basic correctness (manual).

## Extensions
- Hook ResearchAgent to a real retriever (FAISS/Chroma) and LLMs.
- Add agent memory and long-term caching.
- Add user authentication and logging for reproducibility.
