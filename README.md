# Учебный проект для группы QAP22

## Команды

```bash
git clone https://github.com/qahelping/qap22_python_project
# Установите зависимости
pip install -r requirements.txt

# Линтеры
isort .
flake8
black .
```
## Запуск теста
```bash
pytest          # стандартный вывод
pytest -v       # подробные имена тестов
pytest -q       # тихий режим
pytest tests/test_pytest/test_intro.py -v -s --cache-clear --tb=short  # пример

```
## Флаги
```bash
#-s — не захватывать stdout/stderr (удобно для дебага print)
#--lf — запустить только “упавшие” на прошлом прогоне
#--ff — сначала упавшие, потом остальные
#--durations=10 — показать 10 самых долгих тестов
```bash

**Отбор тестов:**

```bash
pytest tests/test_python_org_wait.py   # один файл
pytest tests -k search                 # по подстроке в имени
pytest -k "not e2e"                    # исключить

```
## Запуск по маркеру
```bash
pytest -m e2e
```
## Поведение при падениях и отчёты:
```bash
pytest -x            # стоп на первом фейле
pytest --maxfail=1   # то же
pytest -ra           # причины skip/xfail
pytest -s            # показать print()/stdout
```
