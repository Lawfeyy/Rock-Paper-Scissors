from jogada import jogo
from time import sleep

jogador = input('Bem vindo! Digite seu nome para contar a pontuação do jogo:  ')
print('''
-=-=-=OPÇÕES=-=-=-
[0] PEDRA
[1] PAPEL
[2] TESOURA
-=-=-=-=-=-=-=-=-''')
escolha = int(input('''Agora selecione uma das opções acima para sua jogada!
-->  '''))

print('Rufem os tambores!!')
sleep(1)
print('Aiiin zé da manga!')
sleep(1)

resultado = jogo(escolha, jogador)
print('{}'.format(resultado))