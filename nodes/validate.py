
from data import graphInput
from data import mock_db
import logging

def validate_id_node(state: graphInput) -> str:
    id = state['id']
    logging.info(f"this is mock_data {mock_db}")
    if id not in mock_db.keys():
        return {"is_id_valid": False} # Update the state
    return {"is_id_valid": True}
