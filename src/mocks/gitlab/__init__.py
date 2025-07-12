"""
Module principal pour les mocks GitLab.
"""

from mocks.models.fake_data import projects
from .fake_gitlab import FakeGitlab

gl = FakeGitlab(projects)

__all__ = ["gl"]
