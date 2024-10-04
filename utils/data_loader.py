import pandas as pd

def load_data(filepath):
    return pd.read_csv(filepath, delimiter=';')

def search_data(df, query):
    results = df[df.apply(lambda row: row.astype(str).str.contains(query, case=False).any(), axis=1)]
    return results
