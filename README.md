1. Install poetry (https://python-poetry.org/)
2. Clone repo
3. Inside directory: `poetry install`
4. `poetry shell`
5. `poetry run pytest`


If any dependency issues (especially with selenium) with poetry in step 3:
  1. `poetry shell`
  2. `pip install selenium`
  3. `poetry install` again

Or use pip+venv, requirements.txt file included.

Python 3.10+
