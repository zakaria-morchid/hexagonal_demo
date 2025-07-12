"""
Module principal pour les mocks GitHub.
"""

from mocks.models.fake_data import projects
from .fake_github import FakeGithub

gh = FakeGithub(projects)

__all__ = ["gh"]
