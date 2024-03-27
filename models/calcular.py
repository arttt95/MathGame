from random import randint


class Calcular:

    def __init__(self, dificuldade: int, /) -> None:
        self.__dificuldade: int = dificuldade
        self.__valor1: int = self._gerar_valor
        self.__valor2: int = self._gerar_valor
        self.__operacao: int = randint(1, 3)  # 1 = somar; 2 = subtrair; 3 = multiplicar.
        self.__resultado: int = self._gerar_resultado

    @property
    def dificuldade(self: object) -> int:
        return self.__dificuldade

    @property
    def valor1(self: object) -> int:
        return self.__valor1

    @property
    def valor2(self: object) -> int:
        return self.__valor2

    @property
    def operacao(self: object) -> int:
        return self.__operacao

    @property
    def resultado(self: object) -> int:
        return self.__resultado

    def __str__(self: object) -> str:
        oper: str = ''
        if self.operacao == 1:
            oper = 'Somar'
        elif self.operacao == 2:
            oper = 'Subtrair'
        else:
            oper = 'Multiplicar'
        return (f'Valor 1: {self.valor1}\n'
                f'Valor 2: {self.valor2}\n'
                f'Dificuldade: {self.dificuldade}\n'
                f'Operação: {oper}')

    @property
    def _gerar_valor(self: object) -> int:
        if self.dificuldade == 1:
            return randint(1, 10)
        elif self.dificuldade == 2:
            return randint(0, 100)
        elif self.dificuldade == 3:
            return randint(0, 1_000)
        elif self.dificuldade == 4:
            return randint(0, 10_000)
        else:
            print('Você não inseriu uma dificuldade válida entre 1 e 4,'
                  ' por isso o jogo será iniciado na dificuldade 5.')
            return randint(0, 100_000)

    @property
    def _gerar_resultado(self: object) -> int:
        if self.operacao == 1:
            return self.valor1 + self.valor2
        elif self.operacao == 2:
            return self.valor1 - self.valor2
        else:
            return self.valor1 * self.valor2

    @property
    def _op_simbolo(self: object) -> str:
        if self.operacao == 1:
            return '+'
        elif self.operacao == 2:
            return '-'
        else:
            return '*'

    def checar_resultado(self: object, resposta: int) -> bool:
        certo: bool = False
        if self.resultado == resposta:
            print('Resposta correta!')
            certo = True
        else:
            print('Resposta errada!')
        print(f'{self.valor1} {self._op_simbolo} {self.valor2} = {self.resultado}')
        return certo

    def mostrar_operacao(self: object) -> None:
        print(f'{self.valor1} {self._op_simbolo} {self.valor2} = ?')
