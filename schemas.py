from pydantic import BaseModel

class Todo(BaseModel):
    is_done: bool
    id: int
    text: str

# Use Todo directly instead of importing it from schemas
TodoSchema = Todo
