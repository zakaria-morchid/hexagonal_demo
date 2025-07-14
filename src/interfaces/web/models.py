"""
Module principal pour les modèles de la web API.
"""

# pylint: disable=missing-class-docstring
from typing import Optional, List
from pydantic import BaseModel


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
