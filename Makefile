.PHONY: run clean

run:
	@PYTHONDONTWRITEBYTECODE=1 python src/app.py

test:
	@PYTHONDONTWRITEBYTECODE=1  PYTHONPATH=src python -m pytest tests -vvv

run_api:
	@PYTHONDONTWRITEBYTECODE=1 python src/run_api.py

clean:
	find . -type d -name '__pycache__' -exec rm -r {} +
