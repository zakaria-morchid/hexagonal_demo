.PHONY: run clean

run:
	@PYTHONDONTWRITEBYTECODE=1 python src/app.py

test:
	@PYTHONDONTWRITEBYTECODE=1  PYTHONPATH=src python -m pytest tests -vvv

clean:
	find . -type d -name '__pycache__' -exec rm -r {} +
