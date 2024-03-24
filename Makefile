install: #устанавливает зависимости в директорию .venv
	poetry install

brain-games: #запускает brain_games.py
	poetry run brain-games
