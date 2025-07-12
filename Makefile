.PHONY: run clean

run_cli:
	@PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python src/main/cli.py

run_api:
	curl http://localhost:8000/merge-requests

server:
	@PYTHONDONTWRITEBYTECODE=1  PYTHONPATH=src uvicorn main.web:app  --reload

test:
	@PYTHONDONTWRITEBYTECODE=1  PYTHONPATH=src python -m pytest tests -vvv

clean:
	find . -type d -name '__pycache__' -exec rm -r {} +
