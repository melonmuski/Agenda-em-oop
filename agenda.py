class Agenda:

    def __init__(self):
        self.__recebe_agenda = f'{input("Titulo:")}\n{input("Descrição:")}\n{input("Categoria:")}'
        self.__data_agenda = f'{int(input("Dia:")):02d}/{int(input("Mes:")):02d}/{int(input("Ano:")):02d}, ' \
                             f'{int(input("Hora:")):02d}:{int(input("Minuto")):02d}'

    @property
    def agenda(self):
        return self.__recebe_agenda

    @property
    def data(self):
        return self.__data_agenda
