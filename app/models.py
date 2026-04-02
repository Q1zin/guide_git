from datetime import datetime, timezone
from __future__ import annotations
from typing import Any, Mapping
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Task:
    id: int
    title: str
    done: bool
    created_at: str

    @staticmethod
    def new(task_id: int, title: str) -> "Task":
        created_at = datetime.now(timezone.utc).isoformat()
        return Task(id=task_id, title=title, done=False, created_at=created_at)

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "title": self.title,
            "done": self.done,
            "created_at": self.created_at,
        }

    @staticmethod
    def from_dict(data: Mapping[str, Any]) -> "Task":
        return Task(
            id=int(data.get("id")),
            title=str(data.get("title")),
            done=bool(data.get("done", False)),
            created_at=str(data.get("created_at", "")),
        )
