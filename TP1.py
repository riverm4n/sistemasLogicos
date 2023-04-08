# Trabalho prático 1 de Sistemas Lógicos, na Universidade Federal do Amazonas, no período 2022/2, ano 2023.
# por Mário Hirotoshi Sugai Júnior, matrícula 22060031
import math

# Elabore uma função em C ou em Python para fazer conversão de bases com as seguinte especificações:
# Argumento de entrada: quantidade a ser convertida, base de origem, base de destino.
# Argumento de saída: valor na base de destino, equivalente em base 10.
# Comportamento:
# - Deve adicionar posições sempre que necessário (ou seja, não tem overflow). Dica: use a fórmula apresentada na
# apostila para identificar o número de posições necessários caso a base de saída seja menor que a de entrada.
# - Se não for informada base de entrada ou de saída, assumir base 10 (valor default).
# - Se a base de saída for 10, só apresentar um argumento de saída.
# - A função deve imprimir o resultado na tela e retornar os valores de saída em uma variável. O formato de impressão é
# livre, contudo deve ser conciso.
# - (opcional) Acelerar a conversão caso as bases de entrada e saída tenham uma relação logarítmica perfeita. Por
# exemplo, Hexa para Binário, Octal para Binário, Hexa para Octal.
# A correção considerará três aspectos, com igual peso:
# 1. Funcionamento segundo o comportamento pedido;
# 2. Organização do código seguindo as boas práticas de construção de algoritmos;
# 3. A qualidade dos comentários de forma que seja possível entender cada porção do código.

def main():
    print("Olá! :D \nSou um programa pensado para converter um dado valor de uma base numérica para outra :) \n")

    # Entradas do usuário e atribuições a variáveis
    valor_entrada = input("Qual valor você gostaria de converter? ")
    base_entrada = input("Favor, informar a base de entrada (0, caso não queira especificar): ")
    base_saida = input("Favor, informar a base de saída (0, caso não queira especificar): ")

    converter(valor_entrada, base_entrada, base_saida)

def converter(valor_entrada, base_entrada, base_saida):
    # Atribuindo valores de entradas ás variáveis de base, considerando os valores default caso não especificadas bases
    # (inserir 0)
    if base_entrada == "0":
        base_entrada = "10"

    if base_saida == "0":
        base_saida = "10"

    if int(base_entrada) > 35 | int(base_saida) > 35:
        print("Infelizmente, este programa está limitado apenas a fazer conversões de valores em bases abaixo de 36")
    elif valor_entrada == "#testes":
        bateria_de_testes()
    else:
        # Parte das conversões propriamente ditas.
        if base_saida == "10":
            # print("DEBUG: chamando função para converter um valor para decimal")
            resultado = converter_valor_para_decimal(valor_entrada, base_entrada)
            print(
                "O valor " + valor_entrada + " em base " + base_entrada + " é equivalente a " + str(resultado) + " na base " +
                base_saida)
        elif base_entrada == "10":
            # print("base de saída igual a 10")
            resultado = converter_valor_decimal_para_base_n(int(valor_entrada), int(base_saida))
            print(
                "O valor " + valor_entrada + " em base " + base_entrada + " é equivalente a " + resultado + " na base " +
                base_saida)
        elif base_entrada > base_saida:
            # print("Base de entrada maior que a base de saída!")
            valor_convertido_em_decimal = converter_valor_para_decimal(valor_entrada, base_entrada)
            resultado = converter_valor_decimal_para_base_n(int(valor_convertido_em_decimal), int(base_saida))

            print(
                "O valor " + valor_entrada + " em base " + base_entrada + " é equivalente a " + resultado + " na base " +
                base_saida)
        elif base_saida > base_entrada:
            # print("Base de saída maior que a base de entrada!")
            valor_convertido_em_decimal = converter_valor_para_decimal(valor_entrada, base_entrada)
            resultado = converter_valor_decimal_para_base_n(int(valor_convertido_em_decimal), int(base_saida))

            print(
                "O valor " + valor_entrada + " em base " + base_entrada + " é equivalente a " + resultado + " na base " +
                base_saida)
        elif base_entrada == base_saida:
            # Esse cenário é só por garantia
            print("Aí é fácil. Base de entrada IGUAL a base de saída. O número é " + valor_entrada + ".")

# A primeira função que pensei em uma forma de implementar foi de converter de uma base qualquer para a base 10, cuja
# já está bem fixa em minha cabeça
def converter_valor_para_decimal(valor, base):
    # Minha ideia inicial está em converter o número cheio para algo iteravel de símbolos (os números individuais),
    # visto que o valor do algarismo e a posição do mesmo no valor cheio são importantes para a conversão.

    saida = 0

    entrada_como_string = str(valor)
    tamanho_entrada = len(entrada_como_string)
    expoente_posicao = 0  # Variável que será incrementada durante o cálculo do expoente da posição, visto que a variável
    # que percorre o vetor é decrescida ao longo do laço

    while tamanho_entrada > 0:
        # debug: print(entrada_como_string[tamanho_entrada - 1])

        # [v = Sx(Bˆp)] <--- o valor em base decimal é dado pela multiplicação do símbolo pela base elevada a posição!
        base_elevada_posicao = pow(int(base), expoente_posicao)

        valor_como_numero = retorna_valor_referencia_bases_acima_de_dez(entrada_como_string[tamanho_entrada - 1])
        saida += int(valor_como_numero) * base_elevada_posicao
        tamanho_entrada -= 1
        expoente_posicao += 1

    return saida

