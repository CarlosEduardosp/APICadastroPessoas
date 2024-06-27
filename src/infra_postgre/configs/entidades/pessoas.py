

# Comando SQL para criar a tabela pessoas
create_pessoas_table_query = '''CREATE TABLE pessoas (
    id SERIAL PRIMARY KEY NOT NULL,
    nome VARCHAR(40) NOT NULL,
    data_nascimento VARCHAR(20) NOT NULL,
    telefone VARCHAR(20) NOT NULL,
    email VARCHAR(40) NOT NULL,
    sexo VARCHAR(20) NOT NULL,
    estado VARCHAR(30) NOT NULL,
    cidade VARCHAR(30) NOT NULL,
    bairro VARCHAR(30) NOT NULL,
    logradouro VARCHAR(50) NOT NULL,
    numero VARCHAR(25) NOT NULL,
    complemento VARCHAR(60) NOT NULL,
    status BOOLEAN NOT NULL    
);'''
