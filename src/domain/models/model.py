"""
Module principal pour les modèles.
"""

# pylint: disable=too-few-public-methods, missing-class-docstring
from dataclasses import dataclass
from typing import List


@dataclass
class Approval:
    name: str
    approved: bool


@dataclass
class MergeRequest:
    platform: str
    project: str
    title: str
    state: str
    author: str
    approvals: List[Approval]


__all__ = ["MergeRequest", "Approval"]
