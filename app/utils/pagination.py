from typing import List, TypeVar, Generic
from pydantic import BaseModel
from fastapi import Query

T = TypeVar("T", bound=BaseModel)

class PaginatedResponse(Generic[T]):
    def __init__(self, items: List[T], total: int, skip: int, limit: int):
        self.items = items
        self.total = total
        self.skip = skip
        self.limit = limit

def paginate(query, skip: int = 0, limit: int = 10):
    total = query.count()
    items = query.offset(skip).limit(limit).all()
    return PaginatedResponse(items=items, total=total, skip=skip, limit=limit)
