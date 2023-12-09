import streamlit as st
import pandas as pd

# Carregar os datasets
df_obito = pd.read_csv('obito_cartorio.csv')
df_boletim = pd.read_csv('boletim.csv')

# Converter a coluna 'date' para o formato de data em ambos os DataFrames
df_obito['date'] = pd.to_datetime(df_obito['date'])
df_boletim['date'] = pd.to_datetime(df_boletim['date'])

# Página de Apresentação
st.title("Análise de Óbitos e Boletins por COVID-19")
st.header("Bem-vindo à Análise de Óbitos e Boletins por COVID-19")
st.write(
    "Esta análise utiliza dados dos datasets sobre óbitos e boletins por COVID-19. "
    "O COVID-19 é uma doença respiratória causada pelo coronavírus SARS-CoV-2. "
    "Os datasets utilizados contêm informações sobre óbitos registrados em cartórios e boletins."
)

# Link para os datasets no Brasil.IO
st.write("Mais informações sobre os datasets podem ser encontradas em (https://brasil.io/dataset/covid19/files/).")

# Filtrar dados específicos da tabela de óbitos
st.header("Dados Específicos da Tabela de Óbitos")
selected_columns_obito = st.multiselect("Selecione as colunas a serem exibidas (Óbitos):", df_obito.columns)
if selected_columns_obito:
    st.write(df_obito[selected_columns_obito])

# Filtrar informações de mortes por motivo e ano na tabela de óbitos
st.header("Análise de Óbitos por Motivo e Ano")
motivos_mortes = df_obito.columns[df_obito.columns.str.startswith('deaths_')].tolist()
motivo_selecionado = st.selectbox("Selecione um motivo de morte:", motivos_mortes)

# Filtrar por ano na tabela de óbitos
ano_selecionado_obito = st.selectbox("Selecione um ano (Óbitos):", df_obito['date'].dt.year.unique())
df_ano_obito = df_obito[df_obito['date'].dt.year == int(ano_selecionado_obito)]

# Exibir total de mortes por motivo e ano na tabela de óbitos
st.subheader(f"Total de Mortes por {motivo_selecionado} em {ano_selecionado_obito}")
total_mortes_motivo_ano_obito = df_ano_obito[motivo_selecionado].sum()
st.write(f"O total de mortes por {motivo_selecionado} em {ano_selecionado_obito} é: {total_mortes_motivo_ano_obito}")

# Filtrar dados específicos da tabela de boletins
st.header("Dados Específicos da Tabela de Boletins")
selected_columns_boletim = st.multiselect("Selecione as colunas a serem exibidas (Boletins):", df_boletim.columns)
if selected_columns_boletim:
    st.write(df_boletim[selected_columns_boletim])

# Filtrar por ano na tabela de boletins
ano_selecionado_boletim = st.selectbox("Selecione um ano (Boletins):", df_boletim['date'].dt.year.unique())
df_ano_boletim = df_boletim[df_boletim['date'].dt.year == int(ano_selecionado_boletim)]

# Exibir dados completos da tabela de boletins
st.subheader(f"Boletins em {ano_selecionado_boletim}")
st.write(df_ano_boletim)