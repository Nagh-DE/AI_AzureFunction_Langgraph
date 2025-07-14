from langgraph.graph import END, START, StateGraph

from data import graphInput, graphOutput, graphContext
from nodes import (validate_id_node, 
                   invalid_id_node, 
                   fetch_messages_node, 
                   prepare_context_node,
                   summarize_sentiment_node,
                   raise_support_alert_node,
                   generate_response_node
                   )

sample_graph = StateGraph(graphContext, 
                          input=graphInput, 
                          output=graphOutput)


sample_graph.add_node("validate", validate_id_node)
sample_graph.add_node("invalid_id", invalid_id_node)
sample_graph.add_node("fetch", fetch_messages_node)
sample_graph.add_node("prepare", prepare_context_node)
sample_graph.add_node("summarize", summarize_sentiment_node)
sample_graph.add_node("raise_alert", raise_support_alert_node)
sample_graph.add_node("generate_response", generate_response_node)

sample_graph.add_edge(START, "validate")
sample_graph.add_conditional_edges(
        "validate",
        lambda state: "fetch" if state["is_id_valid"] else "invalid_id"
    )
sample_graph.add_edge("invalid_id", END)
sample_graph.add_edge("fetch", "prepare")
sample_graph.add_edge("prepare", "summarize")
# Branching from evaluation:
sample_graph.add_conditional_edges(
    "summarize",
    lambda state: "raise_alert" if state["sentiment_class"] == "negative" else "generate_response"

)

sample_graph.add_edge("raise_alert", "generate_response")
sample_graph.add_edge("generate_response",END)

sample_graph_executor = sample_graph.compile()
