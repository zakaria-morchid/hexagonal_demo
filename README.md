# hexagonal_demo

| Dossier                     | Rôle en architecture hexagonale                               |
| --------------------------- | ------------------------------------------------------------- |
| `domain/models/`            | 📦 Entités métiers (`MergeRequest`, etc.)                     |
| `domain/ports/`             | 🔌 Ports (interfaces abstraites : ex. `MergeRequestProvider`) |
| `domain/usecases/`          | 💡 Cas d’usage métier (`ListMergeRequestsUseCase`)            |
| `infrastructure/providers/` | 🧱 Adaptateurs secondaires (`GitHub`, `GitLab`, etc.)         |
| `mocks/`                    | 🧪 Stubs/fakes pour tests                                     |
| `app.py`                    | 🎯 Point d’entrée (exécution, CLI, etc.)                      |
| `tests/`                    | 🧪 Tests unitaires et d’intégration                            |