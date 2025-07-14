"""
Modèles de données pour les mocks.
"""

# pylint: disable=missing-class-docstring, too-many-instance-attributes
from dataclasses import dataclass
from typing import List, Optional

from enum import Enum
from datetime import datetime


class Source(Enum):
    GITLAB = "gitlab"
    GITHUB = "github"


class ProjectVisibility(str, Enum):
    PRIVATE = "private"
    INTERNAL = "internal"
    PUBLIC = "public"


class MergeRequestState(str, Enum):
    OPENED = "opened"
    CLOSED = "closed"
    MERGED = "merged"


@dataclass
class User:
    id: int
    username: str
    name: str


@dataclass
class Namespace:
    id: int
    name: str
    path: str


@dataclass
class Reviewer:
    user: User
    approved: bool


@dataclass
class MergeRequest:
    id: int
    title: str
    state: MergeRequestState
    project_id: int
    author: User
    reviewers: List[Reviewer]
    commit_sha: str
    merged_at: Optional[datetime] = None


@dataclass
class Tag:
    name: str
    committed_date: datetime
    author_name: str
    message: str


@dataclass
class Project:
    id: int
    name: str
    description: str
    visibility: ProjectVisibility
    web_url: str
    namespace: Namespace
    mergerequests: List[MergeRequest]
    source: Source
    tags: Optional[List[Tag]] = None
