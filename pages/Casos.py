import pandas as pd
import streamlit as st
import plotly.express as px

# Carregar dados do CSV
caminho_arquivo = "boletim.csv"
try:
    df = pd.read_csv(caminho_arquivo)
except FileNotFoundError:
    st.error(f"Arquivo não encontrado: {caminho_arquivo}")
    st.stop()



# Verificar se a coluna "state" está presente no DataFrame
if "state" not in df.columns:
    st.error("A coluna 'state' não está presente no DataFrame.")
    st.stop()

# Verificar se a coluna "date" está presente no DataFrame
if "date" not in df.columns:
    st.error("A coluna 'date' não está presente no DataFrame.")
    st.stop()

# Filtro por estado
selected_state = st.sidebar.selectbox("Selecione um estado para filtrar:", df["state"].unique())
filtered_df = df[df["state"] == selected_state]


# Exibir o DataFrame filtrado por estado
st.header(f"Visualização dos Dados para o Estado {selected_state}:")

st.dataframe(filtered_df)

# Verificar se a coluna "date" está presente no DataFrame filtrado
if "date" not in filtered_df.columns:
    st.error("A coluna 'date' não está presente no DataFrame filtrado.")
    st.stop()

# Filtro de casos por incidência mês a mês
st.header("Filtro de Casos por Incidência Mês a Mês:")
# Converter a coluna 'date' para o tipo datetime
filtered_df['date'] = pd.to_datetime(filtered_df['date'])
# Adicionar uma nova coluna 'Month' para extrair o mês
filtered_df['Month'] = filtered_df['date'].dt.month
# Agrupar por mês e contar o número de casos
monthly_incidence = filtered_df.groupby('Month').size().reset_index(name='Cases')

# Exibir gráfico de barras para a incidência mês a mês
st.bar_chart(monthly_incidence.set_index('Month'))

# Mapa dos estados mais afetados
st.header("Mapa dos Estados Mais Afetados:")
# Agrupar por estado e contar o número total de casos
total_cases_by_state = df.groupby('state').size().reset_index(name='Total Cases')

# Criar um mapa usando Plotly Express
fig = px.choropleth(total_cases_by_state,
                    locations='state',
                    locationmode='USA-states',
                    color='Total Cases',
                    scope="usa",
                    title='Estados Mais Afetados',
                    labels={'Total Cases': 'Número de Casos'}
                    )
# Exibir o mapa
st.plotly_chart(fig)