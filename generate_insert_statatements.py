import pandas as pd
from datetime import datetime
from convert_values import convert_value

def generate_insert_statements_from_xlsx(file_path, table_name, column_types, column_names=None):
    df = pd.read_excel(file_path)
    
    df = df.where(pd.notnull(df), None)
    
    if column_names:
        df.columns = column_names

    columns = df.columns.tolist() 
    
    insert_statements = []

    for index, row in df.iterrows():
        values = [
            convert_value(row[col], column_types[i]) for i, col in enumerate(columns)
        ]

        insert_query = f'INSERT INTO {table_name} ({", ".join(columns)}) VALUES ({", ".join(values)});'
        insert_statements.append(insert_query)
    
    return insert_statements
