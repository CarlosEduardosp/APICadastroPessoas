def Validar_dados_entrada(
        nome: str = "",
        data_nascimento: str = "00000000",
        telefone: str = "",
        email: str = "@",
        sexo: str = "x",
        estado: str = "",
        cidade: str = "",
        bairro: str = "",
        logradouro: str = "",
        numero: str = "",
        status: bool = True,
        complemento: str = '',
        id: int = 0
) -> bool:
    """ Validador de dados """

    if not isinstance(nome, str):
        return {"success": False, "data": "Nome deve ser uma String"}

    if len(nome) > 40:
        return {"success": False, "data": "Nome deve ser menor que 40 caracteres"}

    if not isinstance(data_nascimento, str):
        return {"success": False, "data": "data_nascimento deve ser uma string"}

    if len(data_nascimento) != 8:
        return {"success": False, "data": f"Apenas {len(data_nascimento)} numeros, e data de Nascimento"
                                          f" deve conter 8 numeros,'2' para o dia, '2' para o mês, '4' para o ano."}

    if not isinstance(email, str):
        return {"success": False, "data": "Email precisa ser uma string."}

    if "@" not in email:
        return {"success": False, "data": "Email inválido, '@' precisa estar no email."}

    if not isinstance(telefone, str):
        return {"success": False, "data": "telefone deve ser uma string"}

    if len(telefone) != 11:
        return {"success": False, "data": f"Apenas {len(telefone)} numeros, e Telefone"
                                          f" deve conter 11 numeros,'2' para o DDD, '9' para numero do telefone."
                                          f"ex: 22988887777, totalizando 11 numeros."}

    if not isinstance(sexo, str):
        return {"success": False, "data": "Sexo deve ser uma string."}

    if len(sexo) > 1:
        return {"success": False, "data": "Sexo deve conter apenas 1 caracter, 'M' ou 'F'."}

    if not isinstance(estado, str):
        return {"success": False, "data": "estado deve ser uma string"}

    if not isinstance(cidade, str):
        return {"success": False, "data": "cidade deve ser uma string"}

    if not isinstance(bairro, str):
        return {"success": False, "data": "bairro deve ser uma string"}

    if not isinstance(logradouro, str):
        return {"success": False, "data": "logradouro deve ser uma string"}

    if not isinstance(numero, str):
        return {"success": False, "data": "numero deve ser uma string"}

    if not isinstance(complemento, str):
        return {"success": False, "data": "complemento deve ser uma string"}

    if not isinstance(status, bool):
        return {"success": False, "data": "Status deve ser um Boolean"}

    if not isinstance(id, int):
        return {"success": False, "data": "Id deve ser um numero nteiro"}

    return {"success": True, "data": "Tudo Ok"}
