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

# Contagem total de mortos durante toda a pandemia
total_mortes_pandemia = df_obito['deaths_total_2020'].sum() + df_obito['deaths_total_2019'].sum()
st.subheader(f"Total de Mortes durante a Pandemia")
st.write(f"O total de mortes durante a pandemia é: {total_mortes_pandemia}")

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

# Informações sobre as Colunas - Tabela de Óbitos
st.subheader("Informações sobre as Colunas - Tabela de Óbitos")
st.write("""
- date: Data do registro.
- state: Estado onde ocorreu o óbito.
- epidemiological_week_2019: Semana epidemiológica no ano de 2019.
- epidemiological_week_2020: Semana epidemiológica no ano de 2020.
- deaths_indeterminate_2019: Número de óbitos com causa indeterminada no ano de 2019.
- deaths_respiratory_failure_2019: Número de óbitos por insuficiência respiratória no ano de 2019.
- deaths_others_2019: Número de óbitos por outras causas no ano de 2019.
- deaths_pneumonia_2019: Número de óbitos por pneumonia no ano de 2019.
- deaths_septicemia_2019: Número de óbitos por septicemia no ano de 2019.
- deaths_sars_2019: Número de óbitos por SARS (Síndrome Respiratória Aguda Grave) no ano de 2019.
- deaths_covid19: Número de óbitos por COVID-19.
- deaths_indeterminate_2020: Número de óbitos com causa indeterminada no ano de 2020.
- deaths_respiratory_failure_2020: Número de óbitos por insuficiência respiratória no ano de 2020.
- deaths_others_2020: Número de óbitos por outras causas no ano de 2020.
- deaths_pneumonia_2020: Número de óbitos por pneumonia no ano de 2020.
- deaths_septicemia_2020: Número de óbitos por septicemia no ano de 2020.
- deaths_sars_2020: Número de óbitos por SARS (Síndrome Respiratória Aguda Grave) no ano de 2020.
- deaths_total_2019: Número total de óbitos no ano de 2019.
- deaths_total_2020: Número total de óbitos no ano de 2020.
- new_deaths_indeterminate_2019: Novos óbitos com causa indeterminada no ano de 2019.
- new_deaths_respiratory_failure_2019: Novos óbitos por insuficiência respiratória no ano de 2019.
- new_deaths_others_2019: Novos óbitos por outras causas no ano de 2019.
- new_deaths_pneumonia_2019: Novos óbitos por pneumonia no ano de 2019.
- new_deaths_septicemia_2019: Novos óbitos por septicemia no ano de 2019.
- new_deaths_sars_2019: Novos óbitos por SARS (Síndrome Respiratória Aguda Grave) no ano de 2019.
- new_deaths_covid19: Novos óbitos por COVID-19.
- new_deaths_indeterminate_2020: Novos óbitos com causa indeterminada no ano de 2020.
- new_deaths_respiratory_failure_2020: Novos óbitos por insuficiência respiratória no ano de 2020.
- new_deaths_others_2020: Novos óbitos por outras causas no ano de 2020.
- new_deaths_pneumonia_2020: Novos óbitos por pneumonia no ano de 2020.
- new_deaths_septicemia_2020: Novos óbitos por septicemia no ano de 2020.
- new_deaths_sars_2020: Novos óbitos por SARS (Síndrome Respiratória Aguda Grave) no ano de 2020.
- new_deaths_total_2019: Novo total de óbitos no ano de 2019.
- new_deaths_total_2020: Novo total de óbitos no ano de 2020.
""")

# Informações sobre as Colunas - Tabela de Boletins
st.subheader("Informações sobre as Colunas - Tabela de Boletins")
st.write("""
- date: Data do registro do boletim.
- notes: Notas relacionadas ao boletim.
- state: Estado ao qual o boletim está associado.
- url: URL relacionada ao boletim.
""")

# Total de Colunas, Linhas e Tabelas
total_colunas_obito = df_obito.shape[1]
total_linhas_obito = df_obito.shape[0]
total_colunas_boletim = df_boletim.shape[1]
total_linhas_boletim = df_boletim.shape[0]

st.subheader("Total de Colunas, Linhas e Tabelas")
st.write(f"Total de colunas na tabela de óbitos: {total_colunas_obito}")
st.write(f"Total de linhas na tabela de óbitos: {total_linhas_obito}")
st.write(f"Total de colunas na tabela de boletins: {total_colunas_boletim}")
st.write(f"Total de linhas na tabela de boletins: {total_linhas_boletim}")