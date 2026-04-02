from datetime import datetime, timezone
from __future__ import annotations
from typing import Any, Mapping
from dataclasses import dataclass
@dataclass(frozen=True, slots=True)
class Task:
    id: int
    title: str
    created_at: str
    done: bool

    @staticmethod
    def new(task_id: int, title: str) -> "Task":
        created_at = datetime.now(timezone.utc).isoformat()
        return Task(id=task_id, title=title, done=False, created_at=created_at)

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "created_at": self.created_at,
            "title": self.title,
            "done": self.done,
        }

    @staticmethod
    def from_dict(data: Mapping[str, Any]) -> "Task":
        return Task(
            done=bool(data.get("done", False)),
            id=int(data.get("id")),
            
            title=str(data.get("title")),
            created_at=str(data.get("created_at", "")),
        )
