import streamlit as st

# 1. Configuração e Estilo
st.set_page_config(page_title="Top Ofertas - Oficial", page_icon="🛍️", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #f5f5f5; color: #333333; }
    
    /* Cabeçalho Amarelo */
    .main-header {
        background-color: #FFF159;
        padding: 15px 5%;
        margin: -6rem -5rem 2rem -5rem;
        text-align: center;
    }
    
    /* Card de Produto */
    .card-resumo {
        background-color: white;
        padding: 15px;
        border-radius: 8px;
        border: 1px solid #eeeeee;
        text-align: center;
        margin-bottom: 10px;
        transition: 0.3s;
    }
    .card-resumo:hover {
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
    }
    
    /* Ajuste do botão para parecer parte do clique */
    .stButton>button {
        background-color: #3483fa !important;
        color: white !important;
        border-radius: 6px !important;
        width: 100%;
        border: none;
    }
    </style>
""", unsafe_allow_html=True)

# 2. Banco de Dados
produtos = {
    "cinta": {
        "nome": "Cinta Colete Modeladora Ampla Carmigras",
        "preco": "99,90",
        "img": "https://logzz-s3.s3.us-east-2.amazonaws.com/uploads/files/products/20240714-131356prok2m05.jpg",
        "link": "https://entrega.logzz.com.br/pay/mem6qq3rw/vlqxc-1-unidade",
        "regioes": ["SC", "SP", "PR"],
        "desc": "Modela sua cintura e melhora a postura instantaneamente.",
        "especificacoes": ["Material: Neoprene Premium", "Ajuste Duplo", "Unissex"]
    },
    "depilador": {
        "nome": "Depilador SkinLiss - Finishing Touch",
        "preco": "89,90",
        "img": "https://a-static.mlcdn.com.br/470x352/depilador-yes-finishing-touch-sem-fio-ativacao-sensor-de-luz-rosto-e-corpo-depiladorlaser/connectcellcomercio/depiladorroxo16/958b6b6bada9045715419c0988f0a3b6.jpeg",
        "link": "https://entrega.logzz.com.br/pay/mem0go36g/azjol-skinliss-9999",
        "regioes": ["SP", "RJ", "MG"],
        "desc": "Depilação sem dor com tecnologia de micro-oscilação.",
        "especificacoes": ["Recarregável USB", "Luz LED", "Hipoalergênico"]
    }
}

# 3. Navegação
if 'detalhe' not in st.session_state:
    st.session_state.detalhe = None

st.markdown('<div class="main-header"><h2 style="color:#2d3277; margin:0;">Top Ofertas - Oficial</h2></div>', unsafe_allow_html=True)

# --- VISÃO: DETALHES ---
if st.session_state.detalhe:
    p = produtos[st.session_state.detalhe]
    if st.button("⬅️ Voltar para a vitrine"):
        st.session_state.detalhe = None
        st.rerun()

    col1, col2 = st.columns([1, 1])
    with col1: st.image(p["img"], use_container_width=True)
    with col2:
        st.title(p["nome"])
        st.write(f"### R$ {p['preco']}")
        st.write("---")
        cep = st.text_input("📍 Informe seu CEP para verificar estoque:", placeholder="00000-000")
        if cep:
            st.success("✅ Disponível para entrega em 24h!")
            st.link_button("FECHAR PEDIDO (PAGAR NA ENTREGA)", p["link"])
        st.subheader("Descrição")
        st.write(p["desc"])

# --- VISÃO: VITRINE ---
else:
    # Banner
    st.image("https://images.tcdn.com.br/img/editor/up/649983/Banner_Topo_Desktop_1.jpg", use_container_width=True)
    
    st.subheader("Ofertas em Destaque")
    cols = st.columns(4)
    
    for idx, (id_p, p) in enumerate(produtos.items()):
        with cols[idx]:
            # O TRUQUE: Envolver a imagem e o botão em uma lógica de clique
            st.markdown(f'<div class="card-resumo">', unsafe_allow_html=True)
            st.image(p["img"], use_container_width=True)
            st.write(f"**{p['nome']}**")
            st.write(f"R$ {p['preco']}")
            
            # O botão funciona como o gatilho principal
            if st.button("Ver Detalhes", key=f"btn_{id_p}"):
                st.session_state.detalhe = id_p
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)