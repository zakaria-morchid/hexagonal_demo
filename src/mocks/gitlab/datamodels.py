from dataclasses import dataclass
from typing import List

@dataclass
class Namespace:
    id: int
    name: str
    path: str

@dataclass
class Project:
    id: int
    name: str
    description: str
    visibility: str
    web_url: str
    namespace: Namespace
@dataclass
class Reviewer:
    name: str
    approved: bool
@dataclass
class MergeRequest:
    id: int
    title: str
    state: str
    project_id: int
    author_name: str
    reviewers: List[Reviewer] # liste de dicts avec `name` et `approved`



