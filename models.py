from typing import List
from pydantic import BaseModel, Field

class Alumno(BaseModel):
    nombre: str 
    apellidos: str 
    matricula: str 
    edad: int 
    materias: List[str]
class Config: 
    schema_extra = {
        "example": {
            "nombre": "Carlos",
            "apellidos": "Carrizosa",
            "matricula": "123456",
            "edad": 50,
            "materias": ["IA", "ML", "DM"]
        }
    }
