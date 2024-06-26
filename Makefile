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

# запуск brain_calc
brain-calc:
	poetry run brain_calc


# launch brain_gcd
brain-gcd:
	poetry run brain_gcd


# launch brain_progression
brain-progression:
	poetry run brain_progression


# launch brain-prime
brain-prime:
	poetry run braim_prime


# сборка проекта
build:
	poetry build

# публикация пакета, ранее созданного с помощью команды сборки
publish:
	poetry publish --dry-run

package-install:
	poetry run pip install ./dist/hexlet_code-0.1.0-py3-none-any.whl

# запускаем линтер
lint:
	poetry run flake8 brain_games
