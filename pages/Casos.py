import pandas as pd
import streamlit as st
import plotly.express as px

# Carregar dados do CSV (obito_cartorio.csv)
caminho_arquivo_obito = "obito_cartorio.csv"
try:
    df_obito = pd.read_csv(caminho_arquivo_obito)
except FileNotFoundError:
    st.error(f"Arquivo não encontrado: {caminho_arquivo_obito}")
    st.stop()

# Verificar se a coluna "state" está presente no DataFrame do óbito
if "state" not in df_obito.columns:
    st.error("A coluna 'state' não está presente no DataFrame do óbito.")
    st.stop()

# Verificar se a coluna "date" está presente no DataFrame do óbito
if "date" not in df_obito.columns:
    st.error("A coluna 'date' não está presente no DataFrame do óbito.")
    st.stop()

# Adicionar controle deslizante para escolher o número mínimo de mortes
min_deaths_obito = st.slider("Escolha o número mínimo de mortes para ser considerado 'mais afetado' (óbito)", 0, 5000, 500)

# Filtro de casos por incidência mês a mês (óbito)
st.header("Filtro de Casos por Incidência Mês a Mês (óbito):")
# Converter a coluna 'date' para o tipo datetime
df_obito['date'] = pd.to_datetime(df_obito['date'])
# Adicionar uma nova coluna 'Month' para extrair o mês
df_obito['Month'] = df_obito['date'].dt.month
# Agrupar por mês, estado e contar o número de casos
monthly_incidence_obito = df_obito.groupby(['Month', 'state']).size().reset_index(name='Cases')

# Exibir gráfico de barras para a incidência mês a mês (óbito)
st.bar_chart(monthly_incidence_obito)

# Carregar dados do novo CSV (boletim.csv)
caminho_arquivo_boletim = "boletim.csv"
try:
    df_boletim = pd.read_csv(caminho_arquivo_boletim)
except FileNotFoundError:
    st.error(f"Arquivo não encontrado: {caminho_arquivo_boletim}")
    st.stop()

# Verificar se a coluna "state" está presente no DataFrame do boletim
if "state" not in df_boletim.columns:
    st.error("A coluna 'state' não está presente no DataFrame do boletim.")
    st.stop()

# Verificar se a coluna "date" está presente no DataFrame do boletim
if "date" not in df_boletim.columns:
    st.error("A coluna 'date' não está presente no DataFrame do boletim.")
    st.stop()

# Adicionar controle deslizante para escolher o número mínimo de mortes
min_deaths_boletim = st.slider("Escolha o número mínimo de mortes para ser considerado 'mais afetado' (boletim)", 0, 5000, 500)

# Filtro de casos por incidência mês a mês (boletim)
st.header("Filtro de Casos por Incidência Mês a Mês (boletim):")
# Converter a coluna 'date' para o tipo datetime
df_boletim['date'] = pd.to_datetime(df_boletim['date'])
# Adicionar uma nova coluna 'Month' para extrair o mês
df_boletim['Month'] = df_boletim['date'].dt.month
# Agrupar por mês, estado e contar o número de casos
monthly_incidence_boletim = df_boletim.groupby(['Month', 'state']).size().reset_index(name='Cases')

# Exibir gráfico de barras para a incidência mês a mês (boletim)
st.bar_chart(monthly_incidence_boletim)

# Combine data from both DataFrames to create a single DataFrame for the choropleth map
df_combined = pd.merge(df_obito.groupby('state')['new_deaths_total_2020'].sum().reset_index(), df_boletim.groupby('state')['url'].count().reset_index(), on='state')

# Mapa dos estados mais afetados no Brasil
st.header("Mapa dos Estados Mais Afetados no Brasil:")
# Adicionar cores ao mapa com base no número de mortes e casos
fig_map_combined = px.choropleth(df_combined,
                                  locations='state',
                                  locationmode='ISO-3',
                                  color='new_deaths_total_2020',
                                  color_continuous_scale='reds',
                                  title='Estados Mais Afetados no Brasil',
                                  labels={'color': 'Número de Mortes'},
                                  scope='south america'
                                  )
# Atualizar o layout do mapa para exibir o Brasil
fig_map_combined.update_geos(projection_type="natural earth", showcoastlines=True, coastlinecolor="black")

# Adicionar as informações de mortes e casos no final do mapa
try:
    # Adicionar o total de mortes como uma anotação no mapa
    fig_map_combined.add_annotation(
        x=0.5,
        y=-0.1,
        text=f'Total de Mortes: {df_combined["new_deaths_total_2020"].sum()}',
        showarrow=False,
        font=dict(size=12)
    )

    # Adicionar o total de casos como uma anotação no mapa
    fig_map_combined.add_annotation(
        x=0.5,
        y=-0.15,
        text=f'Total de Casos: {df_combined["url"].sum()}',
        showarrow=False,
        font=dict(size=12)
    )

    # Exibir o mapa
    st.plotly_chart(fig_map_combined)

    # Filtrar os estados mais afetados com base no número mínimo de mortes escolhido pelo usuário
    most_affected_states_combined = df_combined[df_combined['new_deaths_total_2020'] >= min_deaths_obito]

    # Exibir informações de mortes para os estados mais afetados
    st.subheader(f"Total de Mortes por Categoria nos Estados Mais Afetados (com mais de {min_deaths_obito} mortes):")
    st.write(most_affected_states_combined)

    # Gráfico de linha para o total de mortes por categoria nos estados mais afetados
    st.header("Total de Mortes por Categoria (Ordenado de Maior para Menor) nos Estados Mais Afetados:")
    most_affected_states_sorted_combined = most_affected_states_combined.sort_values(by='new_deaths_total_2020', ascending=False)
    fig_line_combined = px.line(x=most_affected_states_sorted_combined['state'], y=most_affected_states_sorted_combined['new_deaths_total_2020'], markers=True)
    st.plotly_chart(fig_line_combined)

except KeyError as e:
    st.error(f"Erro ao acessar colunas: {e}")