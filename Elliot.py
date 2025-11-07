import pandas as pd

def ajouter_colonne_string(fichier_csv):
    df = pd.read_csv(fichier_csv)
    
    df['Population_string'] = df['Populationtotal'].astype(str)
    
    df.to_csv('communes-france-INSEE.csv', index=False)
    
    
    return df

df = ajouter_colonne_string('communes-france-INSEE.csv')