from typing import TypedDict, List, Literal


class graphInput(TypedDict):
    id: str


class graphContext(graphInput):
    id: str
    messages: List[str]
    cleaned_messages: List[str]
    sentiment_summary: str
    sentiment_class: Literal["positive", "negative", "neutral"]
    is_id_valid: bool


class graphOutput(TypedDict):
    id: str
    sentiment_summary: str
    status_message: str