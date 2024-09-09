from generate_insert_statatements import generate_insert_statements_from_xlsx

# Caminho e nome do arquivo
file_path = 'hist_ena.xlsx'
table_name = 'hist_ena'

# Tipo e nome das colunas
column_types = ['int', 'int', 'string', 'float'] 
column_names = ['Ano', 'Mes', 'Submercado', 'pc_mlt']


if __name__ == "__main__":
    insert_statements = generate_insert_statements_from_xlsx(file_path, table_name, column_types, column_names)

    # Salva os comandos de inserção no arquivo
    with open("inserts_hist_ena.sql", "w") as file:
        for statement in insert_statements:
            file.write(statement + '\n')
