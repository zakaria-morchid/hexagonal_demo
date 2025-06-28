from .datamodels import Namespace, Project, MergeRequest, Reviewer, User
from .datamodels import Source
from random import choice, randint

# Utilisateurs de référence
users = [
    User(id=1, username="zmorchid", name="Zakaria"),
    User(id=2, username="souleyman", name="Souleyman"),
    User(id=3, username="cedric", name="Cédric"),
    User(id=4, username="nabil", name="Nabil"),
    User(id=5, username="amina", name="Amina"),
    User(id=6, username="lucas", name="Lucas"),
]

# Espaces de nommage
namespaces = [
    Namespace(id=1, name="iac", path="do-amont/automatisation/iac"),
    Namespace(id=2, name="middleware", path="do-amont/socle-technique/middleware"),
    Namespace(id=3, name="sti", path="do-amont/services-techniques-and-industrialisation/supervision"),
]

# Générateur de MergeRequest avec variations
def generate_merge_requests(project_id: int, count: int) -> list[MergeRequest]:
    mrs = []
    for i in range(count):
        author = choice(users)
        title = choice([
            "Fix login", "Improve error handling", "Add CI pipeline", "Refactor auth service", "Update README"
        ])
        reviewers = [
            Reviewer(user=choice(users), approved=bool(randint(0, 1)))
            for _ in range(randint(1, 3))
        ]
        mrs.append(MergeRequest(
            id=project_id * 100 + i,
            title=title,
            state=choice(["opened", "closed", "merged"]),
            project_id=project_id,
            author=author,
            reviewers=reviewers
        ))
    return mrs

# Projets variés
projects = [
    Project(
        id=1,
        name="infra-as-code",
        description="Provision infrastructure using code",
        visibility="private",
        web_url="https://fake.gitlab.com/iac/infra-as-code",
        namespace=namespaces[0],
        mergerequests=generate_merge_requests(1, 3),
        source=choice([Source.GITHUB, Source.GITLAB])
    ),
    Project(
        id=2,
        name="vault-as-code",
        description="Manage Vault secrets as code",
        visibility="public",
        web_url="https://fake.gitlab.com/iac/vault-as-code",
        namespace=namespaces[0],
        mergerequests=generate_merge_requests(2, 2),
        source=choice([Source.GITHUB, Source.GITLAB])
    ),
    Project(
        id=3,
        name="tomcat",
        description="Configuration de Tomcat pour production",
        visibility="internal",
        web_url="https://fake.gitlab.com/middleware/tomcat",
        namespace=namespaces[1],
        mergerequests=generate_merge_requests(3, 1),
        source=choice([Source.GITHUB, Source.GITLAB])
    ),
    Project(
        id=4,
        name="vmarket-ansible",
        description="Déploiement Ansible de VMarket",
        visibility="private",
        web_url="https://fake.gitlab.com/sti/vmarket-ansible",
        namespace=namespaces[2],
        mergerequests=generate_merge_requests(4, 0),
        source=choice([Source.GITHUB, Source.GITLAB])
    ),
    Project(
        id=5,
        name="docker-images",
        description="Gestion des images Docker de base",
        visibility="private",
        web_url="https://fake.gitlab.com/sti/docker-images",
        namespace=namespaces[2],
        mergerequests=generate_merge_requests(5, 4),
        source=choice([Source.GITHUB, Source.GITLAB])
    ),
]