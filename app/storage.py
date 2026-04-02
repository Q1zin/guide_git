from __future__ import annotations
import json
from typing import Iterable
from .models import Task
from pathlib import Path

class JsonTaskStore:
    def __init__(self, path: Path):
        self.path = path

    def load(self) -> list[Task]:
        if not self.path.exists():
            return []

        try:
            raw = json.loads(self.path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return []

        if not isinstance(raw, list):
            return []

        tasks: list[Task] = []
        for item in raw:
            if isinstance(item, dict):
                try:
                    tasks.append(Task.from_dict(item))
                except Exception:
                    continue
        return tasks

    def save(self, tasks: Iterable[Task]) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)

        payload = [t.to_dict() for t in tasks]
        tmp_path = self.path.with_suffix(self.path.suffix + ".tmp")
        tmp_path.write_text(
            json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        tmp_path.replace(self.path)

    def add(self, title: str) -> Task:
        tasks = self.load()
        next_id = (max((t.id for t in tasks), default=0) + 1) if tasks else 1
        task = Task.new(next_id, title)
        tasks.append(task)
        self.save(tasks)
        return task

    def mark_done(self, task_id: int) -> bool:
        tasks = self.load()
        updated = False
        new_tasks: list[Task] = []

        for task in tasks:
            if task.id == task_id:
                new_tasks.append(Task(id=task.id, title=task.title, done=True, created_at=task.created_at))
                updated = True
            else:
                new_tasks.append(task)

        if updated:
            self.save(new_tasks)
        return updated

    def delete(self, task_id: int) -> bool:
        tasks = self.load()
        new_tasks = [t for t in tasks if t.id != task_id]
        if len(new_tasks) == len(tasks):
            return False
        self.save(new_tasks)
        return True
