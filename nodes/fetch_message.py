from data import graphContext
from data import mock_db
import logging

def fetch_messages_node(state: graphContext) -> graphContext:
    id = state['id']
    logging.info(f"Fetching messages for ID: {id}")
    fetched_summary = mock_db.get(id, "No data found for this ID.") # Use .get for safety
    
    # Simulate fetching messages (if mock_db only stores summary)
    # In a real scenario, mock_db[id] might be a list of messages.
    # For now, let's just make sure 'messages' is a list.
    
    logging.info(f"Fetched summary for '{id}': {fetched_summary}")
    return {
        "messages": fetched_summary,
    }