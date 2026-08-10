
"""A classe Catalogo. Leia o README.md antes de começar.
 
Esta é a peça central do projeto: carrega o JSON uma vez, constrói os
índices no __init__ e expõe os 16 métodos que o main.py e o cli.py usam.
"""
import json
 
 
class Catalogo:
    def __init__(self, caminho_json: str):
        with open(caminho_json, "r", encoding="utf-8") as file:
            self.database = json.load(file)
        self.fila = []
 
    # --- usuários e playlists ---
 
    def listar_usuarios(self) -> list[str]:
        nomes = sorted({usuario["nome"] for usuario in self.database["usuarios"]})
        return nomes
 
    def buscar_usuario_por_nome(self, nome: str):
        for usuario in self.database["usuarios"]:
            if usuario["nome"] == nome:
                return usuario["id"]
        return None
 
    def buscar_cont_por_id(self, id: str):
        for conteudo in self.database["conteudos"]:
            if conteudo["id"] == id:
                return conteudo
        return None
 
    def playlist_de(self, usuario_id: str):
        for usuario in self.database["usuarios"]:
            if usuario["id"] == usuario_id:
                return usuario["playlist"]
        return None
 
    def numero_de_itens(self, usuario_id: str) -> int:
        for usuario in self.database["usuarios"]:
            if usuario["id"] == usuario_id:
                return len(usuario["playlist"])
        return 0
 
    def conteudo_na_posicao(self, usuario_id: str, posicao: int):
        for usuario in self.database["usuarios"]:
            if usuario["id"] == usuario_id:
                playlist = usuario["playlist"]
                try:
                    return playlist[posicao - 1]
                except IndexError:
                    return None
        return None
 
    def intersecao_playlists(self, usuario_ids: list[str]):
        playlists = []
        for uid in usuario_ids:
            for usuario in self.database["usuarios"]:
                if usuario["id"] == uid:
                    playlists.append(usuario["playlist"])
                    break
            else:
                playlists.append([])  
 
        if not playlists:
            return []
 
        comuns = set(playlists[0])
        for p in playlists[1:]:
            comuns &= set(p)
 
        return [cid for cid in playlists[0] if cid in comuns]
 
    # --- dados de um conteúdo ---
 
    def rating_de(self, conteudo_id: str):
        for conteudo in self.database["conteudos"]:
            if conteudo["id"] == conteudo_id:
                try:
                    return float(conteudo["rating"])
                except (KeyError, TypeError, ValueError):
                    return None
        return None
 
    def duracao_total_de(self, conteudo_id: str):
        for conteudo in self.database["conteudos"]:
            if conteudo["id"] == conteudo_id:
                if conteudo["tipo"] == "musica":
                    return conteudo["duracao_seg"]
                duracao = 0
                for faixa in conteudo.get("faixas", []):
                    if faixa.get("duracao_seg") is not None:
                        duracao += faixa["duracao_seg"]
                return duracao
        return None
 
    def generos_de(self, conteudo_id: str):
        for conteudo in self.database["conteudos"]:
            if conteudo["id"] == conteudo_id:
                generos = conteudo["generos"]
                if isinstance(generos, str):
                    return [generos]
                return generos
        return None
 
    def plataformas_de(self, conteudo_id: str):
        for conteudo in self.database["conteudos"]:
            if conteudo["id"] == conteudo_id:
                plataformas = conteudo["plataformas"]
                if isinstance(plataformas, str):
                    return [plataformas]
                return plataformas
        return None
 
    def data_adicionado_de(self, conteudo_id: str):
        for conteudo in self.database["conteudos"]:
            if conteudo["id"] == conteudo_id:
                data = conteudo["data_adicionado"]
                if "/" in data:
                    partes = data.split("/")
                    return "-".join(reversed(partes))
                return data
        return None
 
    def execucoes_de(self, conteudo_id: str):
        for conteudo in self.database["conteudos"]:
            if conteudo["id"] == conteudo_id:
                if conteudo["tipo"] == "musica":
                    return conteudo.get("engajamento", {}).get("execucoes")
                return None
        return None
 
    def conteudos_do_genero(self, genero: str):
        encontrados = []
        for conteudo in self.database["conteudos"]:
            generos_conteudo = conteudo["generos"]
            if isinstance(generos_conteudo, str):
                generos_conteudo = [generos_conteudo]
            if genero in generos_conteudo:
                encontrados.append(conteudo["id"])
        return encontrados
 
    # --- fila de reprodução ---
 
    def enfileirar(self, conteudo_id: str) -> bool:
        existe = any(c["id"] == conteudo_id for c in self.database["conteudos"])
        if existe:
            self.fila.append(conteudo_id)
        return existe
 
    def proximo(self):
        if not self.fila:
            return None
        return self.fila.pop(0)
 
    def fila_atual(self):
        return list(self.fila)
