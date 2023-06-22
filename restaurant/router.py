from fastapi import APIRouter, HTTPException
from .storage import get_students_storage, get_marks_storage
# from .schema import StudentCreateSchema, StudentUpdateSchema, Student, Mark

router = APIRouter()

