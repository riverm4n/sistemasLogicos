# Trabalho prático 2 de Sistemas Lógicos, na Universidade Federal do Amazonas, no período 2022/2, ano 2023.
# por Mário Hirotoshi Sugai Júnior, matrícula 22060031

# De uma forma geral, o jogo produz um valor aleatório inicial que é apresentado ao jogador. O jogador tem que girar a
# roda (produzir um outro valor aleatório e somar ao anterior). Caso não goste do resultado, ele tem mais 3 tentativas
# para mudar. A primeira é sempre obrigatória. Ele não pode ficar com o valor inicial, mesmo que seja o maior valor.

def main():
    imprimir_roda_da_fortuna_ascii_art()

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

if __name__ == "__main__":
    main()