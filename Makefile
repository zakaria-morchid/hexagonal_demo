.PHONY: run clean

run:
	@PYTHONDONTWRITEBYTECODE=1 python src/app.py

clean:
	find . -type d -name '__pycache__' -exec rm -r {} +
