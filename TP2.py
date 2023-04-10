# Trabalho prático 2 de Sistemas Lógicos, na Universidade Federal do Amazonas, no período 2022/2, ano 2023.
# por Mário Hirotoshi Sugai Júnior, matrícula 22060031
import time
import math
import random
from itertools import cycle

# De uma forma geral, o jogo produz um valor aleatório inicial que é apresentado ao jogador. O jogador tem que girar a
# roda (produzir um outro valor aleatório e somar ao anterior). Caso não goste do resultado, ele tem mais 3 tentativas
# para mudar. A primeira é sempre obrigatória. Ele não pode ficar com o valor inicial, mesmo que seja o maior valor.

def main():
    imprimir_roda_da_fortuna_ascii_art()
    lista = ['0', '1', '2', '3', '4', '5', '6', '7', '-8', '-7', '-6', '-5', '-4', '-3', '-2', '-1']

    # essa função irá ser responsável por transformar nossa lista em sua representação binaria, bem como utilizando
    # complemento de 2
    lista_bin = converter_lista(lista)

    # Transformando a lista dos binários em uma lista circular, forma que pensei que seria interessante para a represen-
    # tação em anel de nossos valores.
    lista_bin_circular = cycle(lista_bin)

    sua_sorte = random.randint(-8, 7)

    print("Vamos começar o jogo! Gerando um número aleatório...")
    fortuna_infortunio = representar_em_complemento_de_dois(str(sua_sorte))
    time.sleep(0.5)
    print("O seu número inicial é " + fortuna_infortunio + "!")
    time.sleep(1)
    index = lista_bin.index(fortuna_infortunio)

    print("Vamos rodar a roda! A primeira vez é obrigatória!")
    time.sleep(0.5)
    print(".", end='')
    time.sleep(0.5)
    print(".", end='')
    time.sleep(0.5)
    print(".", end='')
    sua_sorte = random.randint(-8, 7)
    print("Sua sorte é: " + str(sua_sorte))

    tamanho_lista = len(lista_bin)
    falta_pra_extrapolar = (tamanho_lista - 1) - index

    if index+sua_sorte > (tamanho_lista - 1):
        fortuna_infortunio = lista_bin[sua_sorte - falta_pra_extrapolar]
    else:
        fortuna_infortunio = lista_bin[index + sua_sorte]

    index = lista_bin.index(fortuna_infortunio)

    print("O seu novo número é: " + fortuna_infortunio + "!")
    time.sleep(0.5)
    print("Então, deseja jogar? Sim (digite 's') ou Não (digite 'd', de desistência), você tem até três tentativas!")
    entrada_jogador = input("Vamos jogar? ")


# Copiei a função abaixo do trabalho 1, de forma a preencher a lista e fazer as conversões iniciais para representação
# em complemento de 2
def converter_valor_decimal_para_binario(valor):
    saida = ""

    entrada_como_string = str(valor)
    tamanho_entrada = len(entrada_como_string)

    resto = 0
    resultado = valor

    # O cálculo abaixo é realizado para saber a quantidade de vezes que passaremos no laço, como explicado em sala na
    # primeira aula (A vantagem computacional de utilizar um for ao invés de um while :))
    if(valor != 0):
        numero_digitos = int(math.log(valor, 2)) + 1
    else:
        numero_digitos = 1

    # Laço responsável por fazer as conversões de fato
    for i in range(numero_digitos):
        # print(str(resultado) + " dividido pela base " + str(base))
        resto = resultado % 2
        resultado = resultado // 2 # usando o operador que pega a parte inteira da divisão
        # print(str(resultado) + " com resto " + str(resto))

        saida = str(resto) + saida

    return saida

