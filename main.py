from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None
    
my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, {"title": "favourite foods", "content": "i like pizza", "id": 2}]
    
@app.get("/")
async def root():
    return {"message": "Welcome to my API"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.post("/posts")
async def create_post(post: Post):
    post_dict = post.model_dump()
    post_dict['id'] = randrange(0, 100000)
    my_posts.append(post_dict)
    return {"data": post_dict}

# title str, content str