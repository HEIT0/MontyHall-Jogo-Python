import random

print('\033[1;7;35m=-' * 20, 'PROBLEMA DE MONTY HALL', '-=' * 20, '\033[m')
print(
    "\033[1;36m--Em uma das portas há um carro e nas outras há cabras--\033[m\n"
    "\033[1;33mESCOLHA UMA PORTA:\n"
    "[ 1 ]\n"
    "[ 2 ]\n"
    "[ 3 ]\033[m")
nporta = float(input('Sua Escolha:'))
print('\033[1;35m-=\033[m' * 20)

if nporta > 3 or nporta < 1 or (nporta % 1) != 0:
    print('\033[1;33mEsta não é uma opção!\033[m')
    quit()
escolha = int(nporta)
premio = random.randint(1, 3)
portas = [1, 2, 3]

portas.remove(escolha)
if premio in portas:
    portas.remove(premio)

nada = random.choice(portas)

resto = [1, 2, 3]
resto.remove(nada)
resto.remove(escolha)

print(
    f"""\033[36mNa porta {nada} há apenas cabras, você quer trocar para a porta {random.choice(resto)} ou permanecer na sua?
    \033[1m[ 1 ]Permanecer
    [ 2 ]Trocar\033[m""")

nporta2 = float(input('Sua Escolha: '))

if nporta2 > 2 or nporta2 < 1 or (nporta2 % 1) != 0:
    print('\033[1;33mEsta não é uma opção!\033[m')
escolha2 = int(nporta2)
print('\033[1;35m-=\033[m' * 20)

if escolha2 == 1 and escolha == premio:
    print('\033[33;1mParabéns, Você ganhou o Carro\033[m')
elif escolha2 == 1 and escolha != premio:
    print('\033[31;1mVocê perdeu, na sua porta há cabras!\033[m')
elif escolha2 == 2 and random.choice(resto) == premio:
    print('\033[33;1mParabéns, Você ganhou o Carro\033[m')
elif escolha2 == 2 and random.choice(resto) != premio:
    print('\033[31;1mVocê perdeu, na porta que você trocou há cabras!\033[m')

print('\033[1;35m-=\033[m' * 20)
