from mocks.gitlab import gl

# Appel simulé
projects = gl.projects.list()

# Utilisation normale
for p in projects:
    print(f"🔹 Project: {p.name} ({p.visibility})")
    print(f"    Namespace: {p.namespace.name}/{p.namespace.path}")
    print("    Merge Requests:")
    for mr in p.mergerequests.list():
        print(f"      - [{mr.state.upper()}] {mr.title}")
    print()