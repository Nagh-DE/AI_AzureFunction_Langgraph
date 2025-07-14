from data import graphContext


def prepare_context_node(state: graphContext) -> graphContext:
    cleaned = [msg.lower().strip() for msg in state["messages"]]
    return {"cleaned_messages":cleaned}