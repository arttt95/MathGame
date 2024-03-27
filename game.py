from models.calcular import Calcular


def main() -> None:
    pontos: int = 0
    jogar(pontos)


def jogar(pontos: int) -> None:
    dificuldade: int = int(input('Informe um nível de dificuldade entre 1 e 4: '))

    calc: Calcular = Calcular(dificuldade)
    print(f'Informe o resultado para a seguinte operação: ')
    calc.mostrar_operacao()  # Irá apresentar "valor1 op valor2 = ?"

    resposta: int = int(input())

    if calc.checar_resultado(resposta):
        pontos = pontos + 1
        print(f'Parabéns você acertou e agora tem {pontos} ponto(s).')
    else:
        print(f'Você continua com {pontos} ponto(s).')

    continuar: int = int(input('Deseja continuar no jogo? [1 - Sim, 0 - Não]: '))

    if continuar:
        print('\n')
        jogar(pontos)
    else:
        print(f'Você finalizou o jogo com {pontos} ponto(s)')
        print('Tks milhão e até a próxima!')


if __name__ == '__main__':
    main()
