.PHONY: run clean

run: run_cli run_api

run_cli:
	@PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python src/main/cli.py

run_api:
	curl http://localhost:8000/merge-requests
	curl "http://localhost:8000/pending-changes?since_version=v1.0.0&target_version=v1.0.1"

server:
	@PYTHONPATH=src python src/main/web.py

test:
	@PYTHONDONTWRITEBYTECODE=1  PYTHONPATH=src python -m pytest tests -vvv

format:
	@PYTHONDONTWRITEBYTECODE=1  PYTHONPATH=src black src

lint:
	PYTHONPATH=src pylint src/*

fl: format lint

clean:
	find . -type d -name '__pycache__' -exec rm -r {} +
