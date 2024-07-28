from datetime import datetime

from drf_spectacular.utils import OpenApiExample

# TODO: task
task_single_response_example = {
    "id": 0,
    "title": "string",
    "description": "string",
    "status": "queue",
    "created_at": datetime.now(),
    "url": "string",
}


task_create_request_example = {
    "title": "string",
    "description": "string",
    "status": "queue",
}

extend_schema_post = {
    "examples": [
        OpenApiExample(
            name=f"Task post request example",
            description="Пример запроса.",
            value=task_create_request_example,
            request_only=True,
        ),
        OpenApiExample(
            name=f"Task create response example",
            description="Пример ответа.",
            value=task_single_response_example,
            response_only=True,
        ),
    ],
    "summary": "Создать новую задачу",
    # "responses": {status.HTTP_201_CREATED: achievement_response_schema},
}
