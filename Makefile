# Makefile for 1st project Brain games

# установка зависимостей
install:
	@echo "Running poetry install"
	poetry install

# запуск brain_games
brain-games:
	poetry run brain-games

# запуск brain_even
brain-even:
	poetry run brain_even

# сборка проекта
build:
	poetry build

# публикация пакета, ранее созданного с помощью команды сборки
publish:
	poetry publish --dry-run

package-install:
	poetry run pip install dist/*.whl

# запускаем линтер
make lint:
	poetry run flake8 brain_games