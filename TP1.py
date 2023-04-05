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
# livre, contudo deve ser conciso. O retorno deve ser em um vetor com duas posições (caso base de saída seja diferente
# de 10) ou uma posição (caso o contrário). O valor da base de saída deve ser a primeira posição do vetor.
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

    # Atribuindo valores de entradas ás variáveis de base, considerando os valores default caso não especificadas bases
    if base_entrada == "0":
        print("DEBUG: atribuições de valores default rolando")
        base_entrada = "10"

    if base_saida == "0":
        print("DEBUG: atribuições de valores default rolando")
        base_saida = "10"

    if base_saida == "10":
        print("DEBUG: chamando função para converter um valor para decimal")
        converter_valor_para_decimal(valor_entrada, base_entrada)
    elif base_entrada == "10":
        print("base de saída igual a 10")
        converter_valor_decimal_para_base_n(int(valor_entrada), int(base_saida))


# A primeira função que pensei em uma forma de implementar foi de converter de uma base qualquer para a base 10, cuja
# já está bem fixa em minha cabeça
def converter_valor_para_decimal(valor, base):
    # Minha ideia inicial está em converter o número cheio para um algo iteravel de símbolos (os números individuais),
    # visto que o valor do algarismo e a posição do mesmo no valor cheio são importantes para a conversão.

    saida = 0

    entrada_como_string = str(valor)
    tamanho_entrada = len(entrada_como_string)
    expoente_posicao = 0  # Variável que será incrementada durante o cálculo do expoente da posição, visto que a variável
    # que percorre o vetor é descrescida ao longo do laço

    while tamanho_entrada > 0:
        # [v = Sx(Bˆp)] <--- o valor em base decimal é dado pela multiplicação do símbolo pela base elevada a posição!
        base_elevada_posicao = pow(int(base), expoente_posicao)

        # verificação sobre a validade daquele símbolo dentro do numero solicitado (por exemplo, se o usuário inserir 3
        # quando a base de entrada for 2, ou inserir 9 caso a base de entrada seja octal etc
        if entrada_como_string[tamanho_entrada - 1] >= base:
            print("Hm.... parece que você utilizou um número dentro do valor na base de entrada, viu... Tchau")
            return "Finalizado sem sucesso"
        else:
            saida += int(entrada_como_string[tamanho_entrada - 1]) * base_elevada_posicao
            tamanho_entrada -= 1
            expoente_posicao += 1

    print("O valor '" + valor + "', inicialmente em base " + str(base) + " em base 10 é: " + str(saida))
    return saida


def converter_valor_decimal_para_base_n(valor, base):
    # Aqui acredito que não há muito para onde ir, utilizarei a fórmula de múltiplas divisões pela base de saída, vamos
    # aonde vou

    print("DEBUG: entrei na função")
    saida = ""

    entrada_como_string = str(valor)
    tamanho_da_entrada = len(entrada_como_string)

    resto = 0
    resultado = valor

    numero_digitos = int(math.log(valor, base)) + 1
    print("número de dígitos para representar " + str(valor) + " na base " + str(base) + ": " + str(numero_digitos))

    for i in range(numero_digitos):
        print("DEBUG: entrei no loop")
        print(str(resultado) + " dividido pela base " + str(base))
        resto = resultado % base
        resultado = resultado // base # usando o operador que pega a parte inteira da divisão
        print(str(resultado) + " com resto " + str(resto))

        saida = str(resto) + saida

    # a string de saída, visto que
    print(saida)
    return saida

if __name__ == "__main__":
    main()
