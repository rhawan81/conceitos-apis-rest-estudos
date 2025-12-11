from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
usuarios = []
class Usuario(BaseModel):
    nome: str
    idade: int
class Produto(BaseModel):
    name: str


@app.get('/produto/{id}')
def mostrar_prod(id:int):
    return {'mensagem ': f'o id do produto é {id}'}

@app.get('/cidade')
def mostrar_cidade(cidade:str):
    return {'Mensagem': f'Voce mora na cidade {cidade}'}
@app.get('/usuario/{id}')
def buscar_por_id(id:int):
    for users in usuarios:
        if users['id'] == id:
            return users
    return {'erro': 'Usuario nao encontrado'}
        
@app.post('/usuario')
def criar_user(dados: Usuario):
    novo_user = {'id': len(usuarios) + 1 , "nome": dados.nome, 'idade':dados.idade}
    usuarios.append(novo_user)
    return {"mensagem": "Usuário criado com sucesso!", "usuario": novo_user}
@app.get('/usuarios')
def listar_user():
    return usuarios
@app.get('/')
def linkedin():
    return {'mensagem': 'API RODANDO MUITO BOM MICHEL'}

@app.get('/hello')
def diga_ola(name:str):
    return {'mensagem': f"Ola, {name} !"}

produtos = []
@app.get('/produtos')
def mostrar_produtos():
    return produtos

@app.get('/produtos/{id}')
def buscar_id(id:int):
    for p in produtos:
        if p['id'] == id:
            return p
    
    return {'Mensagem': 'produto nao encontrado'}
        

@app.post('/produtos')
def criar_prods(prod: Produto):
    novo_produto = {'id': len(produtos) + 1 , 'name': prod.name}
    produtos.append(novo_produto)
    
    return {'mensagem ': f'o produto {novo_produto} criado com sucesso !'}

@app.delete('/produtos/{id}')
def deletar(id: int):
    for p in produtos:
        if p['id'] == id:
            produtos.remove(p)
            return {'mensagem': 'produto removido com sucesso'}
    return {'mensagem': 'Produto nao foi encontrado'}
