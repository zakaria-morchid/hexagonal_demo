"""
Module principal pour les modèles de release.
"""

# pylint: disable=missing-class-docstring
from dataclasses import dataclass
from datetime import datetime
from typing import List

from enum import Enum


class Source(Enum):
    GITLAB = "gitlab"
    GITHUB = "github"


@dataclass
class Change:
    platform: Source
    project: str
    title: str
    author: str
    merged_at: datetime
    commit_sha: str


@dataclass
class PendingChanges:
    target_version: str
    changes: List[Change]
