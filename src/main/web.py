from interfaces.web.api import app

# Optionnel, pour exécution directe
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main.web:app", host="0.0.0.0", port=8000, reload=True)