def representar_em_complemento_de_dois(valor):
    # Essa função responsabiliza-se pela adequação aos valores para complemento de dois
    valor_bin = "0"
    saida = "0000"

    # nossos numeros serão representados aqui sempre com 4 dígitos, usando a regra do MSB (most significant bit)

    if int(valor) > 0:
        valor_bin = converter_valor_decimal_para_binario(int(valor))
        saida = "0000" + valor_bin # Adicionando o valor em binario ao fim da representação basica, no for abaixo reduzo a quantidade de caracteres :)
        tamanho_numero = len(valor_bin)

        saida = saida[tamanho_numero:] # Usando a função slice para reduzir o tamanho da saída

        return saida
    elif int(valor) < 0:
        valor_bin = converter_valor_decimal_para_binario(int(valor[-1])) # converter somente o número, sem sinal
        saida = "1000" + valor_bin
        tamanho_numero = len(valor_bin)

        saida = "1" + saida[tamanho_numero + 1:] # Usando a função slice para reduzir o tamanho da saída

        # Estamos invertendo os números, contudo, resta ainda fazermos o complemento de dois nesses valores, coisa que
        # será feita abaixo:

        primeiro_um = False
        nova_saida = ""

        for numero in reversed(saida[1:]):
            if primeiro_um == False:
                if numero == '1':
                    primeiro_um = True
                    nova_saida = "1" + nova_saida
                elif numero == '0':
                    nova_saida = "0" + nova_saida
            elif primeiro_um == True:
                if numero == '1':
                    nova_saida = "0" + nova_saida
                elif numero == '0':
                    nova_saida = "1" + nova_saida

        saida = '1' + nova_saida

        return saida
    else:
        return saida

def converter_lista(lista):
    # Nessa função, iremos iretar sobre a lista e converter valor a valor, se positivo, realizar conversão normal e com-
    # plementar com zeros, se negativo, iremos utilizar a representação utilizando complemento de dois!

    for numero in lista:
        novo_valor = representar_em_complemento_de_dois(numero)
        lista[int(numero)] = novo_valor

    # print(lista)

    return lista

def imprimir_roda_da_fortuna_ascii_art():
    print(
        "MMMMMMMMMMMMMMMMMMMMWk,....,OWMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMNKOxol' '::' 'loxOKNMMMMMMMMMMMMMMM\nMMMMM"
        "MMMMMMN0xl:;,''..  ..  ..'',;:ld0WMMMMMMMMMMM\nMMMMMMMMWKd:;,'',;,.,cl,  .:;'.',,'',;:dKWMMMMMMMM\nMMMMMMW0l,"
        ",,'...lOkdkKKl..:xxolod:...,,,,l0WMMMMMM\nMMMMMKl,,,..,:;.;kKKKKKl..:xxxxxo'.,:,..,,,lKMMMMM\nMMMWO;';'..,cl"
        "l:.,x0KKKl..:xxxxl..;loc,..';';OWMMM\nMMWx,,,..:llllll:.'d0KKl..:xxxc..:llllll:..,,,xWMM\nMWk',,....';cllllc"
        "..lxd;. 'cl:..cllllc;''''.,,'kWM\nMK;';.;ddc;'.',:ll;..;:cccc:,..;ll:,'',cdO0c.;';KM\nWo';..;oxxxdl:,....:xK"
        "NNNNNNKx:...';lx0KKKOc.';'oW\nX:';.;dxxxxxxxxl..dKOkkkkkkkkOKo.'xKKKKKKK0Oc.;':X\nK,,,.':::::::::,.:K0c,,,,,"
        ",,,c0K:.:lllllllll;.,,,0\nK,,,.,ccccccccc;.:XKo::;;;;::o0K:.';;;;;;;;;'.,,,0\nX;';.l00KKKKKKKk,.dXXKd:;;:dKX"
        "Xd..oxxxxxxxxd:.;';X\nWo';'.ckKKK0ko:,...ckKK0000KKkc...',coxxxxo;..;'oW\nM0;,;.c0Oxl;'',:ll;..,:cllcc;..;ll"
        ":,..';ldd;.;,;KM\nMWk',,.,,'';cllllc'.;lc'..,oxc.'cllolc;'.''.,,'kWM\nMMWx',,..:llllll:..cxxx:..l0K0o..:llll"
        "ll:..,,'xWMM\nMMMWk;';'.',col:..lxxxx:..l0KK0d'.:loc,..';,;kWMMM\nMMMMMKl,,,..,c;.'lxxxxx:..l0KKKKx,.;c,..,,"
        ",lKMMMMM\nMMMMMMW0l,,,'...:ddloxx;..lKKkxOOl...',,,l0WMMMMMM\nMMMMMMMMWKd:,,'',,'.'::'..,ol,.';,'',;:oKWMMMM"
        "MMMM\nMMMMMMMMMMMN0dc:;,''.''''.'''.'',;:cd0NMMMMMMMMMMM\nMMMMMMMMMMMMMMWXOo;'..........';oOXWMMMMMMMMMMMMMM")

    print("\nOlá! Seja muito bem-vindo a Roda da Fortuna!")
    time.sleep(2)
    print("\nOu devo eu dizer... Infortúnio? É o que veremos!")
    time.sleep(2)

if __name__ == "__main__":
    main()