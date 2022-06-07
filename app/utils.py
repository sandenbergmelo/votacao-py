from rich import print


def limpar():
    from os import system, name
    system('cls' if name == 'nt' else 'clear')


def confirmar(msg: str = '') -> bool:
    while True:
        try:
            valor = str(input(f'{msg} [S/N]: ')).strip().upper()[0]
            if valor not in 'SN':
                print('[red][bold]ERRO![/] Digite uma opção válida.[/]')
                continue
        except (ValueError, TypeError):
            print('[red][bold]ERRO![/] Digite uma opção válida.[/]')
            continue
        except KeyboardInterrupt:
            print('\n[yellow][bold]Interrupção![/][/]')
            continue

        return True if valor == 'S' else False


def input_int(msg: str = '') -> int:
    """Lê um número inteiro"""
    while True:
        try:
            valor = int(str(input(msg)).strip())
        except (ValueError, TypeError):
            print('[red][bold]ERRO![/] Digite um número inteiro válido.[/]')
            continue
        except KeyboardInterrupt:
            print(
                '\n[yellow][bold]Interrupção![/] O usuário preferiu interromper a leitura.[/]')
            valor = 0

        return valor


def linha(tamanho: int = 42) -> str:
    return '-' * tamanho


def cabecalho(txt: str) -> str:
    tamanho = len(txt) + 4

    print(linha(tamanho))
    print(txt.center(tamanho))
    print(linha(tamanho))


def menu(titulo, lista: list) -> int:
    cabecalho(titulo)

    for i, item in enumerate(lista):

        print(f'[yellow]{i}[/] - [blue]{item}[/]')
    print(linha(11))

    while True:
        opc = input_int('Sua opção: ')
        if opc >= 0 and opc <= i:
            break
        print('[red][bold]ERRO! [/]Digite uma opção válida[/]')
    return opc
