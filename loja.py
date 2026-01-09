import streamlit as st

# 1. Configuração da Página (Identidade da Empresa)
st.set_page_config(page_title="Top Ofertas - Oficial", page_icon="🛍️", layout="wide")

# 2. Cores da Top Ofertas (Design Profissional)
st.markdown("""
    <style>
    /* Cor do fundo e dos botões */
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        background-color: #FF8C00; /* Laranja da sua logo */
        color: white;
        font-weight: bold;
        border: none;
        height: 50px;
        font-size: 18px;
    }
    /* Efeito ao passar o mouse */
    .stButton>button:hover {
        background-color: #FFA500;
        color: black;
    }
    /* Deixar o título mais bonito */
    h1 {
        color: #FF8C00;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Cabeçalho
st.title("🛍️ Top Ofertas")
st.write("<p style='text-align: center;'>As melhores ofertas com pagamento na entrega (Cash on Delivery)!</p>", unsafe_allow_html=True)

# 4. Teu Produto (Ajustado com a foto que você já tem)
produtos = [
    {
        "nome": "Cinta Colete Modeladora", 
        "preco": 99.99, 
        "link": "https://entrega.logzz.com.br/pay/mem6qq3rw/vlqxc-1-unidade",
        "imagem": "https://logzz-s3.s3.us-east-2.amazonaws.com/uploads/files/products/20240714-131356prok2m05.jpg"
    }
]

# 5. Criando a Vitrine
col1, col2, col3 = st.columns(3)

for i, produto in enumerate(produtos):
    with col1: # Como você tem 1 produto, vamos focar na primeira coluna
        st.image(produto["imagem"], use_container_width=True)
        st.subheader(produto["nome"])
        st.write(f"### R$ {produto['preco']:.2f}")
        
        if st.button(f"COMPRAR AGORA", key=i):
            st.success("A abrir checkout seguro...")
            st.markdown(f"**[CLIQUE AQUI PARA FINALIZAR PEDIDO]({produto['link']})**")

# 6. Botão de Suporte no Menu Lateral
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3081/3081559.png", width=100) # Ícone de loja
st.sidebar.title("Top Ofertas")
if st.sidebar.button("Falar com Atendente 💬", key="suporte"):
    st.sidebar.info("A abrir o WhatsApp de suporte...")