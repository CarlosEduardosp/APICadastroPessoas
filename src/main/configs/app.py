from fastapi import FastAPI
from .rotas.rotas_pessoa import delete_pessoa, inserir_pessoa, select_by_id, select_todos, update_pessoa, aniversariantes, homens, mulheres, faixa_etaria
from .rotas.rotas_imagem import inserir_imagem, select_imagem_id, delete_imagem
from .rotas.rota_inicial import inicio
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(select_todos.router, tags=["Selecionar todas as pessoas cadastradas no banco de dados."])
app.include_router(inserir_pessoa.router, tags=["Inserir uma nova pessoa no banco de dados."])
app.include_router(delete_pessoa.router, tags=["Deleta uma pessoa com id específico no banco de dados."])
app.include_router(update_pessoa.router, tags=["Realizar o Update no banco através do Id da pessoa."])
app.include_router(select_by_id.router, tags=["Selecionar uma pessoa do banco com id específico."])
app.include_router(inserir_imagem.router, tags=["Inserir imagens no banco de dados."])
app.include_router(select_imagem_id.router, tags=["Seleciona imagens no banco de dados pelo id."])
app.include_router(delete_imagem.router, tags=["Deleta imagens no banco de dados pelo id."])
app.include_router(inicio.router, tags=["Mensagem Inicial da api."])
app.include_router(aniversariantes.router, tags=["Seleciona todas as pessoas que fazem aniversario no mes "
                                                 "especificado no banco de dados."])
app.include_router(homens.router, tags=["Seleciona todos os homens no banco de dados."])
app.include_router(mulheres.router, tags=["Seleciona todas as mulheres no banco de dados."])
app.include_router(faixa_etaria.router, tags=["Seleciona pessoas em uma faixa de idades."])


# Lista de origens permitidas
allowed_origins = [
    "http://www.icnvararuama.com.br",
    "https://www.icnvararuama.com.br",
    "http://170.231.112.194",
    "http://icnvararuama.netlify.app",
    "https://icnvararuama.netlify.app",
    "http://2600:1f1e:c3c:f302::c8",
    "http://2600:1f1e:c3c:f301::c8",
    "http://52.67.97.86",
    "http://177.71.195.255",
    "http://170.231.112.205"
]

# Configurar CORS (Cross-Origin Resource Sharing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],  # Substitua pelo domínio do seu aplicativo, * para todos os dominios
    allow_credentials=True,
    allow_methods=["GET", "POST", "DELETE", "PUT"],  # Você pode especificar métodos permitidos, como ["GET", "POST"]
    allow_headers=["Authorization"],  # Você pode especificar cabeçalhos permitidos, como ["Authorization"]
)



