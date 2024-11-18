import pandas as pd
from sklearn.preprocessing import LabelEncoder

pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.colheader_justify', 'left')

df = pd.read_csv('cliente_v2_preparado.csv')

# Codificação one-hot para 'estado_civil' em True ou False
df = pd.concat([df, pd.get_dummies(df['estado_civil'], prefix='estado_civil')], axis=1)

# Codificação ordinal para 'nivel_educação'
educacao_ordem = {'Ensino Fundamental': 1, 'Ensino Médio': 2, 'Ensino Superior': 3, 'Pós-graduação': 4}
df['nivel_educacao_ordinal'] = df['nivel_educacao'].map(educacao_ordem)

#Codificação cat.codes para 'area_atuacao' que cria a numeração automaticamente (semelhante ao LabelEncoder)
df['area_atuacao_cod'] = df['area_atuacao'].astype('category').cat.codes

#Codificando com LabelEncoder para 'estado', que cria um númenro para cada valor único de 0 a n_classes-1
label_encoder = LabelEncoder()
df['estado_cod'] = label_encoder.fit_transform(df['estado'])

print (df)