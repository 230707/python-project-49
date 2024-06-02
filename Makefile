# Makefile for 1st project Brain games

# установка зависимостей
install:
	poetry install

# запуск brain_games
brain-games:
	poetry run brain-games


# сборка проекта
build:
	poetry build


# публикация пакета, ранее созданного с помощью команды сборки
publish:
	poetry publish --dry-run


package-install:
	python3 -m pip install --user dist/*.whl

