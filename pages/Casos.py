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

# Mapa dos estados mais afetados no Brasil (óbito)
st.header("Mapa dos Estados Mais Afetados no Brasil (óbito):")
# Agrupar por estado e contar o número total de casos
total_cases_by_state_obito = df_obito.groupby('state').size().reset_index(name='Total Cases (óbito)')

# Agrupar por estado e somar o número total de mortes (óbito)
total_deaths_by_state_obito = df_obito.groupby('state')[[
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

# Adicionar cores ao mapa com base no número de mortes (óbito)
fig_map_obito = px.choropleth(total_cases_by_state_obito,
                              locations='state',
                              locationmode='ISO-3',
                              color=total_deaths_by_state_obito['new_deaths_total_2020'],
                              color_continuous_scale='reds',
                              title='Estados Mais Afetados no Brasil (óbito)',
                              labels={'Total Cases (óbito)': 'Número de Casos (óbito)', 'color': 'Número de Mortes (óbito)'},
                              scope='south america'
                              )
# Atualizar o layout do mapa para exibir o Brasil
fig_map_obito.update_geos(projection_type="natural earth", showcoastlines=True, coastlinecolor="black")

# Adicionar as informações de mortes no final do mapa (óbito)
try:
    # Adicionar o total de mortes (óbito) como uma anotação no mapa
    fig_map_obito.add_annotation(
        x=0.5,
        y=-0.1,
        text=f'Total de Mortes (óbito): {total_deaths_by_state_obito["new_deaths_total_2020"].sum()}',
        showarrow=False,
        font=dict(size=12)
    )

    # Exibir o mapa (óbito)
    st.plotly_chart(fig_map_obito)

    # Filtrar os estados mais afetados com base no número mínimo de mortes escolhido pelo usuário (óbito)
    most_affected_states_obito = total_deaths_by_state_obito[total_deaths_by_state_obito['new_deaths_total_2020'] >= min_deaths_obito]

    # Exibir informações de mortes para os estados mais afetados (óbito)
    st.subheader(f"Total de Mortes por Categoria nos Estados Mais Afetados (com mais de {min_deaths_obito} mortes) (óbito):")
    st.write(most_affected_states_obito)

    # Gráfico de linha para o total de mortes por categoria nos estados mais afetados (óbito)
    st.header("Total de Mortes por Categoria (Ordenado de Maior para Menor) nos Estados Mais Afetados (óbito):")
    most_affected_states_sorted_obito = most_affected_states_obito.sort_values(by='new_deaths_total_2020', ascending=False)
    fig_line_obito = px.line(x=most_affected_states_sorted_obito.index, y=most_affected_states_sorted_obito['new_deaths_total_2020'], markers=True)
    st.plotly_chart(fig_line_obito)

except KeyError as e:
    st.error(f"Erro ao acessar colunas (óbito): {e}")

# Mapa dos estados mais afetados no Brasil (boletim)
st.header("Mapa dos Estados Mais Afetados no Brasil (boletim):")
# Agrupar por estado e contar o número total de casos no boletim
total_cases_by_state_boletim = df_boletim.groupby('state').size().reset_index(name='Total Cases (boletim)')

# Agrupar por estado e somar o número total de mortes no boletim
total_deaths_by_state_boletim = df_boletim.groupby('state')[[
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

# Adicionar cores ao mapa com base no número de mortes no boletim
fig_map_boletim = px.choropleth(total_cases_by_state_boletim,
                                locations='state',
                                locationmode='ISO-3',
                                color=total_deaths_by_state_boletim['new_deaths_total_2020'],
                                color_continuous_scale='reds',
                                title='Estados Mais Afetados no Brasil (boletim)',
                                labels={'Total Cases (boletim)': 'Número de Casos (boletim)', 'color': 'Número de Mortes (boletim)'},
                                scope='south america'
                                )
# Atualizar o layout do mapa para exibir o Brasil
fig_map_boletim.update_geos(projection_type="natural earth", showcoastlines=True, coastlinecolor="black")

# Adicionar as informações de mortes no final do mapa (boletim)
try:
    # Adicionar o total de mortes (boletim) como uma anotação no mapa
    fig_map_boletim.add_annotation(
        x=0.5,
        y=-0.1,
        text=f'Total de Mortes (boletim): {total_deaths_by_state_boletim["new_deaths_total_2020"].sum()}',
        showarrow=False,
        font=dict(size=12)
    )

    # Exibir o mapa (boletim)
    st.plotly_chart(fig_map_boletim)

    # Filtrar os estados mais afetados com base no número mínimo de mortes escolhido pelo usuário
    most_affected_states = total_deaths_by_state[total_deaths_by_state['new_deaths_total_2020'] >= min_deaths]

    # Exibir informações de mortes para os estados mais afetados
    st.subheader(f"Total de Mortes por Categoria nos Estados Mais Afetados (com mais de {min_deaths} mortes):")
    st.write(most_affected_states)

    # Gráfico de linha para o total de mortes por categoria nos estados mais afetados
    st.header("Total de Mortes por Categoria (Ordenado de Maior para Menor) nos Estados Mais Afetados:")
    most_affected_states_sorted = most_affected_states.sort_values(by='new_deaths_total_2020', ascending=False)
    fig_line = px.line(x=most_affected_states_sorted.index, y=most_affected_states_sorted['new_deaths_total_2020'], markers=True)
    st.plotly_chart(fig_line)

except KeyError as e:
    st.error(f"Erro ao acessar colunas: {e}")