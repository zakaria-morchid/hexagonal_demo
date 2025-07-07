from pydantic import BaseModel
from typing import List

class Approval(BaseModel):
    name: str
    approved: bool

class MergeRequest(BaseModel):
    platform: str
    project: str
    title: str
    state: str
    author: str
    approvals: List[Approval]