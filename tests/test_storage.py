import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from app.storage import JsonTaskStore


class TestJsonTaskStore(unittest.TestCase):
    def test_add_and_load(self):
        with TemporaryDirectory() as tmp:
            store_path = Path(tmp) / "tasks.json"
            store = JsonTaskStore(store_path)

            self.assertEqual(store.load(), [])

            t1 = store.add("one")
            t2 = store.add("two")

            tasks = store.load()
            self.assertEqual([t.id for t in tasks], [1, 2])
            self.assertEqual([t.title for t in tasks], ["one", "two"])
            self.assertFalse(tasks[0].done)
            self.assertFalse(tasks[1].done)
            self.assertEqual(t1.id, 1)
            self.assertEqual(t2.id, 2)

    def test_done_and_delete(self):
        with TemporaryDirectory() as tmp:
            store_path = Path(tmp) / "tasks.json"
            store = JsonTaskStore(store_path)

            store.add("one")
            store.add("two")

            self.assertTrue(store.mark_done(2))
            tasks = store.load()
            self.assertEqual([t.done for t in tasks], [False, True])

            self.assertTrue(store.delete(1))
            tasks = store.load()
            self.assertEqual([t.id for t in tasks], [2])

            self.assertFalse(store.delete(999))
            self.assertFalse(store.mark_done(999))
