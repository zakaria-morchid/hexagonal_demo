"""
Module principal pour les modèles de release.
"""

# pylint: disable=missing-class-docstring, too-many-instance-attributes
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


class ReleaseStatus(str, Enum):
    DRAFT = "draft"
    PUBLISHED = "published"
    CANCELLED = "cancelled"


@dataclass
class Release:
    platform: Source
    tag: str
    changes: List[Change]
    created_by: str
    created_at: datetime
    version: str
    validated: bool = False
    status: ReleaseStatus = ReleaseStatus.DRAFT
