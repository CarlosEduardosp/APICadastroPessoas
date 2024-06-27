
# Comando SQL para criar a tabela imagem
create_imagem_table_query = '''CREATE TABLE imagem (
    id SERIAL PRIMARY KEY NOT NULL,
    id_pessoa INTEGER NOT NULL,
    imagem BYTEA NOT NULL, 
    nome VARCHAR(50) NOT NULL      
);'''