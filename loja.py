import streamlit as st

# 1. Configuração de Alta Fidelidade
st.set_page_config(page_title="Top Ofertas - Oficial", page_icon="🛍️", layout="wide")

# 2. CSS AVANÇADO - Quebrando barreiras visuais
st.markdown("""
    <style>
    /* Remove as margens pretas deselegantes do Streamlit */
    .block-container { padding-top: 0rem; padding-bottom: 0rem; max-width: 100%; }
    [data-testid="stHeader"] { background: rgba(0,0,0,0); }
    
    /* Cabeçalho Laranja Top Ofertas */
    .top-bar {
        background-color: #FF8C00; 
        padding: 15px 5%;
        display: flex;
        align-items: center;
        justify-content: space-between;
        color: white;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }
    
    /* Card de Produto Profissional */
    .card-produto {
        background: white;
        border-radius: 12px;
        padding: 20px;
        border: 1px solid #e0e0e0;
        transition: 0.3s ease;
        text-align: center;
        margin-bottom: 20px;
        cursor: pointer;
    }
    .card-produto:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        border-color: #FF8C00;
    }
    
    /* Banner Estilo Mercado Livre */
    .main-banner {
        background: linear-gradient(135deg, #FF8C00 0%, #FFA500 100%);
        color: white;
        padding: 50px;
        border-radius: 20px;
        text-align: center;
        margin: 20px 0;
    }
    </style>
""", unsafe_allow_html=True)

# 3. BANCO DE DADOS EDITÁVEL - Edite aqui as descrições!
# Adicione quantas linhas quiser entre as aspas triplas ('''descrição''')
produtos = {
    "cinta": {
        "nome": "Cinta Colete Modeladora Premium",
        "preco": "99,90",
        "img": "https://logzz-s3.s3.us-east-2.amazonaws.com/uploads/files/products/20240714-131356prok2m05.jpg",
        "link": "https://entrega.logzz.com.br/pay/mem6qq3rw/vlqxc-1-unidade",
        "desc_longa": """
            ### 💎 Benefícios Exclusivos:
            * Melhora a postura instantaneamente.
            * Reduz até 3 números do seu manequim.
            * Tecido inteligente que não enrola e deixa a pele respirar.
            * Ideal para pós-parto e uso diário.
        """
    },
    "depilador": {
        "nome": "Depilador SkinLiss Finishing Touch",
        "preco": "89,90",
        "img": "https://a-static.mlcdn.com.br/470x352/depilador-yes-finishing-touch-sem-fio-ativacao-sensor-de-luz-rosto-e-corpo-depiladorlaser/connectcellcomercio/depiladorroxo16/958b6b6bada9045715419c0988f0a3b6.jpeg",
        "link": "https://entrega.logzz.com.br/pay/mem0go36g/azjol-skinliss-9999",
        "desc_longa": """
            ### ✨ Por que escolher o SkinLiss:
            * Tecnologia de micro-oscilação: remove pelos sem dor.
            * Sensor de luz que ativa apenas em contato com a pele.
            * Recarregável USB - use em qualquer lugar.
            * Recomendado por dermatologistas para peles sensíveis.
        """
    }
}

# 4. Interface
if 'detalhe' not in st.session_state: st.session_state.detalhe = None

# Cabeçalho com Mascote (Simulado por emoji por enquanto)
st.markdown("""
    <div class="top-bar">
        <div style="display:flex; align-items:center; gap:15px;">
            <span style="font-size:30px;">🦊</span> 
            <h2 style="margin:0; color:white;">TOP OFERTAS</h2>
        </div>
        <div style="font-weight:bold;">Pagamento na Entrega 🚚</div>
    </div>
""", unsafe_allow_html=True)

if st.session_state.detalhe:
    p = produtos[st.session_state.detalhe]
    if st.button("⬅️ Voltar para a Loja"):
        st.session_state.detalhe = None
        st.rerun()
    
    col1, col2 = st.columns([1, 1.2])
    with col1: st.image(p["img"], use_container_width=True)
    with col2:
        st.title(p["nome"])
        st.markdown(f"<h2 style='color:#FF8C00;'>R$ {p['preco']}</h2>", unsafe_allow_html=True)
        cep = st.text_input("📍 Informe seu CEP para entrega rápida")
        if cep:
            st.success("✅ Estoque disponível! Receba amanhã.")
            st.link_button("FECHAR PEDIDO NO WHATSAPP", p["link"])
        st.markdown(p["desc_longa"])

else:
    # Banner Profissional
    st.markdown("""
        <div class="main-banner">
            <h1>OFERTAS BLACK OUT ⚡</h1>
            <p>Frete Grátis e Pagamento na Porta para todo o Brasil!</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.subheader("🔥 Mais Vendidos")
    cols = st.columns(4)
    for idx, (id_p, p) in enumerate(produtos.items()):
        with cols[idx]:
            # Div que permite clique visual
            st.markdown(f"""
                <div class="card-produto">
                    <img src="{p['img']}" style="width:100%; border-radius:8px;">
                    <h4 style="color:#333;">{p['nome']}</h4>
                    <p style="color:#FF8C00; font-size:22px; font-weight:bold;">R$ {p['preco']}</p>
                </div>
            """, unsafe_allow_html=True)
            if st.button(f"Ver Detalhes", key=id_p):
                st.session_state.detalhe = id_p
                st.rerun()