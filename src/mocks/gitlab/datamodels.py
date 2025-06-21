from dataclasses import dataclass

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
class MergeRequest:
    id: int
    title: str
    state: str
    project_id: int
