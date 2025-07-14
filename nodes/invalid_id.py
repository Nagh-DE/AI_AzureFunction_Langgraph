from data import graphContext, graphOutput
import logging

def invalid_id_node(state: graphContext) -> graphOutput:
    logging.info(f"Handling invalid ID: {state['id']}")
    return {
        "sentiment_summary": "NA",
        "status_message": f"ID '{state['id']}' not found."
    }