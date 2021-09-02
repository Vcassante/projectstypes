from termcolor import colored
def leiaint(msg):
    while True:
        try:
            n=int(input(msg))
        except:
            print(colored('Erro digite um número inteiro válido!','red'))
            continue
        else:
            return n
            break

def leiareal(msg):
    while True:
        try:
            n=float(input(msg)).replace(',', '.')
        except(TypeError,ValueError):
            print(colored('Erro digite um número real válido', 'red'))
            continue 
        except KeyboardInterrupt:
            print('O usuário não quia digitar o valor')
            return 0
        else:
            return float(n)
            break



i=leiaint('Digite um número inteiro: ')
f=leiareal('Digite um número real: ')

print(f'Você digitou os números {i} e {f}')
