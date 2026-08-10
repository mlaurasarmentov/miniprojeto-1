
"""Modo batch: lê consultas.json, responde em ordem, grava respostas.json.
 
Uso: python main.py consultas.json respostas.json
"""
import sys
import json
 
from catalogo import Catalogo
 
CAMINHO_CATALOGO = "catalogo_final.json"
 
def executar_operacao(cat: Catalogo, tipo: str, parametros: dict):
    metodo = getattr(cat, tipo, None)
    return metodo(**parametros)
 
def main():
    caminho_consultas = sys.argv[1]
    caminho_respostas = sys.argv[2]
 
    with open(caminho_consultas, "r", encoding="utf-8") as file:
        dados = json.load(file)
    consultas = dados["consultas"]
 
    cat = Catalogo(CAMINHO_CATALOGO)
 
    respostas = {}
    for consulta in consultas:
        tipo = consulta.get("tipo")
        parametros = consulta.get("parametros", {})
        resposta = executar_operacao(cat, tipo, parametros)
        respostas[str(consulta.get("id"))] = resposta
 
    with open(caminho_respostas, "w", encoding="utf-8") as file:
        json.dump(respostas, file, ensure_ascii=False, indent=2)
 
if __name__ == "__main__":
    main()
 
