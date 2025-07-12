"""
Modèles de données pour les mocks.
"""

# pylint: disable=missing-class-docstring, too-many-instance-attributes
from dataclasses import dataclass
from typing import List

from enum import Enum


class Source(Enum):
    GITLAB = "gitlab"
    GITHUB = "github"


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
    state: str
    project_id: int
    author: User
    reviewers: List[Reviewer]


@dataclass
class Project:
    id: int
    name: str
    description: str
    visibility: str
    web_url: str
    namespace: Namespace
    mergerequests: List[MergeRequest]
    source: Source
