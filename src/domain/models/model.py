"""
Module principal pour les modèles.
"""

# pylint: disable=too-few-public-methods, missing-class-docstring
from typing import List
from pydantic import BaseModel


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


__all__ = ["MergeRequest", "Approval"]
