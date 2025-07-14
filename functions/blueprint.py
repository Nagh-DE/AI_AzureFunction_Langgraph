from azure import functions as func

blueprint = func.Blueprint()

from .functions_task import task_function