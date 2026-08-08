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
        lista_usuarios = []
        for usuario in database["usuarios"]:
            num += 1
            if usuario not in lista_usuarios:
                lista_usuarios.append(usuario["nome"])
        lista_usuarios.sort()
        print(f"{num} usuários (em ordem alfabética):")
        for um, dois, tres in zip(lista_usuarios[::3], lista_usuarios[1::3], lista_usuarios[2::3]): # formatiza em colunas
            print ('{:<18}{:<18}{:<}'.format(um, dois, tres))

    def buscar_usuario_por_nome(self, nome: str):
        for usuario in database["usuarios"]:
            if usuario["nome"] == nome:
                return usuario["id"]

    def buscar_cont_por_id(self, id: str):
        for conteudos in database["conteudos"]:
            if conteudos["id"] == id:
                if conteudos["tipo"] == "album":
                    tipo = "álbum"
                else:
                    tipo = "música"
                return (conteudos["titulo"] + " - " + conteudos["artista"] + " (" + tipo + ") ")

    def playlist_de(self, usuario_id: str):
        playlist_usuario = []
        musicas = 0
        for usuarios in database["usuarios"]:
            if usuarios["id"] == usuario_id:
                playlist = usuarios["playlist"]
                nome = usuarios["nome"]
        for musica in playlist:
            musicas += 1
            for conteudos in database["conteudos"]:
                if conteudos["id"] == id:
                    if conteudos["tipo"] == "album":
                        tipo = "álbum"
                    else:
                        tipo = "música"
                    playlist_usuario.append(conteudos["titulo"] + " - " + conteudos["artista"] + " (" + tipo + ") ")
        print(f"Playlist de {nome} ({musicas} itens):")
        for index, info in enumerate(playlist_usuario):
            print(f"{index + 1}. {info}")

    def numero_de_itens(self, usuario_id: str):
        itens = 0
        for usuarios in database["usuarios"]:
            if usuarios["id"] == usuario_id:
                playlist = usuarios["playlist"]
        for musica in playlist:
            itens += 1
        return itens

    def conteudo_na_posicao(self, usuario_id: str, posicao: int):
        playlist_usuario = []
        for usuarios in database["usuarios"]:
            if usuarios["id"] == usuario_id:
                playlist = usuarios["playlist"]
                nome = usuarios["nome"]
        for i in playlist:
            for conteudos in database["conteudos"]:
                if conteudos["id"] == i:
                    if conteudos["tipo"] == "album":
                        tipo = "álbum"
                    else:
                        tipo = "música"
                    playlist_usuario.append(conteudos["titulo"] + " - " + conteudos["artista"] + " (" + tipo + ") ")
        try:
            return playlist_usuario[posicao - 1]
        except:
            return "undefined"
        

    def intersecao_playlists(self, usuario_ids: list[str]):
        playlist_u1 = []
        playlist_u2 = []
        musicas = 0
        for usuarios in database["usuarios"]:
            if usuarios["id"] == usuario_ids[0]:
                    playlist1 = usuarios["playlist"]
                    if usuario_ids[0] == usuario_ids[1]:
                        playlist2 = usuarios["playlist"]
            elif usuarios["id"] == usuario_ids[1] and usuario_ids[0] != usuario_ids[1]:
                playlist2 = usuarios["playlist"]
        for i in playlist2:
            for j in playlist1:
                for conteudos in database["conteudos"]:
                    if conteudos["id"] == j:
                        playlist_u2.append(conteudos["id"])
            for conteudos in database["conteudos"]:
                if conteudos["id"] == i and conteudos["id"] in playlist_u2:
                    if conteudos["tipo"] == "album":
                        tipo = "álbum"
                    else:
                        tipo = "música"
                    playlist_u1.append(conteudos["titulo"] + " - " + conteudos["artista"] + " (" + tipo + ") " + " (" + conteudos["id"] + ") ")
                    musicas += 1
        print(f"Interseção ({musicas} conteúdos):")
        for info in playlist_u1:
            print(f"  - {info}")


    # --- dados de um conteúdo ---
    def rating_de(self, conteudo_id: str):
        for conteudos in database["conteudos"]:
            if conteudos["id"] == conteudo_id:
                try:
                    rating = float(conteudos["rating"])
                except: 
                    rating = None
            else:
                rating = None
        return rating

    def duracao_total_de(self, conteudo_id: str):
        duracao = 0
        for conteudos in database["conteudos"]:
            if conteudos["id"] == conteudo_id:
                if conteudos["tipo"] == "musica":
                    duracao = conteudos["duracao_seg"] 
                else:
                    for faixas in conteudos["faixas"]:
                        if faixas["duracao_seg"] != None:
                            duracao += faixas["duracao_seg"]
        return duracao

    def generos_de(self, conteudo_id: str):
        for conteudos in database["conteudos"]:
            if conteudos["id"] == conteudo_id:
                return ", ".join(conteudos["generos"])
        return None

    def plataformas_de(self, conteudo_id: str):
        for conteudos in database["conteudos"]:
            if conteudos["id"] == conteudo_id:
                return ", ".join(conteudos["plataformas"])
        return None

    def data_adicionado_de(self, conteudo_id: str):
        partes = []
        for conteudos in database["conteudos"]:
            if conteudos["id"] == conteudo_id:
                if "/" in conteudos["data_adicionado"]:
                    partes = conteudos["data_adicionado"].split("/")
                    return "-".join(reversed(partes))
                else:
                    return "".join(conteudos["data_adicionado"])

    def execucoes_de(self, conteudo_id: str):
        for conteudos in database["conteudos"]:
            if conteudos["id"] == conteudo_id:
                return None
                
    def conteudos_do_genero(self, genero: str):
        musica_no_gen = []
        musicas = 0
        for conteudo in database["conteudos"]:
            generos_conteudo = conteudo["generos"]
            if isinstance(generos_conteudo, str):
                generos_conteudo = [generos_conteudo]
            if genero in generos_conteudo:
                if conteudo["tipo"] == "album":
                    tipo = "álbum"
                else:
                    tipo = "música"
                musica_no_gen.append(conteudo["titulo"] + " - " + conteudo["artista"] + " (" + tipo + ") (" + str(conteudo["id"]) + ")")
                musicas += 1
        if musicas == 0:
            print("Nenhum conteúdo nesse gênero.")
            return 1
        print(f'{musicas} conteúdos em "{genero}":')
        for info in musica_no_gen:
            print(f"  - {info}")

    # --- fila de reprodução ---
    def enfileirar(self, conteudo_id: str):
        for conteudos in database["conteudos"]:
            if conteudos["id"] == conteudo_id:
                return True


    def proximo(self, fila: list):
        try:
            print(f"Tocando: {fila[0]}")
            fila.popleft()
            if len(fila) == 1:
                print(f"Resta {len(fila)} item na fila.")
            else:
                print(f"Restam {len(fila)} itens na fila.")
        except:
            print("Fila vazia.")

    def fila_atual(self, fila: list):
        if not fila:
            print("Fila vazia.")
        else:
            print(f"Fila atual ({len(fila)} itens, próximo primeiro):")
            for musicas, index in enumerate(fila):
                print(f"   {index}. {musicas}")
