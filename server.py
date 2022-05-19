from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()
animalList = []

class Animal(BaseModel):
    ids: None = None
    nome: str
    idade: int
    sexo: str
    cor: str

@app.get('/')
async def home():
    return {
        'msg':'Hello, world!'
    }

@app.post('/animais')
async def animais(item: Animal):
    try:
        item.ids = random.randint(0, 100)
        animalList.append(item.dict())
        return {'msg':"Sucesso ao cadastrar!"}
    except:
        return {'msg':'Algum erro ocorreu.'}

@app.get('/animais')
async def animais():
    return animalList


@app.get('/animais/{animal_id}')
async def find_animal_by_id(animal_id: int):
    for i in range(0, len(animalList)):
        if animalList[i]['ids'] == animal_id:
            return animalList[i]
        else:
            return {'msg':'Animal não localizado.'}

@app.delete('/animais/{animal_id}')
async def find_animal_by_id(animal_id: int):
    for i in range(0, len(animalList)):
        if animalList[i]['ids'] == animal_id:
            animalList.pop(i)
            return {'msg':'Sucesso ao deletar!'}
        else:
            return {'msg':'Animal não localizado.'}
    
    