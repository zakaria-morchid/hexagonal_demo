from mocks.gitlab import gl

# Appel simulé
projects = gl.projects.list()

# Utilisation normale
for p in projects:
    print(f"🔹 Project: {p.name}")
    print("    MRs:")
    mr_manager = gl.projects.get_merge_requests(p.id)
    for mr in mr_manager.list():
        print(f"      - {mr.title} ({mr.state})")
        for reviewer in mr.reviewers:
            has_approved = reviewer.approved
            print(f"           - {'OK' if has_approved else '  '} {reviewer.user.name}")
    print()