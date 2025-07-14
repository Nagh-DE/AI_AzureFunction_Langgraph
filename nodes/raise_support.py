from data import graphContext
import logging

def raise_support_alert_node(state: graphContext) -> graphContext:
    print(f"[ALERT] Negative feedback detected for ID {state['id']}")
    # Implement your alert logic here, e.g., send an email or log to a monitoring system.
    logging.info(f"Alert raised for ID {state['id']} with sentiment: {state['sentiment_class']}")
    return state