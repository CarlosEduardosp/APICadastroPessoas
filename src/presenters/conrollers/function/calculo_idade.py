from datetime import datetime


def calcular_idade(data_nascimento: str):
    """Função para calcular a idade com base na data de nascimento."""

    if len(data_nascimento) == 8:

        # convertento a string data_nascimento, em datetime
        data_nascimento = datetime.strptime(data_nascimento, "%d%m%Y")
        data_atual = datetime.now()

        if data_nascimento.year >= data_atual.year:
            return 0

        else:

            if data_atual.month > data_nascimento.month \
                    or (data_atual.month == data_nascimento.month
                        and data_atual.day >= data_nascimento.day):

                # Retorna a idade, já contando o aniversário do ano atual.
                idade = data_atual.year - data_nascimento.year
            else:
                # Retorna a idade, sem contar o aniversário do ano atual.
                idade = data_atual.year - data_nascimento.year - 1

            return idade

    else:
        return 0


