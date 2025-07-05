def display_merge_requests(provider, username=None):
    print(f"🛠️  [{provider.name}]")
    for mr in provider.list_merge_requests(username=username):
        print(f"  ▪ {mr['project']}")
        print(f"  ▪ {mr['title']} ({mr['state']})")
        print(f"    Auteur : {mr['author']}")
        for approval in mr["approvals"]:
            print(f"     - {'OK' if approval['approved'] else '  '} {approval['name']}")
