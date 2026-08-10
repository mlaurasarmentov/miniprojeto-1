
"""Menu interativo no terminal.
 
Uso: python cli.py catalogo_final.json
"""
import sys
from collections import deque
from catalogo import Catalogo
 
cat = Catalogo(sys.argv[1])
 
historico = deque(maxlen=10)  # histórico
 
 
def descricao(conteudo_id: str) -> str:
    """Formata 'Título - Artista (tipo)' a partir de um ID de conteúdo."""
    conteudo = cat.buscar_cont_por_id(conteudo_id)
    if conteudo is None:
        return f"{conteudo_id} (não encontrado)"
    tipo = "álbum" if conteudo["tipo"] == "album" else "música"
    return f'{conteudo["titulo"]} - {conteudo["artista"]} ({tipo})'
 
 
def formatar_listar_usuarios(nomes: list[str]) -> str:
    linhas = [f"{len(nomes)} usuários (em ordem alfabética):"]
    for um, dois, tres in zip(nomes[::3], nomes[1::3], nomes[2::3]):
        linhas.append("{:<18}{:<18}{:<}".format(um, dois, tres))
    return "\n".join(linhas)
 
 
def formatar_playlist(nome: str, ids: list[str]) -> str:
    linhas = [f"Playlist de {nome} ({len(ids)} itens):"]
    for i, cid in enumerate(ids):
        linhas.append(f"{i + 1}. {descricao(cid)}")
    return "\n".join(linhas)
 
 
def formatar_intersecao(ids: list[str]) -> str:
    linhas = [f"Interseção ({len(ids)} conteúdos):"]
    for cid in ids:
        linhas.append(f"  - {descricao(cid)} ({cid})")
    return "\n".join(linhas)
 
 
def formatar_conteudos_do_genero(genero: str, ids: list[str]) -> str:
    if not ids:
        return "Nenhum conteúdo nesse gênero."
    linhas = [f'{len(ids)} conteúdos em "{genero}":']
    for cid in ids:
        linhas.append(f"  - {descricao(cid)} ({cid})")
    return "\n".join(linhas)
 
 
def formatar_fila_atual(ids: list[str]) -> str:
    if not ids:
        return "Fila vazia."
    linhas = [f"Fila atual ({len(ids)} itens, próximo primeiro):"]
    for i, cid in enumerate(ids):
        linhas.append(f"   {i + 1}. {descricao(cid)}")
    return "\n".join(linhas)
 
 
while True:
    print(f"\n Trilha Sonora \n \
————————————— \n \
0. Sair \n \
1. Listar todos os usuários \n \
2. Ver playlist completa de um usuário \n \
3. Conteúdo na posição N da playlist \n \
4. Interseção de playlists (N usuários) \n \
5. Dados de um conteúdo (rating, duração, gêneros, plataformas, data, execuções) \n \
6. Conteúdos de um gênero \n \
7. Enfileirar conteúdo na fila de reprodução \n \
8. Tocar próximo da fila \n \
9. Ver fila atual \n \
10. Ver histórico")
 
    try:
 
        comando = int(input("> "))
        if 0 > comando or comando > 10:
            raise ValueError()
        if comando == 0:
            break
 
        match comando:
            case 1:
                print(formatar_listar_usuarios(cat.listar_usuarios()))
                historico.append(1)
 
            case 2:
                nome = input("Nome do usuário: ")
                id = cat.buscar_usuario_por_nome(nome)
                print(formatar_playlist(nome, cat.playlist_de(id) or []))
                historico.append(2)
 
            case 3:
                nome = input("Nome do usuário: ")
                id = cat.buscar_usuario_por_nome(nome)
                num = cat.numero_de_itens(id)
                print(f"Playlist de {nome} tem {num} itens (posições 1 a {num}).")
                posicao = int(input("Posição: "))
                conteudo_id = cat.conteudo_na_posicao(id, posicao)
                if conteudo_id is None:
                    print(f"Posição {posicao} de {nome}: undefined")
                else:
                    print(f"Posição {posicao} de {nome}: {descricao(conteudo_id)}")
                historico.append(3)
 
            case 4:
                nomes = input("Nome dos usuários separados por vírgula (ex.: Nicholas, Uchoa): ")
                if "," not in nomes:
                    print("Informe pelo menos 2 usuários.")
                dados = nomes.split(", ")
                ids = [cat.buscar_usuario_por_nome(n) for n in dados]
                print(formatar_intersecao(cat.intersecao_playlists(ids)))
                historico.append(4)
 
            case 5:
                id = input("ID do conteúdo (ex.: t000000): ")
                conteudo = cat.buscar_cont_por_id(id)
                if conteudo is None:
                    print(f'Conteúdo "{id}" não encontrado.')
                else:
                    print(descricao(id))
                    rating = cat.rating_de(id)
                    duracao = cat.duracao_total_de(id)
                    print(f"  rating: {rating}")
                    duracao_min = int(int(duracao) / 60)
                    duracao_seg = int(duracao) % 60
                    print(f"  duração: {duracao_min}m{duracao_seg}s")
                    generos = cat.generos_de(id)
                    print(f"  gêneros: {', '.join(generos)}")
                    plataformas = cat.plataformas_de(id)
                    print(f"  plataformas: {', '.join(plataformas)}")
                    data = cat.data_adicionado_de(id)
                    print(f"  adicionado: {data}")
                    execucoes = cat.execucoes_de(id)
                    if execucoes is not None:
                        print(f"  execuções: {execucoes}")
                historico.append(5)
 
            case 6:
                genero = input("Gênero (ex.: Pop): ")
                print(formatar_conteudos_do_genero(genero, cat.conteudos_do_genero(genero)))
                historico.append(6)
 
            case 7:
                id = input("ID do conteúdo para enfileirar (ex.: t000000): ")
                if cat.enfileirar(id):
                    n = len(cat.fila)
                    sufixo = "item" if n == 1 else "itens"
                    print(f"Enfileirado: {descricao(id)} (fila com {n} {sufixo}).")
                else:
                    print(f'Conteúdo "{id}" não existe - nada foi enfileirado.')
                historico.append(7)
 
            case 8:
                proximo_id = cat.proximo()
                if proximo_id is None:
                    print("Fila vazia.")
                else:
                    resto = len(cat.fila)
                    sufixo = "item" if resto == 1 else "itens"
                    print(f"Tocando: {descricao(proximo_id)}")
                    print(f"Rest{'a' if resto == 1 else 'am'} {resto} {sufixo} na fila.")
                historico.append(8)
 
            case 9:
                print(formatar_fila_atual(cat.fila_atual()))
                historico.append(9)
 
            case 10:
                historico.append(10)
                print("Histórico de comandos:")
                for i in range(len(historico)):
                    print(f"  - {historico[i]}")
 
    except:
        print(" Opção inválida.")
 
