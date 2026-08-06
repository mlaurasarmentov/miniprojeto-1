"""A classe Catalogo. Leia o README.md antes de começar.

Esta é a peça central do projeto: carrega o JSON uma vez, constrói os
índices no __init__ e expõe os 16 métodos que o main.py e o cli.py usam.
"""
import json

with open("/home/laura/Documents/faculdade/p1/trilha/TRILHA2026/miniprojeto-1/catalogo_dev.json", "r") as file:
    database = json.load(file)

class Catalogo:
    def __init__(self, caminho_json: str): 
        caminho_json = database

    # --- usuários e playlists ---
    def listar_usuarios(self):
        num = 0
        lista = []
        for usuario in database["usuarios"]:
            num += 1
            if usuario not in lista:
                lista.append(usuario["nome"])
        lista.sort()
        print(f"{num} usuários (em ordem alfabética):")
        for um, dois, tres in zip(lista[::3], lista[1::3], lista[2::3]):
            print ('{:<18}{:<18}{:<}'.format(um, dois, tres))

    def buscar_usuario_por_nome(self, nome: str):
        for usuario in database["usuarios"]:
            if usuario["nome"] == nome:
                return usuario["id"]

    def playlist_de(self, usuario_id: str):
        lista = []
        num = 0
        for usuarios in database["usuarios"]:
            if usuarios["id"] == usuario_id:
                playlist = usuarios["playlist"]
                nome = usuarios["nome"]
        for i in playlist:
            num += 1
            for conteudos in database["conteudos"]:
                if conteudos["id"] == i:
                    if conteudos["tipo"] == "album":
                        tipo = "álbum"
                    else:
                        tipo = "música"
                    lista.append(conteudos["titulo"] + " - " + conteudos["artista"] + " (" + tipo + ") ")
        print(f"Playlist de {nome} ({num} itens):")
        for index, info in enumerate(lista):
            print(f"{index + 1}. {info}")

    def numero_de_itens(self, usuario_id: str):
        num = 0
        for usuarios in database["usuarios"]:
            if usuarios["id"] == usuario_id:
                playlist = usuarios["playlist"]
        for i in playlist:
            num += 1
        return num

    def conteudo_na_posicao(self, usuario_id: str, posicao: int):
        lista = []
        num = 0
        for usuarios in database["usuarios"]:
            if usuarios["id"] == usuario_id:
                playlist = usuarios["playlist"]
                nome = usuarios["nome"]
        for i in playlist:
            num += 1
            for conteudos in database["conteudos"]:
                if conteudos["id"] == i:
                    if conteudos["tipo"] == "album":
                        tipo = "álbum"
                    else:
                        tipo = "música"
                    lista.append(conteudos["titulo"] + " - " + conteudos["artista"] + " (" + tipo + ") ")
        try:
            return lista[posicao - 1]
        except:
            return "undefined"
        

    def intersecao_playlists(self, usuario_ids: list[str]):
        list.split()

    # --- dados de um conteúdo ---
    def rating_de(self, conteudo_id: str) -> float | None: ...
    def duracao_total_de(self, conteudo_id: str) -> int | None: ...
    def generos_de(self, conteudo_id: str) -> list[str] | None: ...
    def plataformas_de(self, conteudo_id: str) -> list[str] | None: ...
    def data_adicionado_de(self, conteudo_id: str) -> str | None: ...
    def execucoes_de(self, conteudo_id: str) -> int | None: ...
    def conteudos_do_genero(self, genero: str) -> list[str]: ...

    # --- fila de reprodução ---
    def enfileirar(self, conteudo_id: str) -> bool: ...
    def proximo(self) -> str | None: ...
    def fila_atual(self) -> list[str]: ...