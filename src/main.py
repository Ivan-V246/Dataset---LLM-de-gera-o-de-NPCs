from groq import Groq
import json
import random

client = Groq(
    api_key = ""
)

modelo = ""
temp = 1

generos = [
"Ópera Espacial",
"Velho Oeste",
"Fantasia Medieval",
"SteamPunk",
"Distopia Futurista",
"Terror e Investigação"
]

arquetipo = [
"mentor", 
"antagonista", 
"anti-herói", 
"falso aliado", 
"figura trágica",
"aliado temporário"
]

figuras = []

with open("Origem.json", "r") as file:
    figuras = json.load(file)

dados = []

for i in figuras:
    g = random.randint(len(generos))
    a = random.randint(len(arquetipo))
    prom = f"""Gere uma ficha de NPC para RPG de mesa do gênero {generos[g]}, inspirado na figura {i["nome"]}, da mitologia {i["mitologia"]}. 
    O personagem deve ter nome e sobrenome originais, e deve ocupar o papel narrativo de {arquetipo[a]}.
    Responda exatamente no formato abaixo. Cada campo deve ter no máximo três linhas.
    Nome: 
    Descrição Física: 
    Traço de personalidade: 
    Classe Social: 
    Objetivo: 
    Medo ou Fraqueza: 
    Traço Físico Marcante: 
    Conflito Atual: 
    Principais Relações: 
    Frase atribuída:"
    """

    completion = client.chat.completions.create(
        model = modelo,
        temperature = temp,
        messages=[
            {
                "role": "user",
                "content": prom
            }
        ]
    )

    d = {
        "input" : {
            "Figura Inspiradora" : i["nome"],
            "Mitologia Origem" : i["mitologia"],
            "Modelo" : modelo,
            "Temperatura" : str(temp),
            "Gênero" : generos[g],
            "Arquétipo" : arquetipo[a]
            },
        "Prompt Gerador" : prom,
        "Personagem Gerado" : completion.choices[0].message.content
    }

    dados.append(d)

with open("Destino.json", "w") as file:
    json.dump(dados, file, ensure_ascii=False, indent=4)