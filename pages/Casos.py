import pandas as pd
import streamlit as st
import plotly.express as px

# Carregar dados do CSV
caminho_arquivo = "obito_cartorio.csv"
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

# Mapa dos estados mais afetados no Brasil
st.header("Mapa dos Estados Mais Afetados no Brasil:")
# Agrupar por estado e contar o número total de casos
total_cases_by_state = df.groupby('state').size().reset_index(name='Total Cases')

# Criar um mapa usando Plotly Express para o Brasil
fig = px.choropleth(total_cases_by_state,
                    locations='state',
                    locationmode='country names',  # Use 'country names' for world maps
                    color='Total Cases',  # Specify the column for color scale
                    color_continuous_scale='reds',  # Adjust color scale as needed
                    title=f'Estados Mais Afetados no Brasil - {selected_state}',
                    labels={'Total Cases': 'Número de Casos'}
                    )

# Adicionar as informações de mortes no final do mapa
try:
    total_deaths = filtered_df[[
        'deaths_indeterminate_2020',
        'deaths_respiratory_failure_2020',
        'deaths_others_2020',
        'deaths_pneumonia_2020',
        'deaths_septicemia_2020',
        'deaths_sars_2020',
        'deaths_covid19',
        'new_deaths_indeterminate_2020',
        'new_deaths_respiratory_failure_2020',
        'new_deaths_others_2020',
        'new_deaths_pneumonia_2020',
        'new_deaths_septicemia_2020',
        'new_deaths_sars_2020',
        'new_deaths_total_2020'
    ]].sum()

    # Adicionar o total de mortes como uma anotação no mapa
    fig.add_annotation(
        x=0.5,
        y=-0.1,
        text=f'Total de Mortes: {total_deaths["new_deaths_total_2020"]}',
        showarrow=False,
        font=dict(size=12)
    )

    # Exibir o mapa
    st.plotly_chart(fig)

    # Exibir informações de mortes no final do mapa
    st.subheader("Total de Mortes por Categoria:")
    st.write(total_deaths)

except KeyError as e:
    st.error(f"Erro ao acessar colunas: {e}")