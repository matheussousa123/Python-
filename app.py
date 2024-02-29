DELIMITADOR = ';'

PASTA_ARQUIVOS = 'CruzamentoPlanilhas'

ARQUIVO_SAIDA = 'PlanilhasCruzadas.csv'

 

DOCUMENTO_1 = {

    'nome': 'NomePlanilha1.csv',

    'colunas': ['Pasta1', 'Pasta2'],

    'coluna_comum': 'Nome'

}

 

DOCUMENTO_2 = {

    'nome': 'NomePlanilha2.csv',

    'colunas': ['Pasta1', 'Pasta2'],

    'coluna_comum': 'Idade'

}

DOCUMENTO_3 = {

    'nome': 'NomePlanilha3.csv',

    'colunas': ['Pasta1', 'Pasta2'],

    'coluna_comum': 'Endereço'

}

 

DOCUMENTOS = [DOCUMENTO_1, DOCUMENTO_2, DOCUMENTO_3]

 

################################################################################

 

import pandas as pd

from tqdm import tqdm

 

ENCODING = 'utf-8-sig'

result = None

temp_column = None

 

 

for file in tqdm(DOCUMENTOS):

    temp_file = pd.read_csv(

        f'{PASTA_ARQUIVOS}/{file["nome"]}', sep=DELIMITADOR, encoding=ENCODING)

 

    if result is not None:

        result = pd.merge(

            result,

            temp_file[file['colunas']],

            left_on=temp_column,

            right_on=file['coluna_comum'],

            how='outer')

    else:

        result = temp_file[file['colunas']]

        temp_column = file['coluna_comum']

 

result.to_csv(ARQUIVO_SAIDA, index=False, sep=DELIMITADOR, encoding=ENCODING)