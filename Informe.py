import streamlit as st

# Criar um aplicativo Streamlit
st.title("Análise de Óbitos por COVID-19")

# Página de Apresentação
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