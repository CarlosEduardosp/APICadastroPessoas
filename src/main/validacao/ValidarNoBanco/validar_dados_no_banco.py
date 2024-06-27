from src.main.adapter.adapter_pessoa import AdapterPessoa
from src.main.composer.pessoa_composer import register_pessoa_composer


def conferir_pessoa_no_banco(email: str):
    """
    :param email: email inserido para cadastro.
    :return: True se o email já existir no banco, false caso não exista nenhum email igual no banco.
    """

    buscar = AdapterPessoa(
        api_route=register_pessoa_composer(),
        data={}
    )

    response = buscar.select_adapter()

    if response.status_code == 200:

        for item in response.body:

            # verifica se o email, enviado já se encontra no banco de dados.
            if email == item['email']:
                return False
        return True
    else:
        return False

