"""Menu interativo no terminal.

Uso: python cli.py catalogo_final.json
"""
import catalogo

""" Início do menu (opções e validação) """
while(True):
    print(f"\n Trilha Sonora \n \
————————————— \n \
1. Listar todos os usuários \n \
2. Ver playlist completa de um usuário \n \
3. Conteúdo na posição N da playlist \n \
4. Interseção de playlists (N usuários) \n \
5. Dados de um conteúdo (rating, duração, gêneros, plataformas, data, execuções) \n \
6. Conteúdos de um gênero \n \
7. Enfileirar conteúdo na fila de reprodução \n \
8. Tocar próximo da fila \n \
9. Ver fila atual")

    try: 
        comando = int(input("> "))
        if 0 > comando or comando > 10:
            raise ValueError()
        if comando == 0:
            break

        match comando: 
            case 1:
                catalogo.Catalogo.listar_usuarios("usuario")

            case 2:
                nome = input("Nome do usuário: ")
                id = catalogo.Catalogo.buscar_usuario_por_nome("usuario", nome)
                catalogo.Catalogo.playlist_de("usuario", id)

            case 3:
                nome = input("Nome do usuário: ")
                id = catalogo.Catalogo.buscar_usuario_por_nome("usuario", nome)
                num = catalogo.Catalogo.numero_de_itens("usuario", id)
                print(f"Playlist de {nome} tem {num} itens (posições 1 a {num}).")
                posicao = int(input("Posição: "))
                conteudo = catalogo.Catalogo.conteudo_na_posicao("usuario", id, posicao)
                print(f"Posição {posicao} de {nome}: {conteudo}")

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
                print(f"  gêneros: {genero}")

            case 6:
                generos = input("Gênero (ex.: Pop): ")
                conteudos = catalogo.Catalogo.conteudos_do_genero("conteudo", generos)
        
    except:
        print(f" Opção inválida.")


