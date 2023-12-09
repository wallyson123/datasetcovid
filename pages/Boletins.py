import pandas as pd
import streamlit as st

# Carregar dados do CSV
caminho_arquivo = "boletim.csv"
df = pd.read_csv(caminho_arquivo)

# Criar um aplicativo Streamlit
st.title("Análise da Base de Dados")

# Exibir total de mortes por motivo e ano na tabela de óbitos
st.subheader(f"Total de Mortes por {motivo_selecionado} em {ano_selecionado_obito}")
total_mortes_motivo_ano_obito = df_ano_obito[motivo_selecionado].sum()
st.write(f"O total de mortes por {motivo_selecionado} em {ano_selecionado_obito} é: {total_mortes_motivo_ano_obito}")

# Filtro por estados na barra lateral
selected_state = st.sidebar.selectbox("Selecione um estado para filtrar:", df["state"].unique())

# Filtrar o DataFrame com base no estado selecionado
filtered_df = df[df["state"] == selected_state]

# Descrição rápida da base de dados
st.header("Descrição da Base de Dados:")
st.write("Esta base de dados contém informações sobre datas, notas, estados e URLs.")
st.write(f"Tamanho da base de dados: {filtered_df.shape[0]} linhas e {filtered_df.shape[1]} colunas para o estado selecionado.")

# Exibir o DataFrame filtrado
st.header(f"Visualização dos Dados para o Estado {selected_state}:")
st.dataframe(filtered_df)

# Você pode adicionar mais análises e visualizações conforme necessário
# ...

# Informações sobre as colunas
st.header("Informações sobre as Colunas:")
st.write("1. **Date:** Data do registro.")
st.write("2. **Notes:** Notas associadas aos registros.")
st.write("3. **State:** Estado relacionado ao registro.")
st.write("4. **URL:** URL associada ao registro.")