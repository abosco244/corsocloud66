from fastapi import FastAPI
from Actor import Actor
from pydantic import BaseModel

class ActorModel(BaseModel):
    first_name: str
    last_name: str

app = FastAPI()

@app.get("/actors")
async def get_all_actors():
    return Actor.getAllActors()

@app.post("/movies/{actor_name}")
async def get_movies_by_actor(actormodel: ActorModel):
    return Actor.getMoviesByActor(actormodel.first_name, actormodel.last_name)