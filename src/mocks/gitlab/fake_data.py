from .datamodels import Namespace, Project, MergeRequest, Reviewer

namespace_iac = Namespace(id=1, name="iac", path="do-amont/automatisation/iac")
namespace_middleware = Namespace(id=2, name="middleware", path="do-amont/socle-technique/middleware")
namespace_sti = Namespace(id=3, name="sti", path="do-amont/services-techniques-and-industrialisation/supervision")

projects = [
    Project(
        id=1,
        name="infra-as-code",
        description="infrastructure as code",
        visibility="private",
        web_url=f"https://fake.gitlab.com/{namespace_iac.path}/infra-as-code",
        namespace=namespace_iac
    ),
    Project(
        id=2,
        name="vault-as-code",
        description="vault as code",
        visibility="private",
        web_url=f"https://fake.gitlab.com/{namespace_iac.path}/vault-as-code",
        namespace=namespace_iac
    ),
    Project(
        id=3,
        name="tomcat",
        description="tomcat",
        visibility="private",
        web_url=f"https://fake.gitlab.com/{namespace_middleware.path}/tomcat",
        namespace=namespace_middleware
    ),
    Project(
        id=4,
        name="vmarket-ansible",
        description="vmarket ansible",
        visibility="private",
        web_url=f"https://fake.gitlab.com/{namespace_sti.path}/vmarket-ansible",
        namespace=namespace_sti
    )
]

merge_requests = [
    MergeRequest(
        id=101,
        title="Fix login",
        state="opened",
        project_id=1,
        author_name="Zakaria",
        reviewers=[
            Reviewer(name="Souleyman", approved=True),
            Reviewer(name="Cédric", approved=False)
        ]
    ),
    MergeRequest(
        id=102,
        title="Refactor infra module",
        state="merged",
        project_id=2,
        author_name="Nabil",
        reviewers=[
            Reviewer(name="Zakaria", approved=True)
        ]
    ),
]
