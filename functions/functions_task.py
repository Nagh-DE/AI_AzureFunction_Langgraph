import json
import logging
from http import HTTPStatus

from azure import functions as func

from graph import sample_graph_executor

from .blueprint import blueprint


@blueprint.function_name(name='function_name')  # update the function name as needed
@blueprint.route(route='route', methods=['POST'])       # update the route as needed
def task_function(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    req_body = req.get_json()
    if not req_body:
        return func.HttpResponse(
            "Invalid request body",
            status_code=HTTPStatus.BAD_REQUEST
        )
    customer_review_id = req_body.get('customer_review_id')
    evaluation_result = [
        sample_graph_executor.invoke(
            input={
                'id': customer_review_id,
            }
        )
    ]

    return func.HttpResponse(
        body=json.dumps(evaluation_result, default=lambda obj: obj.__dict__),
        status_code=HTTPStatus.OK,
    )
