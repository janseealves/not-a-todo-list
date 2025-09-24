from sqlalchemy import text
from sqlalchemy.orm import Session

from core.schemas import Task, TaskCreate, TaskUpdate


class CreateTaskError(Exception):
    pass
class TaskNotFound(Exception):
    pass

class UpdateTaskError(Exception):
    pass

def create_task(task_in: TaskCreate, db: Session):
    query = text("""
        INSERT INTO task (title, description)
        VALUES (:title, :description)
        RETURNING id;
    """)

    result = db.execute(query, {
        "title": task_in.title,
        "description": task_in.description
    })

    row = result.fetchone()
    if row is None: 
        raise CreateTaskError
    id = row[0]

    db.commit()

    return Task(
        id=id,
        title=task_in.title,
        description=task_in.description
    )


def read_tasks(db: Session):
    query = text("""
        SELECT * 
        FROM tasks;
    """)

    result = db.execute(query)
    return result.fetchall()


def read_task(id: int, db: Session):
    query = text("""
        SELECT *
        FROM tasks
        WHERE id = :id;
    """)

    result = db.execute(query, {"id": id})
    return result.first()


def update_task(id: int, task_update: TaskUpdate, db: Session):
    update_data = task_update.model_dump(exclude_unset=True)

    if not update_data:
        raise UpdateTaskError

    if not read_task(id, db):
        raise TaskNotFound

    set_clauses = [f"{key} = :{key}" for key in update_data.keys()]

    set_clauses_string = ", ".join(set_clauses)

    query = text(f"""
        UPDATE tasks
        SET 
            {set_clauses_string}
        WHERE id = :id
    """)

    db.execute(query, update_data)
    db.commit()        

    return read_task(id, db)
        

def delete_task(id: int, db: Session):
    if not read_task(id, db):
        raise TaskNotFound

    # Implementar verificações...
    query = text("""    
        DELETE
        FROM tasks
        WHERE id = :id;
    """)

    db.execute(query, {"id": id})
    db.commit()
