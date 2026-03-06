# LLM de Geração de NPCs - Dataset

![Python](https://img.shields.io/badge/Python-3.17-green?logo=python&logoColor=white)
![Git](https://img.shields.io/badge/Git-Versionamento-yellow?logo=git&logoColor=white)
![Json](https://img.shields.io/badge/Json-Armazenamento-blue?logo=json&logoColor=white)


Repositório criado para **registrar o processo de construção** e **armazenar um dataset de treino para uma LLM** que tem como objetivo a geração de **NPCS para campanhas de RPG de mesa**.

***

## ⚙️ Criação e Origem dos dados

Os **dados sintéticos** serão gerados por LLMs disponibilizadas na internet, por meio de APIs. A fim de evitar uma homogeinização dos dados, serão utilizados modelos e temperaturas diferentes, além de alguns critérios de base para direcionar a criação, como:
 
**Figuras Inspiradoras**, reunidas de dez mitologias/culturas diferentes:

1. Grega 
2. Romana 
3. Nórdica
4. Egípcia
5. Japonesa
6. Chinesa
7. Celta
8. Suméria
9. Iorubá
10. Tupi-Guarani

**Gêneros/Contextos**:

1. Ópera Espacial
2. Velho Oeste
3. Steampunk
4. Terror e Investigação
5. Fantasia Medieval
6. Distopia Futurista

e **Arquétipos** de personagem:

1. Mentor
2. Aliado Temporário
3. Figura Trágica
4. Falso Aliado
5. Antagonista
6. Anti-Héroi

### Fontes Utilizadas
```
https://pt.wikipedia.org/wiki/Lista_de_figuras_da_mitologia_grega
https://pt.wikipedia.org/wiki/Mitologia_romana
https://pt.wikipedia.org/wiki/Mitologia_n%C3%B3rdica
https://pt.wikipedia.org/wiki/Mitologia_sum%C3%A9ria
https://pt.wikipedia.org/wiki/Mitologia_guarani
https://pt.wikipedia.org/wiki/Mitologia_japonesa
https://pt.wikipedia.org/wiki/Mitologia_chinesa
https://pt.wikipedia.org/wiki/Mitologia_celta
https://pt.wikipedia.org/wiki/Religi%C3%A3o_iorub%C3%A1
https://www.suapesquisa.com/resumos/mitologia_celta.htm
https://www.todamateria.com.br/mitologia-egipcia/
https://segredosdomundo.r7.com/mitologia-ioruba/

```
### Modelos Utilizados
```
openai/gpt-oss-120b
```

## 📚 Estrutura do Dataset

O arquivo **main.py** armazenado em */src* é o programa responsável por fazer as requisições para a API e armazenar os dados gerados. 

As **figuras inspiradoras** serão armazenadas como arquivos Json em */data/Figuras*, separadas em listas por cultura/mitologia.

Os **dados de origem humana** serão armazenados como arquivos Json em */data/Dados Naturais*.

Os **dados gerado por LLMs** serão armazenados como arquivos Json em */data/Dados Sintéticos*, sendo cada um dos NPCs um objeto com a seguinte estrutura:
```
{
    "input":{
                "Figura Inspiradora": 
                "Mitologia Origem": 
                "Modelo": 
                "Temperatura": 
                "Gênero": 
                "Arquétipo":
            }
    "Prompt Gerador":
    "Personagem Gerado":
}
```

## 🛠️ Ferramentas Utilizadas 
- **[Python]()** — principal linguagem de programação utilizada. 
- **[Git](https://git-scm.com/)** — versionamento e controle do código.  
- **[Json]()** — formato de texto utilizado para armazenar os dados. 

***
### 📝 Licença

Este repositório está sob a licença **CC By-Sa**. Sinta-se a vontade para utilizá-lo, desde que **dê os devidos créditos** e **mantenha essa mesma licença**.