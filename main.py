# Importa as classes principais do FastAPI.
from fastapi import FastAPI, HTTPException

# Importa FileResponse para devolver arquivos de imagem ao navegador.
from fastapi.responses import FileResponse

# Importa o middleware responsável por permitir requisições do frontend.
from fastapi.middleware.cors import CORSMiddleware

# Importa os módulos utilizados para trabalhar com caminhos e localizar arquivos.
import os
import glob


# Cria a aplicação principal da API.
app = FastAPI()


# Configura o CORS para aceitar requisições vindas de qualquer origem.
# Isso permite que o frontend, mesmo executado noutra porta, aceda à API.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# Obtém o caminho absoluto da pasta onde este arquivo main.py está localizado.
PASTA_BASE = os.path.dirname(os.path.abspath(__file__))

# Cria o caminho absoluto para a pasta que contém as imagens das figurinhas.
PASTA_IMAGENS = os.path.join(PASTA_BASE, "figurinhas")


# Catálogo das figurinhas do álbum.
# Apenas as figurinhas que já possuem imagem na pasta figurinhas/ ficam ativas.
# As restantes permanecem comentadas até que os respetivos arquivos sejam adicionados.
figurinhas = [
    {
        "id": 1,
        "nome": "Alan Turing",
        "categoria": "IA",
        "imagem_url": "/figurinhas/1/imagem",
    },
    {
        "id": 2,
        "nome": "John McCarthy",
        "categoria": "IA",
        "imagem_url": "/figurinhas/2/imagem",
    },

    # Ainda indisponível: adicione à pasta figurinhas/ uma imagem iniciada por 03.
     {
         "id": 3,
         "nome": "Sam Altman",
         "categoria": "IA",
         "imagem_url": "/figurinhas/3/imagem",
     },

    # Ainda indisponível: adicione à pasta figurinhas/ uma imagem iniciada por 04.
     {
         "id": 4,
         "nome": "Geoffrey Hinton",
         "categoria": "IA",
         "imagem_url": "/figurinhas/4/imagem",
     },

    # Ainda indisponível: adicione à pasta figurinhas/ uma imagem iniciada por 05.
     {
         "id": 5,
         "nome": "Yann LeCun",
         "categoria": "IA",
         "imagem_url": "/figurinhas/5/imagem",
     },

    # Ainda indisponível: adicione à pasta figurinhas/ uma imagem iniciada por 06.
     {
         "id": 6,
         "nome": "Guido van Rossum",
         "categoria": "PYTHON",
         "imagem_url": "/figurinhas/6/imagem",
     },

    # Ainda indisponível: adicione à pasta figurinhas/ uma imagem iniciada por 07.
     {
         "id": 7,
         "nome": "Tim Peters",
         "categoria": "PYTHON",
         "imagem_url": "/figurinhas/7/imagem",
     },

    # Ainda indisponível: adicione à pasta figurinhas/ uma imagem iniciada por 08.
     {
         "id": 8,
         "nome": "Raymond Hettinger",
         "categoria": "PYTHON",
         "imagem_url": "/figurinhas/8/imagem",
     },

    # Ainda indisponível: adicione à pasta figurinhas/ uma imagem iniciada por 09.
     {
         "id": 9,
         "nome": "Travis Oliphant",
         "categoria": "PYTHON",
         "imagem_url": "/figurinhas/9/imagem",
     },

    # Ainda indisponível: adicione à pasta figurinhas/ uma imagem iniciada por 10.
     {
         "id": 10,
         "nome": "Wes McKinney",
         "categoria": "PYTHON",
         "imagem_url": "/figurinhas/10/imagem",
     },

    # Ainda indisponível: adicione à pasta figurinhas/ uma imagem iniciada por 11.
     {
         "id": 11,
         "nome": "Edgar F. Codd",
         "categoria": "BANCO DE DADOS",
         "imagem_url": "/figurinhas/11/imagem",
     },

    # Ainda indisponível: adicione à pasta figurinhas/ uma imagem iniciada por 12.
     {
         "id": 12,
         "nome": "Larry Ellison",
         "categoria": "BANCO DE DADOS",
         "imagem_url": "/figurinhas/12/imagem",
     },

    # Ainda indisponível: adicione à pasta figurinhas/ uma imagem iniciada por 13.
     {
         "id": 13,
         "nome": "Michael Widenius",
         "categoria": "BANCO DE DADOS",
         "imagem_url": "/figurinhas/13/imagem",
     },

    # Ainda indisponível: adicione à pasta figurinhas/ uma imagem iniciada por 14.
     {
         "id": 14,
         "nome": "Salvatore Sanfilippo",
         "categoria": "BANCO DE DADOS",
         "imagem_url": "/figurinhas/14/imagem",
     },

    # Ainda indisponível: adicione à pasta figurinhas/ uma imagem iniciada por 15.
     {
         "id": 15,
         "nome": "Eliot Horowitz",
         "categoria": "BANCO DE DADOS",
         "imagem_url": "/figurinhas/15/imagem",
     },

    # Ainda indisponível: adicione à pasta figurinhas/ uma imagem iniciada por 16.
     {
         "id": 16,
         "nome": "Linus Torvalds",
         "categoria": "SISTEMAS OPERACIONAIS",
         "imagem_url": "/figurinhas/16/imagem",
     },

    # Ainda indisponível: adicione à pasta figurinhas/ uma imagem iniciada por 17.
     {
         "id": 17,
         "nome": "Dennis Ritchie",
         "categoria": "SISTEMAS OPERACIONAIS",
         "imagem_url": "/figurinhas/17/imagem",
     },

    # Ainda indisponível: adicione à pasta figurinhas/ uma imagem iniciada por 18.
     {
         "id": 18,
         "nome": "Richard Stallman",
         "categoria": "SISTEMAS OPERACIONAIS",
         "imagem_url": "/figurinhas/18/imagem",
     },

    # Ainda indisponível: adicione à pasta figurinhas/ uma imagem iniciada por 19.
     {
         "id": 19,
         "nome": "Bill Gates",
         "categoria": "SISTEMAS OPERACIONAIS",
         "imagem_url": "/figurinhas/19/imagem",
     },

    # Ainda indisponível: adicione à pasta figurinhas/ uma imagem iniciada por 20.
     {
         "id": 20,
         "nome": "Steve Jobs",
         "categoria": "SISTEMAS OPERACIONAIS",
         "imagem_url": "/figurinhas/20/imagem",
     },

    # Ainda indisponível: adicione à pasta figurinhas/ uma imagem iniciada por 21.
    {
         "id": 21,
         "nome": "Paulo Silveira",
         "categoria": "BRASIL",
         "imagem_url": "/figurinhas/21/imagem",
     },

    # Ainda indisponível: adicione à pasta figurinhas/ uma imagem iniciada por 22.
     {
         "id": 22,
         "nome": "Guilherme Silveira",
         "categoria": "BRASIL",
         "imagem_url": "/figurinhas/22/imagem",
    },

    # Ainda indisponível: adicione à pasta figurinhas/ uma imagem iniciada por 23.
     {
         "id": 23,
         "nome": "Gustavo Guanabara",
         "categoria": "BRASIL",
         "imagem_url": "/figurinhas/23/imagem",
     },

    # Ainda indisponível: adicione à pasta figurinhas/ uma imagem iniciada por 24.
     {
         "id": 24,
         "nome": "Maurício Aniche",
         "categoria": "BRASIL",
         "imagem_url": "/figurinhas/24/imagem",
     },

    # Ainda indisponível: adicione à pasta figurinhas/ uma imagem iniciada por 25.
     {
         "id": 25,
         "nome": "Andre David",
         "categoria": "BRASIL",
         "imagem_url": "/figurinhas/25/imagem",
     },

    # Ainda indisponível: adicione à pasta figurinhas/ uma imagem iniciada por 26.
     {
         "id": 26,
         "nome": "Guilherme Lima",
         "categoria": "BRASIL",
         "imagem_url": "/figurinhas/26/imagem",
     },

    # Ainda indisponível: adicione à pasta figurinhas/ uma imagem iniciada por 27.
    {
         "id": 27,
         "nome": "Gi Space Coding",
         "categoria": "BRASIL",
         "imagem_url": "/figurinhas/27/imagem",
     },

    # Ainda indisponível: adicione à pasta figurinhas/ uma imagem iniciada por 28.
     {
        "id": 28,
        "nome": "Vinicius Neves",
         "categoria": "BRASIL",
         "imagem_url": "/figurinhas/28/imagem",
     },

     #Ainda indisponível: adicione à pasta figurinhas/ uma imagem iniciada por 29.
     {
         "id": 29,
         "nome": "Rafaela Ballerini",
         "categoria": "BRASIL",
         "imagem_url": "/figurinhas/29/imagem",
     },

     #Ainda indisponível: adicione à pasta figurinhas/ uma imagem iniciada por 30.
     {
         "id": 30,
         "nome": "Palmira",
         "categoria": "BRASIL",
         "imagem_url": "/figurinhas/30/imagem",
     },
]


# Endpoint que devolve a lista de figurinhas atualmente disponíveis.
@app.get("/figurinhas")
def listar_figurinhas():
    return figurinhas


# Endpoint que procura e devolve o arquivo de imagem correspondente ao ID informado.
@app.get("/figurinhas/{id}/imagem")
def obter_imagem_figurinha(id: int):
    # Cria o padrão de procura, usando o ID com dois dígitos.
    # Exemplo para o ID 1: 01[!0-9]*
    # O trecho [!0-9] garante que o prefixo 01 não seja confundido com 010, 011 etc.
    padrao_arquivo = os.path.join(PASTA_IMAGENS, f"{id:02d}[!0-9]*")

    # Procura na pasta todos os arquivos que correspondem ao padrão.
    arquivos_encontrados = glob.glob(padrao_arquivo)

    # Se nenhum arquivo for encontrado, devolve o erro HTTP 404.
    if not arquivos_encontrados:
        raise HTTPException(
            status_code=404,
            detail="Imagem da figurinha não encontrada.",
        )

    # Devolve o primeiro arquivo encontrado como resposta HTTP.
    return FileResponse(arquivos_encontrados[0])
