import streamlit as st

# Configuração da página do seu site
st.set_page_config(page_title="Minha Loja Logzz", page_icon="🛍️")

st.title("🚀 Minha Vitrine de Produtos")
st.write("Escolha seu produto e pague apenas no recebimento (Cash on Delivery)!")

# Aqui é onde você vai colocar seus produtos da Logzz depois
produtos = [
    {    "nome": "Cinta colete modeladora", 
        "preco": 99.99, 
        "link": "https://entrega.logzz.com.br/pay/mem6qq3rw/vlqxc-1-unidade",
        "imagem": "https://logzz-s3.s3.us-east-2.amazonaws.com/uploads/files/products/20240714-131356prok2m05.jpg" # Adicione o link da foto aqui
    }
]


# Criando a vitrine organizada
col1, col2, col3 = st.columns(3)

for i, produto in enumerate(produtos):
    with [col1, col2, col3][i % 3]:
        st.image(produto["imagem"], use_container_width=True)
        st.subheader(produto["nome"])
        st.write(f"**R$ {produto['preco']:.2f}**")
        if st.button(f"Comprar {produto['nome']}", key=i):
            st.success("Redirecionando para o checkout...")
            st.write(f"Link de destino: {produto['link']}")

st.sidebar.markdown("---")
st.sidebar.write("📱 **Suporte via WhatsApp**")
if st.sidebar.button("Falar com Atendente"):
    st.sidebar.write("Abrindo conversa...")

# Adicionando Suporte no Menu Lateral (Sidebar)
st.sidebar.markdown("---") # Linha divisória
st.sidebar.subheader("Precisa de ajuda? 💬")

# Substitua o número abaixo pelo SEU número (DDI + DDD + Número)
# Exemplo para Brasil: 55 + DDD + Número
meu_numero = "5571992934052" 
mensagem_padrao = "Olá! Gostaria de da falar com atendente."

# Link gerador de conversa
link_whatsapp = f"https://wa.me/{meu_numero}?text={mensagem_padrao.replace(' ', '%20')}"

# Adicionei o parâmetro key="btn_whatsapp" para torná-lo único
if st.sidebar.button("Falar com Atendente", key="btn_whatsapp"):
    st.sidebar.markdown(f"[✅ Clique aqui para abrir o WhatsApp]({link_whatsapp})")