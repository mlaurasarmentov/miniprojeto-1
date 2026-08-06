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

    except:
        print(f" Opção inválida.")

    if comando == 1:
        catalogo.Catalogo.listar_usuarios("usuario")

    elif comando == 2:
        nome = input("Nome do usuário: ")
        id = catalogo.Catalogo.buscar_usuario_por_nome("usuario", nome)
        catalogo.Catalogo.playlist_de("usuario", id)

