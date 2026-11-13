# Langgraph-project

This repository contains a minimal **LangGraph** example for building a graph-based, stateful workflow.

## What it demonstrates

- **Nodes** are Python functions that update shared workflow state.
- **Edges** define how state flows from one node to the next.
- A compiled graph runs from `START` to `END` while carrying and updating the same state object.

The workflow in `workflow.py` has three nodes:

1. `sanitize_message`
2. `enrich_message`
3. `finalize`

Flow:

`START -> sanitize_message -> enrich_message -> finalize -> END`

## Run locally

```bash
python -m pip install -r requirements.txt
python workflow.py
```

Example output includes the final state and an `audit_trail` showing each node transition.
