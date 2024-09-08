from task.models.task import Task


def test_create_task_title(session):
    new_task = Task(title="Test Task", description="Test Description")
    session.add(new_task)
    session.commit()

    task_from_db = session.query(Task).first()
    assert task_from_db.title == "Test Task"


def test_create_task_description(session):
    new_task = Task(title="Test Task", description="Test Description")
    session.add(new_task)
    session.commit()

    task_from_db = session.query(Task).first()
    assert task_from_db.description == "Test Description"


def test_task_default_completed_value(session):
    new_task = Task(title="Test Task", description="Test Description")
    session.add(new_task)
    session.commit()

    task_from_db = session.query(Task).first()
    assert task_from_db.completed is False


def test_task_completed_false(session):
    new_task = Task(title="Test Task", description="Test Description", completed=False)
    session.add(new_task)
    session.commit()

    task_from_db = session.query(Task).first()
    assert task_from_db.completed is False


def test_task_completed_true(session):
    new_task = Task(title="Test Task", description="Test Description", completed=True)
    session.add(new_task)
    session.commit()

    task_from_db = session.query(Task).first()
    assert task_from_db.completed is True
