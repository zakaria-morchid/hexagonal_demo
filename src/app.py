from mocks.gitlab import gl

# Appel simulé
projects = gl.projects.list()

# Utilisation normale
for p in projects:
    print(f"🔹 Project: {p.name}")
    print("    MRs:")
    for mr in p.mergerequests.list():
        for reviewer in mr.reviewers:
            reviewer_name = reviewer.get("name", "Inconnu")
            has_approved = reviewer.get("approved", False)
            print(f"      - {'OK' if has_approved else '  '} {reviewer_name}")
    print()