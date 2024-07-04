# Solicita ao usuário que insira uma palavra e remove os espaços em branco no início e no final da string,
# além de converter todas as letras para maiúsculas.
palavra = str(input('Digite uma palavra: ')).strip().upper()

# Separa a palavra em uma lista de caracteres.
c = palavra.split()

# Junta os caracteres da lista para formar uma palavra sem espaços.
palavrajunta = ''.join(c)

# Inicializa uma string vazia para armazenar o inverso da palavra.
inverso = ''

# Itera sobre os índices da palavra na ordem reversa.
for letra in range(len(palavrajunta)-1, -1, -1):
    # Adiciona cada letra ao inverso da palavra.
    inverso += palavrajunta[letra]

# Verifica se o inverso da palavra é diferente da palavra original.
if inverso != palavrajunta:
    # Se forem diferentes, imprime que a palavra não é um palíndromo.
    print('A frase: {} não é um Palíndromo, pois '.format(palavra))
    # Imprime as versões original e invertida da palavra.
    print('{} é diferente de {}'.format(palavrajunta, inverso))
else:
    # Se forem iguais, imprime que a palavra é um palíndromo.
    print('A frase: {} é um Palíndromo, pois'.format(palavra))
    # Imprime as versões original e invertida da palavra.
    print('{} é igual a {}'.format(palavrajunta, inverso))