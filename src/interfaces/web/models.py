from pydantic import BaseModel
from typing import Optional, List

class ChangeDTO(BaseModel):
    project: str
    title: str
    author: str
    merged_at: Optional[str]
    platform: Optional[str] = None
    commit_sha: Optional[str] = None


class PendingChangesDTO(BaseModel):
    target_version: str
    changes: List[ChangeDTO]



