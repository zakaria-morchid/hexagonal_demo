import gitlab
from unittest.mock import MagicMock
from .fake_data import projects, merge_requests

def to_mock_project(project):
    mock = MagicMock()
    mock.id = project.id
    mock.name = project.name
    mock.description = project.description
    mock.visibility = project.visibility
    mock.web_url = project.web_url
    namespace_mock = MagicMock()
    namespace_mock.id = project.namespace.id
    namespace_mock.name = project.namespace.name
    namespace_mock.path = project.namespace.path
    mock.namespace = namespace_mock
    return mock

def to_mock_merge_request(mr):
    mock = MagicMock()
    mock.id = mr.id
    mock.title = mr.title
    mock.state = mr.state
    mock.project_id = mr.project_id
    return mock

def get_mock_gitlab_client():
    gl = gitlab.Gitlab('https://fake.gitlab.com', private_token='fake')

    mock_projects = [to_mock_project(p) for p in projects]
    mock_merge_requests = [to_mock_merge_request(mr) for mr in merge_requests]

    gl.projects.list = MagicMock(return_value=mock_projects)

    def get_merge_requests(project_id):
        return [mr for mr in mock_merge_requests if mr.project_id == project_id]

    for mock_project in mock_projects:
        mock_project.mergerequests.list = MagicMock(
            return_value=get_merge_requests(mock_project.id)
        )

    return gl
