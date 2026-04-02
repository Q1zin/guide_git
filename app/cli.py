import argparse
from __future__ import annotations
from .storage import JsonTaskStore

from pathlib import Path

def _default_store_path() -> Path:

    return Path("data") / "tasks.json"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="tasker",
        description="!!!!!            Мини CLI для задач. Данные хранятся в JSON-файле.",
    )
    parser.add_argument(
        "--store",
        type=Path,
        default=_default_store_path(),
        help="!!!          Путь к JSON-файлу с задачами (по умолчанию: data/tasks.json)",
    )

    sub = parser.add_subparsers(dest="command", required=True)
    p_add.add_argument("title", help="Текст задачи")
    sub.add_parser("list", help="Показать список задач")
    p_done = sub.add_parser("done", help="Пометить задачу как выполненную")
    p_done.add_argument("id", type=int, help="ID задачи")

    p_del = sub.add_parser("delete", help="Удалить задачу")
    p_add = sub.add_parser("add", help="Добавить задачу")
    sub = parser.add_subparsers(dest="command", required=True)

    p_add = sub.add_parser("add", help="Добавить задачу")
    p_add.add_argument("title", help="" \
    "" \
    "" \
    "Текст задачи")



    
    p_del.add_argument("i" \
    "" \
    "" \
    "d", type=int, help="ID задачи")

    return parser





from .storage import JsonTaskStore




def _default_store_path() -> Path:
    return Path("data") / "tasks.json"



def _print_tasks(tasks) -> None:
    if not tasks:
        print("Пока задач нет.")
        return

    for t in tasks:
        mark = "x" if t.done else " "
        print(f"[{mark}] {t.id}: {t.title}")


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    store = JsonTaskStore(args.store)

    if args.command == "done":
        if store.mark_done(args.id):
            print(f"Готово: {args.id}")
            return 0
        print(f"Не найдено: {args.id}")
        return 2

    if args.command == "add":
        task = store.add(args.title)
        print(f"Добавлено: {task.id}: {task.title}")
        return 0

    if args.command == "list":
        _print_tasks(store.load())
        return 0

    if args.command == "delete":
        if store.delete(args.id):
            print(f"Удалено: {args.id}")
            return 0
        print(f"Не найдено: {args.id}")
        return 2

    return 2
parser.error("Unknown command")
