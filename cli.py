"""Menu interativo no terminal.

Uso: python cli.py catalogo_final.json
"""
import catalogo
from collections import deque

""" Início do menu (opções e validação) """

fila = [] # para não reiniciar a fila toda vez!
historico = deque(maxlen=10) # histórico

while(True):
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

#    try: 

    comando = int(input("> "))
    if 0 > comando or comando > 10:
        raise ValueError()
    if comando == 0:
        break

    match comando: 
        case 1:
            catalogo.Catalogo.listar_usuarios("usuario")
            historico.append(1)

        case 2:
            nome = input("Nome do usuário: ")
            id = catalogo.Catalogo.buscar_usuario_por_nome("usuario", nome)
            catalogo.Catalogo.playlist_de("usuario", id)
            historico.append(2)

        case 3:
            nome = input("Nome do usuário: ")
            id = catalogo.Catalogo.buscar_usuario_por_nome("usuario", nome)
            num = catalogo.Catalogo.numero_de_itens("usuario", id)
            print(f"Playlist de {nome} tem {num} itens (posições 1 a {num}).")
            posicao = int(input("Posição: "))
            conteudo = catalogo.Catalogo.conteudo_na_posicao("usuario", id, posicao)
            print(f"Posição {posicao} de {nome}: {conteudo}")
            historico.append(3)

        case 4:
            id1 = []
            id2 = []
            nomes = input("Nome dos usuários separados por vírgula (ex.: Nicholas, Uchoa): ")
            if "," not in nomes:
                print("Informe pelo menos 2 usuários.")
            dados = nomes.split(", ")
            id1.append(catalogo.Catalogo.buscar_usuario_por_nome("usuario", dados[0]))
            id2.append(catalogo.Catalogo.buscar_usuario_por_nome("usuario", dados[1]))
            id1.extend(id2)
            catalogo.Catalogo.intersecao_playlists("usuario", id1)
            historico.append(4)
        
        case 5:
            id = input("ID do conteúdo (ex.: t000000): ")
            nome = catalogo.Catalogo.buscar_cont_por_id("conteudo", id)
            print(nome)
            rating = catalogo.Catalogo.rating_de("conteudo", id)
            duracao = catalogo.Catalogo.duracao_total_de("conteudo", id)
            print(f"  rating: {rating}")
            duracao_min = int(int(duracao) / 60)
            duracao_seg = int(duracao) % 60
            print(f"  duração: {duracao_min}m{duracao_seg}s")
            generos = catalogo.Catalogo.generos_de("conteudo", id)
            print(f"  gêneros: {generos}")
            plataformas = catalogo.Catalogo.plataformas_de("conteudo", id)
            print(f"  plataformas: {plataformas}")
            data = catalogo.Catalogo.data_adicionado_de("conteudo", id)
            print(f"  adicionado: {data}")
            execucoes = catalogo.Catalogo.duracao_total_de("conteudo", id)
            if execucoes != None:
                print(f"  execuções: {execucoes}")
            historico.append(5)

        case 6:
            generos = input("Gênero (ex.: Pop): ")
            conteudos = catalogo.Catalogo.conteudos_do_genero("conteudo", generos)
            historico.append(6)
        
        case 7:
            id = input("ID do conteúdo para enfileirar (ex.: t000000): ")
            if catalogo.Catalogo.enfileirar("conteudo", id) == True:
                fila.append(catalogo.Catalogo.buscar_cont_por_id("conteudo", id))
                if len(fila) == 1:
                    print(f"Enfileirado: {"".join(fila)}(fila com {len(fila)} item).")
                else:
                    print(f"Enfileirado: {"".join(fila)}(fila com {len(fila)} itens).")
            else:
                print(f'Conteúdo "{id} não existe - nada foi enfileirado.')
            historico.append(7)

        case 8:
            catalogo.Catalogo.proximo("conteudo", fila)
            historico.append(8)
            
        case 9:
            catalogo.Catalogo.fila_atual("conteudo", fila)
            historico.append(9)

        case 10: 
            historico.append(10)
            print("Histórico de comandos:")
            for i in range(len(historico)):
                print(f"  - {historico[i]}")
            

#    except:
#        print(f" Opção inválida.")


