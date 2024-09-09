import pandas as pd
from datetime import datetime

def convert_value(value, col_type):
    if pd.isnull(value):
        return "NULL"
    
    conversion_map = {
        'string': lambda v: f"'{str(v)}'",
        'float': lambda v: f"{float(v)}",  
        'int': lambda v: f"{int(v)}",    
        'date': lambda v: f"'{v.strftime('%Y')}'" if isinstance(v, datetime) else f"'{pd.to_datetime(v).strftime('%Y')}'"
    }
    
    conversion_func = conversion_map.get(col_type, conversion_map['string'])
    
    return conversion_func(value)