import streamlit as st
from controller.livro_controller import cadastrar_livros, obter_livros
from dados.database import criar_tabela
from controller.usuario_controller import cadastrar_usuario, obter_usuarios

# Criar tabela na inicialização
criar_tabela()

st.title("Cadastro de Livros")

# Formuláio
st.subheader("Adicionar novo livro")
with st.form("form_livro"):
    isbn = st.text_input("ISBN")
    titulo = st.text_input("Titulo")
    submitted = st.form_submit_button("Cadastrar")

    if submitted:
        mensagem = cadastrar_livros(isbn, titulo)
        st.success(mensagem)

# Listagem
st.subheader("Livros cadastrados")
livros = obter_livros()

if livros:
    for i in livros:
        st.write(f"**ISBN:** {i[0]} | **Título:** {i[1]}")
else:
    st.info("Nenhum livro cadastrado ainda.")
    
# Cadastro de usuários
st.subheader("Adicionar novo usuário")
with st.form("form_usuario"):
    cpf = st.text_input("CPF")
    nome = st.text_input("Nome")
    submitted_usuario = st.form_submit_button("Cadastrar Usuário")
    
    if submitted_usuario:
        mensagem = cadastrar_usuario(cpf, nome)
        st.success(mensagem)
    
# Listagem de usuários
st.subheader("Usuários cadastrados")
usuarios = obter_usuarios()

if usuarios:
    for u in usuarios:
        st.write(f"**CPF:** {u[0]} | **Nome:** {u[1]}")
else:
    st.info("Nenhum usuário cadastrado ainda.")