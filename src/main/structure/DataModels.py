from datetime import datetime
from typing import Dict, List, Literal, TypedDict

Documents = List[Dict[Literal["text"], str]]


class Dataset (TypedDict):
    uploaded_at: datetime
    name: str
    size: int
    documents: List[Documents]
