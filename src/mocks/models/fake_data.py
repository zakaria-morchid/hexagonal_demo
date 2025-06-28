from .datamodels import Namespace, Project, MergeRequest, Reviewer, User
from .datamodels import Source


zakaria = User(id=1, username="zmorchid", name="Zakaria")
souleyman = User(id=2, username="souleyman", name="Souleyman")
cedric = User(id=3, username="cedric", name="Cédric")
nabil = User(id=4, username="nabil", name="Nabil")

namespace_iac = Namespace(id=1, name="iac", path="do-amont/automatisation/iac")
namespace_middleware = Namespace(id=2, name="middleware", path="do-amont/socle-technique/middleware")
namespace_sti = Namespace(id=3, name="sti", path="do-amont/services-techniques-and-industrialisation/supervision")


merge_requests_project_1 = [
    MergeRequest(
        id=101,
        title="Fix login",
        state="opened",
        project_id=1,
        author=zakaria,
        reviewers=[
            Reviewer(user=souleyman, approved=True),
            Reviewer(user=cedric, approved=False)
        ]
    ),
    MergeRequest(
        id=102,
        title="Refactor infra module",
        state="opened",
        project_id=1,
        author=nabil,
        reviewers=[
            Reviewer(user=zakaria, approved=True)
        ]
    ),
]

merge_requests_project_2 = [
    MergeRequest(
        id=201,
        title="Fix login",
        state="opened",
        project_id=2,
        author=zakaria,
        reviewers=[
            Reviewer(user=souleyman, approved=True),
            Reviewer(user=cedric, approved=False)
        ]
    ),
]

merge_requests_project_3 = []

merge_requests_project_4 = []

projects = [
    Project(
        id=1,
        name="infra-as-code",
        description="infrastructure as code",
        visibility="private",
        web_url=f"https://fake.gitlab.com/{namespace_iac.path}/infra-as-code",
        namespace=namespace_iac,
        mergerequests=merge_requests_project_1,
        source=Source.GITLAB
    ),
    Project(
        id=2,
        name="vault-as-code",
        description="vault as code",
        visibility="private",
        web_url=f"https://fake.gitlab.com/{namespace_iac.path}/vault-as-code",
        namespace=namespace_iac,
        mergerequests=merge_requests_project_2,
        source=Source.GITHUB
    ),
    Project(
        id=3,
        name="tomcat",
        description="tomcat",
        visibility="private",
        web_url=f"https://fake.gitlab.com/{namespace_middleware.path}/tomcat",
        namespace=namespace_middleware,
        mergerequests=merge_requests_project_3,
        source=Source.GITHUB
    ),
    Project(
        id=4,
        name="vmarket-ansible",
        description="vmarket ansible",
        visibility="private",
        web_url=f"https://fake.gitlab.com/{namespace_sti.path}/vmarket-ansible",
        namespace=namespace_sti,
        mergerequests=merge_requests_project_4,
        source=Source.GITHUB
    )
]
