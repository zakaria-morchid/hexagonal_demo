"""
Module principal pour le serveur web.
"""

import uvicorn


def run_web():
    """
    Exécute le serveur web.
    """
    uvicorn.run("interfaces.web.api:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    run_web()
