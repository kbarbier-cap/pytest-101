PROJECT_SLUG := python_unit_tests_101
.PHONY: test

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache


install_env: ## isntall dependencies and the root package
	pip install -e .

task_preprocessing:
	python src/$(PROJECT_SLUG)/tasks/preprocessing_task.py

task_features_engineering:
	python src/$(PROJECT_SLUG)/tasks/features_engineering_task.py

test:
	pytest tests/ --cov $(PROJECT_SLUG)