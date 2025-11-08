import requests

#url da api
url = 'https://pokeapi.co/api/v2/pokemon'

#fazendo get da api para obter os dados
response = requests.get(url)

#tratando os dados para conseguir manipula-los // virou um dicionário
data = response.json()

# aqui o data['count'] é onde está armazenado o número total de pokemons no get
numero_de_pokemons = data['count']

# crianco um dicionario vazio para armazenar os dados que queremos
pokemons_names_types = {}

# fazendo um loop para percorrer todos os pokemons e capturar os dados que queremos armazenar
for pokemon in range (1, 3 + 1):

    #segundo request para pegar os detalhes de cada pokémon, ou seja acessando a página especifica de cada pokemon
    response2 = requests.get(f'{url}/{pokemon}')
    data2 = response2.json()

    
    #Armazenando o nome do pokemon
    name = data2['name']

    #armazenando os tipos caso exista mais de 1 tipo no mesmo pokemon
    tipos = []

    # fazendo um loop para percorrer todos os tipos que aquele pokémon tenha e armazenando ele na lista tipos
    for tipo in data2['types']:
        
        tipos.append(tipo['type']['name'])
    
    # adicionando ao dicionario vazio os nomes e os tipos
    pokemons_names_types.update({name: tipos})
    #pokemons_names_types[name] = tipos

    print('print3')
    print(pokemons_names_types)



# mostrando o que foi armazenado    
print(pokemons_names_types) 