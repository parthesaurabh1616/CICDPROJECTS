import unittest
from app.main import add_task, list_tasks, delete_task

class TestTodoApp(unittest.TestCase):

    def test_add_task(self):
        tasks = []
        tasks = add_task("Learn Python", tasks)
        self.assertIn("Learn Python", tasks)

    def test_delete_task(self):
        tasks = ["Learn Python", "Build CLI"]
        tasks = delete_task(0, tasks)
        self.assertNotIn("Learn Python", tasks)

if __name__ == '__main__':
    unittest.main()