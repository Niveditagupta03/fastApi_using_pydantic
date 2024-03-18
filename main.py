from fastapi import FastAPI, Depends, HTTPException
from model import Todo
from utils import get_db
#from database import SessionLocal
from schemas import Todo as TodoSchema
from typing import List




app = FastAPI()

# Read operation (Get all todos)
@app.get("/", response_model=List[TodoSchema])
async def get_all_todos(db = Depends(get_db)):
    return db.query(Todo).all()

# Create operation
@app.post("/create", response_model=TodoSchema)
async def create_todo(text: str, is_complete: bool = False, db = Depends(get_db)):
    todo = Todo(text=text, is_done=is_complete)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo

# Update operation
@app.put("/update/{id}", response_model=TodoSchema)
async def update_todo(id: int, new_text: str = "", is_complete: bool = False, db = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    if new_text:
        todo.text = new_text
    todo.is_done = is_complete
    db.commit()
    db.refresh(todo)
    return todo


# # Delete operation
@app.delete("/delete/{id}", response_model=TodoSchema)
async def delete_todo(id: int, db = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(todo)
    db.commit()
    return todo
