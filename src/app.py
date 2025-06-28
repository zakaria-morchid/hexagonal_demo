from mocks.gitlab import gl
from mocks.github import gh
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
    
    
for project in gh.list_all_projects():
    print(f"🔹 Project: {project.name}")
    for mr in gh.list_merge_requests(project.id):
        print(f"  ▪ MR: {mr.title}")
        for reviewer in gh.list_reviewers_for_merge_request(project.id, mr.id):
            status = "✅" if reviewer.approved else "❌"
            print(f"    - {reviewer.user.name} {status}")