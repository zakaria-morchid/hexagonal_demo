"""
Préparation des données de test pour les projets, les utilisateurs, les espaces de nommage, etc.
"""

# pylint: disable=line-too-long
import random
import string
from random import choice, randint
from datetime import datetime, timedelta
from typing import Optional

from .datamodels import (
    Namespace,
    Project,
    MergeRequest,
    Reviewer,
    User,
    MergeRequestState,
    ProjectVisibility,
    Tag,
    Source,
)

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
    Namespace(
        id=3,
        name="sti",
        path="do-amont/services-techniques-and-industrialisation/supervision",
    ),
]

# Tags
tags = [
    Tag(
        name="v1.0.0",
        committed_date=datetime.now() - timedelta(days=10),
        author_name="zmorchid",
        message="Initial release",
    ),
    Tag(
        name="v1.0.1",
        committed_date=datetime.now() - timedelta(days=5),
        author_name="zmorchid",
        message="Minor changes",
    ),
]


def _generate_commit_sha(length=40) -> str:
    return "".join(random.choices("abcdef" + string.digits, k=length))


# Générateur de MergeRequest avec variations
def generate_merge_requests(
    project_id: int, count: int, state: Optional[MergeRequestState] = None
) -> list[MergeRequest]:
    """
    Génère une liste de MergeRequest pour un projet donné.
    """
    mrs = []
    for i in range(count):
        author = choice(users)
        title = choice(
            [
                "Fix login",
                "Improve error handling",
                "Add CI pipeline",
                "Refactor auth service",
                "Update README",
                "Add new feature",
                "Fix bug",
                "Refactor code",
                "Add new test",
                "Update documentation",
            ]
        )
        reviewers = [
            Reviewer(user=choice(users), approved=bool(randint(0, 1)))
            for _ in range(randint(1, 3))
        ]

        if state is None:
            state = choice(
                [
                    MergeRequestState.OPENED,
                    MergeRequestState.CLOSED,
                    MergeRequestState.MERGED,
                ]
            )

        # ✅ merged_at uniquement si Merged
        merged_at = None
        if state == MergeRequestState.MERGED:
            merged_at = datetime.now() - timedelta(days=randint(1, 15))

        commit_sha = _generate_commit_sha()

        mrs.append(
            MergeRequest(
                id=project_id * 100 + i,
                title=title,
                state=state,
                project_id=project_id,
                author=author,
                reviewers=reviewers,
                commit_sha=commit_sha,
                merged_at=merged_at,
            )
        )
    return mrs


# Projets variés
projects = [
    Project(
        id=1,
        name="infra-as-code",
        description="Provision infrastructure using code",
        visibility=ProjectVisibility.PRIVATE,
        web_url="https://fake.gitlab.com/iac/infra-as-code",
        namespace=namespaces[0],
        mergerequests=generate_merge_requests(1, 2, MergeRequestState.MERGED),
        source=Source.GITLAB,
        tags=tags,
    ),
    Project(
        id=2,
        name="vault-as-code",
        description="Manage Vault secrets as code",
        visibility=ProjectVisibility.PUBLIC,
        web_url="https://fake.gitlab.com/iac/vault-as-code",
        namespace=namespaces[0],
        mergerequests=generate_merge_requests(2, 2, MergeRequestState.MERGED),
        source=Source.GITHUB,
        tags=tags,
    ),
    Project(
        id=3,
        name="tomcat",
        description="Configuration de Tomcat pour production",
        visibility=ProjectVisibility.INTERNAL,
        web_url="https://fake.gitlab.com/middleware/tomcat",
        namespace=namespaces[1],
        mergerequests=generate_merge_requests(3, 4),
        source=choice([Source.GITHUB, Source.GITLAB]),
        tags=tags,
    ),
    Project(
        id=4,
        name="vmarket-ansible",
        description="Déploiement Ansible de VMarket",
        visibility=ProjectVisibility.PRIVATE,
        web_url="https://fake.gitlab.com/sti/vmarket-ansible",
        namespace=namespaces[2],
        mergerequests=generate_merge_requests(4, 4),
        source=choice([Source.GITHUB, Source.GITLAB]),
        tags=tags,
    ),
    Project(
        id=5,
        name="docker-images",
        description="Gestion des images Docker de base",
        visibility=ProjectVisibility.PRIVATE,
        web_url="https://fake.gitlab.com/sti/docker-images",
        namespace=namespaces[2],
        mergerequests=generate_merge_requests(5, 4),
        source=choice([Source.GITHUB, Source.GITLAB]),
        tags=tags,
    ),
]
