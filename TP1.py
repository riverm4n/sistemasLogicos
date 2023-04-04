# Trabalho prático 1 de Sistemas Lógicos
# por Mário Hirotoshi Sugai Júnior, matrícula 22060031

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
    print ("Olá! :D \nSou um programa pensado para converter um dado valor de uma base numérica para outra :) \n")

    # Entradas do usuário e atribuições a variáveis
    valor_entrada = input("Qual valor você gostaria de converter? ")
    base_entrada = input("Favor, informar a base de entrada (0, caso não queira especificar): ")
    base_saida = input("Favor, informar a base de saída (0, caso não queira especificar): ")

    # Atribuindo valores de entradas ás variáveis de base, considerando os valores default caso não especificadas bases
    if(base_entrada == 0):
        base_entrada = 10

    if (base_saida == 0):
        base_saida = 10

if __name__ == "__main__":
    main()