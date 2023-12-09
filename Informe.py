import streamlit as st
import pandas as pd

# Carregar o dataset
df = pd.read_csv('obito_cartorio.csv')

# Converter a coluna 'date' para o formato de data
df['date'] = pd.to_datetime(df['date'])

# Página de Apresentação
st.title("Análise de Óbitos por COVID-19")
st.header("Bem-vindo à Análise de Óbitos por COVID-19")
st.write(
    "Esta análise utiliza dados do dataset sobre óbitos por COVID-19. "
    "O COVID-19 é uma doença respiratória causada pelo coronavírus SARS-CoV-2. "
    "O dataset utilizado contém informações sobre óbitos registrados em cartórios."
)

# Link para o dataset no Brasil.IO
st.write("Mais informações sobre o dataset podem ser encontradas (https://brasil.io/dataset/covid19/files/).")

# Exibir informações gerais
st.header("Informações Gerais")
st.write("Aqui estão algumas informações gerais sobre a análise:")

# Adicione mais informações gerais conforme necessário
st.write(
    "- Esta análise considera dados de óbitos registrados em cartórios em todo o Brasil."
)
st.write(
    "- As informações são provenientes do dataset público disponibilizado pelo Brasil.IO."
)
st.write(
    "- Para uma análise mais detalhada, consulte os dados brutos e a documentação completa do dataset."
)

# Adicionar link para dados brutos
st.subheader("Dados Brutos")
st.write(
    "Os dados brutos deste dataset estão disponíveis [aqui](https://brasil.io/dataset/covid19/files/)."
)

# Exibir conclusões ou análises
st.header("Conclusões e Análises")
st.write("Neste espaço, você pode adicionar conclusões ou análises adicionais.")

# Adicionar link para análises aprofundadas
st.subheader("Análises Aprofundadas")
st.write(
    "Para análises mais detalhadas ou personalizadas, você pode acessar "
    "[páginas específicas](https://brasil.io/dataset/covid19/files/) relacionadas aos tópicos de interesse."
)

# Exibir dados específicos da tabela
st.header("Dados Específicos da Tabela")
selected_columns = st.multiselect("Selecione as colunas a serem exibidas:", df.columns)
if selected_columns:
    st.write(df[selected_columns])

# Filtrar informações de mortes no total, por ano e por mês
st.header("Análise de Óbitos por COVID-19")
st.subheader("Total de Mortes")
total_mortes = df['deaths_total_2020'].sum()
st.write(f"O total de mortes registradas em 2020 é: {total_mortes}")

# Filtrar por ano
ano_selecionado = st.selectbox("Selecione um ano:", df['date'].dt.year.unique())
df_ano = df[df['date'].dt.year == ano_selecionado]

# Exibir total de mortes por ano
st.subheader(f"Total de Mortes em {ano_selecionado}")
total_mortes_ano = df_ano['deaths_total_2020'].sum()
st.write(f"O total de mortes em {ano_selecionado} é: {total_mortes_ano}")