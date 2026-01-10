import streamlit as st

# 1. Configuração da Página
st.set_page_config(page_title="Top Ofertas - Oficial", page_icon="🛍️", layout="wide")

# 2. Design Profissional (CSS)
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
        padding: 15px;
        border: 1px solid #333;
        border-radius: 15px;
        margin-bottom: 25px;
        background-color: #111;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Cabeçalho
st.title("🛍️ Top Ofertas")
st.write("<p style='text-align: center;'>As melhores ofertas com pagamento na entrega!</p>", unsafe_allow_html=True)

# 4. Lista de Produtos (Adicione mais aqui seguindo o modelo)
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

# 5. Vitrine em Grade (3 colunas)
cols = st.columns(3)

for i, produto in enumerate(produtos):
    with cols[i % 3]: 
        st.markdown('<div class="produto-container">', unsafe_allow_html=True)
        st.image(produto["imagem"], width=200)
        st.write(f"**{produto['nome']}**")
        st.write(f"### R$ {produto['preco']:.2f}")
        
        if st.button(f"COMPRAR AGORA", key=f"btn_{i}"):
            st.success("A abrir checkout...")
            st.markdown(f"**[CLIQUE AQUI PARA FINALIZAR]({produto['link']})**")
        st.markdown('</div>', unsafe_allow_html=True)

# 6. Suporte via WhatsApp na Barra Lateral
st.sidebar.title("Top Ofertas")
st.sidebar.write("---")
st.sidebar.write("### Precisa de ajuda?")

# COLOQUE SEU NÚMERO ABAIXO (Ex: 55 + DDD + Numero)
meu_whatsapp = "5547997270179" 
link_whatsapp = f"https://wa.me/{meu_whatsapp}?text=Olá! Estava na loja Top Ofertas e gostaria de tirar uma dúvida."

st.sidebar.markdown(f"""
    <a href="{link_whatsapp}" target="_blank">
        <button style="width:100%; border-radius:10px; background-color:#25D366; color:white; font-weight:bold; border:none; height:45px; cursor:pointer;">
            Falar no WhatsApp 💬
        </button>
    </a>
""", unsafe_allow_html=True)