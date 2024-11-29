import streamlit as st
import requests

def busca_cep(cep):
    resposta=requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    return resposta


st.set_page_config(page_title="Busca_Cep",page_icon="🔗")

st.title("Sistema de busca CeP")
st.divider()


menu=st.sidebar
cep=menu.text_input("Digite o CEP:")
botao=menu.button("Pesquisar")

if botao:
    resposta=busca_cep(cep)

    if resposta.status_code==200:
        st.success("CEP encontrado",icon="✔")
        dados=resposta.json()

        col1,col2=st.columns(2)


        col1.markdown(f"**Cep:**{dados['cep']}")
        col1.markdown(f"**Logradouro:**{dados['logradouro']}")
        col1.markdown(f"**Complemento:**{dados['complemento']}")
        col1.markdown(f"**unidade:**{dados['unidade']}")
        col1.markdown(f"**bairro:**{dados['bairro']}")
        col1.markdown(f"**localidade:**{dados['localidade']}")
        col2.markdown(f"**UF:**{dados['uf']}")
        col2.markdown(f"**estado:**{dados['estado']}")
        col2.markdown(f"**Região:**{dados['regiao']}")
        col2.markdown(f"**Codigo IBGE:**{dados['ibge']}")
        col2.markdown(f"**Gia:**{dados['gia']}")
        col2.markdown(f"**DDD:**{dados['ddd']}")
        col2.markdown(f"**Siafi:**{dados['siafi']}")
        st.balloons()
    else:
        st.error("Seu CEP informado é invalido!",icon="❌")



        