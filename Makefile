install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

brain-games:
	poetry run brain-games

package-install:
	python -m pip install dist/*.whl
