import pytest
from core import TaskManager


def test_create_task():
    # Test that creating a task adds it to the list of tasks.
    tm = TaskManager('test_tasks.json')
    tm.create_task('1', '2', '3')
    task = tm.read_task('1')
    assert task['title'] == '1'
    assert task['content'] == '2'
    assert task['priority'] == '3'
    with open('test_tasks.json', "w") as f:
        pass


def test_read_task():
    # Test that reading a task returns the correct task.
    tm = TaskManager('test_tasks.json')
    with pytest.raises(ValueError):
        tm.read_task('non-existing task')
    tm.create_task('1', '2', '3')
    task = tm.read_task('1')
    assert task['title'] == '1'
    assert task['content'] == '2'
    assert task['priority'] == '3'
    with open('test_tasks.json', "w") as f:
        pass


def test_update_task():
    # Test that updating a task changes its properties.
    tm = TaskManager('test_tasks.json')
    with pytest.raises(ValueError):
        tm.update_task('non-existing task')
    tm.create_task('1', '2', '3')
    tm.update_task('1', new_title='4', new_content='5')
    task = tm.read_task('4')
    assert task['title'] == '4'
    assert task['content'] == '5'
    assert task['priority'] == '3'
    with open('test_tasks.json', "w") as f:
        pass


def test_delete_task():
    # Test that deleting a task removes it from the list of tasks.
    tm = TaskManager('test_tasks.json')
    with pytest.raises(ValueError):
        tm.delete_task('non-existing task')
    tm.create_task('1', '2', '3')
    tm.delete_task('1')
    with pytest.raises(ValueError):
        tm.read_task('title')
    with open('test_tasks.json', "w") as f:
        pass


def test_list_tasks():
    # Test that listing tasks returns a list sorted by priority.
    tm = TaskManager('test_tasks.json')
    tm.create_task('1', '2', '3')
    tm.create_task('a', 'b', 'c')
    tasks = tm.list_tasks()
    assert tasks[0]['priority'] == '3'
    assert tasks[1]['priority'] == 'c'
    with open('test_tasks.json', "w") as f:
        pass
