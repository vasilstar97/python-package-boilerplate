SOURCE_DIR = my_package
TEST_DIR = tests

lint:
	pylint ${SOURCE_DIR}

format:
	isort ${SOURCE_DIR}
	black ${SOURCE_DIR}

venv: # затем необходимо активировать: source .venv/bin/activate
	python3 -m venv .venv

install: # простая установка зависимостей без editable режима
	pip install .

install-dev: # установка зависимостей для разработки включая dev
	pip install -e '.[dev]'

install-docs: # установка зависимостей включая docs
	pip install -e '.[docs]'

build:
	python3 -m build .

clean:
	rm -rf ./build ./dist ./${SOURCE_DIR}.egg-info

pypi: clean build # команда для сборки и загрузки в pypi
	python3 -m twine upload dist/*

test-pypi: clean build # команда для сборки и загрузки в тестовый pypi
	python3 -m twine upload --repository testpypi dist/*

test: # тестирование
	pytest ${TEST_DIR}

test-cov: # тестирование с выводом процента покрытия кода тестами
	pytest ${TEST_DIR} --cov