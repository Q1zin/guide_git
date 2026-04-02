# guide_git

Небольшой учебный проект на Python: CLI‑менеджер задач (todo) с хранением в JSON.

## Что внутри

- `app/` — код приложения (парсер аргументов, модель, хранилище)
- `tests/` — минимальные тесты на `unittest`
- `data/tasks.json` — файл с задачами (создаётся автоматически, в git игнорируется)

## Требования

- Python 3.10+ (подойдёт и 3.11/3.12)

## Как запустить (macOS/Linux)

1) Создать виртуальное окружение:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2) Установить зависимости (здесь их нет, но команда полезна на будущее):

```bash
python -m pip install -r requirements.txt
```

3) Запуск CLI:

Показать помощь:

```bash
python -m app -h
```

Добавить задачу:

```bash
python -m app add "Купить молоко"
```

Список задач:

```bash
python -m app list
```

Отметить как выполненную:

```bash
python -m app done 1
```

Удалить задачу:

```bash
python -m app delete 1
```

## Где хранятся данные

По умолчанию задачи лежат в `data/tasks.json` (создаётся при первом `add`).

Можно указать другой файл:

```bash
python -m app --store /tmp/my_tasks.json add "Тест"
```

## Как запустить тесты

```bash
python -m unittest discover -s tests -v
```

## Альтернативный запуск

Можно запускать через `run.py` (эквивалентно):

```bash
python run.py list
```