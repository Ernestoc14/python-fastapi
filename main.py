from typing import Union
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

movies = [
    {
        "id": 1,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que...",
        "year": "2009",
        "rating": 7.8,
        "category": "Acción"
    },
    {
        "id": 2,
        "title": "Interestellar",
        "overview": "Space",
        "year": "2014",
        "rating": 9.3,
        "category": "Ficcion"
    },{
        "id": 3,
        "title": "Garfield",
        "overview": "Cat movie",
        "year": "2023",
        "rating": 8.2,
        "category": "Comic"
    }
]

# fastapi dev main.py
app = FastAPI()
app.title = "Mi primera API con FastAPI"

@app.get("/", tags= ["home"])

def read_root():
    return HTMLResponse("<h2>HOLA</h2>")

# Get all movies
@app.get("/movies", tags=["movies"])
def getMovies():
    return movies

# Get one movie by id DYNAMIC ROUTING
@app.get("/movies/{id}", tags=["movies"])
def getMovieById(id: int):
    return [movie for movie in movies if movie["id"] == id]

