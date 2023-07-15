from random import randint

def jogo(escolha_jogador, jogador):
    opcoes = ('Pedra', 'Papel', 'Tesoura')
    escolha_jogador = opcoes[escolha_jogador]
    escolha_computador = opcoes[randint(0,2)]
    print('-=' *12)
    print('O player {} jogou {}'.format(jogador, escolha_jogador))
    print('O computador jogou {}'.format(escolha_computador))
    print('-=' *12)
    if escolha_jogador == escolha_computador:
        return 'EMPATE! :|'
    elif escolha_jogador == 'Pedra' and escolha_computador == 'Tesoura':
        return '{} VENCEU! :D'.format(jogador)
    elif escolha_jogador == 'Papel' and escolha_computador == 'Pedra':
        return '{} VENCEU! :D'.format(jogador)
    elif escolha_jogador == 'Tesoura' and escolha_computador == 'Papel':
        return '{} VENCEU! :D'.format(jogador)
    elif escolha_computador == 'Pedra' and escolha_jogador == 'Tesoura':
        return '{} PERDEU! :( O domínio das máquinas está apenas começando...)'.format(jogador)
    elif escolha_computador == 'Papel' and escolha_jogador == 'Pedra':
        return '{} PERDEU! :( O domínio das máquinas está apenas começando...)'.format(jogador)
    elif escolha_computador == 'Tesoura' and escolha_jogador == 'Papel':
        return '{} PERDEU! :( O domínio das máquinas está apenas começando...)'.format(jogador)
    else:
        return 'Isso não é uma opção fi! Joga de novo u.U'