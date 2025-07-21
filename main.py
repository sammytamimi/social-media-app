<<<<<<< HEAD
from fastapi import FastAPI, Response, status
=======
from fastapi import FastAPI, Response, status, HTTPException
>>>>>>> feature/delete-posts
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

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p
<<<<<<< HEAD
=======

def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i
    return None
        
    
>>>>>>> feature/delete-posts
    
@app.get("/")
async def root():
    return {"message": "Welcome to my API"}

@app.get("/posts")
async def get_posts():
    return {"data": my_posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED) # change default status code to 201 from 200 to show post was created
async def create_post(post: Post):
    post_dict = post.model_dump()
    post_dict['id'] = randrange(0, 100000)
    my_posts.append(post_dict)
    return {"data": post_dict}

@app.get("/posts/{id}") # path parameter for post
async def get_post(id: int, response: Response):
    post = find_post(id)
    if not post:
<<<<<<< HEAD
        response.status_code = status.HTTP_404_NOT_FOUND
    return {"post detail": post}
=======
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found ")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'message' : f"post with id: {id} was not found "}
    return {"post_detail": post}

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id: int):
    index = find_index_post(id)
    if index is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} not found")
    
    my_posts.pop(index)
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)
    

>>>>>>> feature/delete-posts
    
