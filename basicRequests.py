from fastapi import FastAPI
import requests

# url da api
url = 'https://pokeapi.co/api/v2/pokemon'

# fazendo get da api para obter os dados
response = requests.get(url)

# tratando os dados para conseguir manipula-los // virou um dicionário
data = response.json()

# aqui o data['count'] é onde está armazenado o número total de pokemons no get
numero_de_pokemons = data['count']

# criando um dicionario vazio para armazenar os dados que queremos
pokemons_names_types = {}
# criando um dicionario vazio para armazenar os pokemons pelos tipos, filtrando apenas os pokemons do tipo especifico passado como parametro no get
pokemons_by_types = {}

# fazendo um loop para percorrer todos os pokemons e capturar os dados que queremos armazenar
for pokemon in range(1, 30 + 1):

    # segundo request para pegar os detalhes de cada pokémon, ou seja acessando a página especifica de cada pokemon
    response2 = requests.get(f'{url}/{pokemon}')
    data2 = response2.json()

    # Armazenando o nome do pokemon
    name = data2['name']

    # armazenando os tipos caso exista mais de 1 tipo no mesmo pokemon
    tipos = []

    # fazendo um loop para percorrer todos os tipos que aquele pokémon tenha e armazenando ele na lista tipos
    for tipo in data2['types']:

        tipos.append(tipo['type']['name'])

    # adicionando ao dicionario vazio os nomes e os tipos
    pokemons_names_types.update({name: tipos})

    


# mostrando o que foi armazenado
print(pokemons_names_types)



# Adicionando condição para adicionar apenas pokemons que forem do tiplo planta no novo dicionário
for poke_name in pokemons_names_types:
    #para cada tipo dentro da lista que vem cada vez que eu chamo o nome do pokemon
    for type in pokemons_names_types[poke_name]:
        # se o tipo não estiver no novo dicionário pokemons_by_types, crie essa nova chave
        if type not in pokemons_by_types:
            pokemons_by_types.update({type:[poke_name]})
        else:
            pokemons_by_types[type].append(poke_name)


app = FastAPI(
    title="APIkemon"
)


# retornando na web o json de todos os pokemons que foram tratados somente nome e tipos (ex: {bulbasauro: [grass, poison], charmander: [fire])
@app.get("/pokemon-types")
def pokemon_types():
    return pokemons_names_types


# rota para pesquisar todos os pokemons do tipo que foi passado no parametro (ex: só pokemons de fogo)
@app.get("/pokemon-types/{tipo}")
def pokemon_types_specific(tipo: str):
    return {tipo:pokemons_by_types[tipo]}