def converter_valor_decimal_para_base_n(valor, base):
    # Aqui acredito que não há muito para onde ir, utilizarei a fórmula de múltiplas divisões pela base de saída
    saida = ""

    entrada_como_string = str(valor)
    tamanho_entrada = len(entrada_como_string)

    resto = 0
    resultado = valor

    # O cálculo abaixo é realizado para saber a quantidade de vezes que passaremos no laço, como explicado em sala na
    # primeira aula (A vantagem computacional de utilizar um for ao invés de um while :))
    numero_digitos = int(math.log(valor, base)) + 1
    # print("número de dígitos para representar " + str(valor) + " na base " + str(base) + ": " + str(numero_digitos))

    # Laço responsável por fazer as conversões de fato
    for i in range(numero_digitos):
        # print(str(resultado) + " dividido pela base " + str(base))
        resto = resultado % base
        resultado = resultado // base # usando o operador que pega a parte inteira da divisão
        # print(str(resultado) + " com resto " + str(resto))

        # Se o valor da base é maior que 10, podemos ter casos em que o resto é maior ou igual a 10, sendo igual a um
        # símbolo
        if(resto >= 10):
            resto = retorna_letra_referencia_bases_acima_de_dez(str(resto))

        saida = str(resto) + saida

    return saida

def retorna_valor_referencia_bases_acima_de_dez(valor):
    dicionario_tabela_char = {
        "A": "10",
        "B": "11",
        "C": "12",
        "D": "13",
        "E": "14",
        "F": "15",
        "G": "16",
        "H": "17",
        "I": "18",
        "J": "19",
        "K": "20",
        "L": "21",
        "M": "22",
        "N": "23",
        "O": "24",
        "P": "25",
        "Q": "26",
        "R": "27",
        "S": "28",
        "T": "29",
        "U": "30",
        "V": "31",
        "X": "32",
        "Y": "33",
        "Z": "34",
    }

    # Ideia meio cara computacionalmente: Ele vai entrar na função todas as vezes pra checar se aquele valor existe no
    # dicionário, caso não exista, ele vai retornar o próprio valor...
    return dicionario_tabela_char.get(valor, valor)

def retorna_letra_referencia_bases_acima_de_dez(valor):
    # Essa função talvez seja meio desnecessária, mas achei que deixaria o código mais enxuto se a definisse aqui, e não
    # utilizasse os outros artifícios de buscar uma chave a partir de um valor em um dicionário, coisa que python não
    # permite fazer com a mesma praticidade que Java em Maps, ironicamente.

    dicionario_tabela_char = {
        "10": "A",
        "11": "B",
        "12": "C",
        "13": "D",
        "14": "E",
        "15": "F",
        "16": "G",
        "17": "H",
        "18": "I",
        "19": "J",
        "20": "K",
        "21": "L",
        "22": "M",
        "23": "N",
        "24": "O",
        "25": "P",
        "26": "Q",
        "27": "R",
        "28": "S",
        "29": "T",
        "30": "U",
        "31": "V",
        "32": "X",
        "33": "Y",
        "34": "Z",
    }

    return dicionario_tabela_char.get(valor)

# Definição dos testes: uma série de execuções baseadas nos exercícios da apostila, em sala + outros aleatórios
# para entrar no modo de testes, basta escrever "#testes" quando solicidado o valor de entrada
def bateria_de_testes():
    print("\nModo de Testes! \n")
    converter("2", "10", "2") # 10
    converter("11", "2", "10") # 3
    converter("63", "10", "2") # 111111
    converter("1011110000", "2", "10") # 752
    converter("111", "2", "10")  # 7
    converter("C9", "2", "10")  # 11001001
    converter("101101", "2", "10")  # 45
    converter("1010111", "2", "10")  # 87
    converter("1111111", "2", "10") # 255
    converter("111000111", "2", "10") #455
    converter("1000110001", "2", "10")

    converter("27", "10", "2")
    converter("31", "10", "2")
    converter("32", "10", "2")
    converter("33", "10", "2")
    converter("198", "10", "2")

    converter("101101", "2", "16")
    converter("1010111", "2", "16")
    converter("1111111", "2", "16")
    converter("111000111", "2", "16")
    converter("1000110001", "2", "16")

    converter("AB9", "16", "2")
    converter("1F3", "16", "2")
    converter("401", "16", "2")
    converter("B0CA", "16", "2")
    converter("CED0", "16", "2")

    converter("27", "10", "16")
    converter("31", "10", "16")
    converter("32", "10", "16")
    converter("33", "10", "16")
    converter("198", "10", "16")

    converter("AB9", "16", "10")
    converter("1F3", "16", "10")
    converter("401", "16", "10")
    converter("B0CA", "16", "10")
    converter("CED0", "16", "10")

if __name__ == "__main__":
    main()