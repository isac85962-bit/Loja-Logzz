import streamlit as st

# 1. Configuração da Página
st.set_page_config(page_title="Top Ofertas - Oficial", page_icon="🛍️", layout="wide")

# 2. Estilo Visual (CSS)
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        background-color: #FF8C00;
        color: white;
        font-weight: bold;
        border: none;
        height: 40px;
    }
    .stButton>button:hover {
        background-color: #FFA500;
        color: black;
    }
    h1 {
        color: #FF8C00;
        text-align: center;
    }
    .produto-container {
        text-align: center;
        padding: 10px;
        border: 1px solid #333;
        border-radius: 15px;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Cabeçalho
st.title("🛍️ Top ofertas")
st.write("<p style='text-align: center;'>As melhores ofertas com pagamento na entrega!</p>", unsafe_allow_html=True)

# 4. Lista de Produtos
produtos = [
    {
        "nome": "Cinta Colete Modeladora", 
        "preco": 99.99, 
        "link": "https://entrega.logzz.com.br/pay/mem6qq3rw/vlqxc-1-unidade",
        "imagem": "https://logzz-s3.s3.us-east-2.amazonaws.com/uploads/files/products/20240714-131356prok2m05.jpg"
    },
    {
        "nome": "Depilador SkinLiss", 
        "preco": 99.99, 
        "link": "https://entrega.logzz.com.br/pay/mem0go36g/azjol-skinliss-9999",
        "imagem": "https://a-static.mlcdn.com.br/470x352/depilador-yes-finishing-touch-sem-fio-ativacao-sensor-de-luz-rosto-e-corpo-depiladorlaser/connectcellcomercio/depiladorroxo16/958b6b6bada9045715419c0988f0a3b6.jpeg"
    }
]

# 5. Vitrine em 3 Colunas
cols = st.columns(3)

for i, produto in enumerate(produtos):
    with cols[i % 3]: # Isso distribui os produtos entre as 3 colunas
        st.markdown('<div class="produto-container">', unsafe_allow_html=True)
        
        # Imagem menor e centralizada
        st.image(produto["imagem"], width=200)
        
        st.write(f"**{produto['nome']}**")
        st.write(f"### R$ {produto['preco']:.2f}")
        
        if st.button(f"COMPRAR AGORA", key=f"btn_{i}"):
            st.success("A abrir checkout...")
            st.markdown(f"**[CLIQUE AQUI PARA FINALIZAR]({produto['link']})**")
        
        st.markdown('</div>', unsafe_allow_html=True)

# 6. Rodapé Lateral
st.sidebar.title("Top Ofertas")
st.sidebar.info("Dúvidas? Entre em contato com o nosso suporte.")