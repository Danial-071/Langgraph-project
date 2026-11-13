from __future__ import annotations

from typing import TypedDict

from langgraph.graph import END, START, StateGraph


class WorkflowState(TypedDict):
    message: str
    processed_message: str
    audit_trail: list[str]


def sanitize_message(state: WorkflowState) -> WorkflowState:
    cleaned = state["message"].strip()
    return {
        **state,
        "message": cleaned,
        "audit_trail": [*state["audit_trail"], f"sanitized: {cleaned}"],
    }


def enrich_message(state: WorkflowState) -> WorkflowState:
    processed = f"Processed -> {state['message']}"
    return {
        **state,
        "processed_message": processed,
        "audit_trail": [*state["audit_trail"], f"enriched: {processed}"],
    }


def finalize(state: WorkflowState) -> WorkflowState:
    return {
        **state,
        "audit_trail": [*state["audit_trail"], "finalized"],
    }


def build_workflow():
    graph = StateGraph(WorkflowState)

    graph.add_node("sanitize_message", sanitize_message)
    graph.add_node("enrich_message", enrich_message)
    graph.add_node("finalize", finalize)

    graph.add_edge(START, "sanitize_message")
    graph.add_edge("sanitize_message", "enrich_message")
    graph.add_edge("enrich_message", "finalize")
    graph.add_edge("finalize", END)

    return graph.compile()


def run_example():
    workflow = build_workflow()
    return workflow.invoke(
        {
            "message": "  Build a graph based stateful workflow with LangGraph  ",
            "processed_message": "",
            "audit_trail": [],
        }
    )


if __name__ == "__main__":
    output = run_example()
    print("Final state:")
    print(output)
