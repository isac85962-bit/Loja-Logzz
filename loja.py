import streamlit as st

# 1. Configuração de Página
st.set_page_config(page_title="Top Ofertas - Oficial", page_icon="🦊", layout="wide")

# 2. Interface Visual (CSS) - Ajustado para cores Laranja/Amarelo
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; color: #333333; }
    
    /* Barra Superior Compacta */
    .top-bar {
        background-color: #FF8C00; 
        padding: 5px 2%;
        display: flex;
        align-items: center;
        justify-content: space-between;
        color: white;
        margin: -6rem -5rem 1rem -5rem;
    }
    
    /* Banner Estilo Mercado Livre */
    .hero-banner {
        background: linear-gradient(90deg, #FFD700 0%, #FF8C00 100%);
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        color: #000;
        margin-bottom: 20px;
        font-weight: bold;
    }

    /* Card de Produto */
    .card-produto {
        background: white;
        border-radius: 10px;
        padding: 15px;
        border: 1px solid #e0e0e0;
        text-align: center;
        transition: 0.3s;
    }
    .card-produto:hover {
        box-shadow: 0 8px 16px rgba(0,0,0,0.1);
        border-color: #FF8C00;
    }

    /* Botões */
    .stButton>button {
        background-color: #FF8C00 !important;
        color: white !important;
        border-radius: 8px !important;
        width: 100%;
        border: none;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# 3. BANCO DE DADOS (ÁREA DE EDIÇÃO)
# Para adicionar mais produtos, basta copiar um bloco inteiro e mudar as informações
produtos = {
    "cinta": {
        "nome": "Cinta Colete Modeladora Premium",
        "preco": "99,90",
        "img": "https://logzz-s3.s3.us-east-2.amazonaws.com/uploads/files/products/20240714-131356prok2m05.jpg",
        "link": "https://entrega.logzz.com.br/pay/mem6qq3rw/vlqxc-1-unidade",
        "descricao": "Nossa Cinta Colete é feita com tecnologia de alta compressão que não enrola.",
        "caracteristicas": ["✅ Material Respirável", "✅ Ajuste Duplo", "✅ Invisível sob a roupa"]
    },
    "depilador": {
        "nome": "Depilador SkinLiss Finishing Touch",
        "preco": "89,90",
        "img": "https://a-static.mlcdn.com.br/470x352/depilador-yes-finishing-touch-sem-fio-ativacao-sensor-de-luz-rosto-e-corpo-depiladorlaser/connectcellcomercio/depiladorroxo16/958b6b6bada9045715419c0988f0a3b6.jpeg",
        "link": "https://entrega.logzz.com.br/pay/mem0go36g/azjol-skinliss-9999",
        "descricao": "Remova pelos instantaneamente e sem dor com o SkinLiss Pro.",
        "caracteristicas": ["✅ Tecnologia de Micro-oscilação", "✅ Bateria Recarregável", "✅ Para peles sensíveis"]
    }
}

# 4. Lógica de Navegação
if 'pagina' not in st.session_state: st.session_state.pagina = 'home'

# Cabeçalho Compacto com Mascote
st.markdown(f"""
    <div class="top-bar">
        <div style="display:flex; align-items:center; gap:10px;">
            <img src="https://raw.githubusercontent.com/isac85962-bit/Loja-Logzz/main/WhatsApp%20Image%202026-01-09%20at%2017.29.39.jpeg" width="40" style="border-radius:50%;">
            <h3 style="margin:0; color:white;">TOP OFERTAS</h3>
        </div>
        <div style="font-size:14px;">🚚 Pagamento na Entrega</div>
    </div>
""", unsafe_allow_html=True)

# --- PÁGINA: DETALHES ---
if st.session_state.pagina != 'home':
    p = produtos[st.session_state.pagina]
    if st.button("⬅️ VOLTAR PARA A LOJA"):
        st.session_state.pagina = 'home'
        st.rerun()
    
    col1, col2 = st.columns([1, 1.2])
    with col1: st.image(p["img"], use_container_width=True)
    with col2:
        st.title(p["nome"])
        st.markdown(f"<h2 style='color:#FF8C00;'>R$ {p['preco']}</h2>", unsafe_allow_html=True)
        st.write("---")
        cep = st.text_input("📍 Informe seu CEP para entrega rápida:")
        if cep:
            st.success("✅ DISPONÍVEL! Receba amanhã e pague na porta.")
            st.link_button("FECHAR PEDIDO AGORA", p["link"])
        st.write(f"### Descrição\n{p['descricao']}")
        for c in p['caracteristicas']: st.write(c)

# --- PÁGINA: HOME ---
else:
    # Banner
    st.markdown('<div class="hero-banner">⚡ PROMOÇÕES EXCLUSIVAS: FRETE GRÁTIS E PAGAMENTO NA ENTREGA 🦊</div>', unsafe_allow_html=True)
    
    cols = st.columns(4)
    for idx, (id_p, p) in enumerate(produtos.items()):
        with cols[idx]:
            st.markdown(f"""
                <div class="card-produto">
                    <img src="{p['img']}" style="width:100%; border-radius:8px;">
                    <p style="margin-top:10px; font-weight:bold; color:#333;">{p['nome']}</p>
                    <p style="color:#FF8C00; font-size:20px; font-weight:bold;">R$ {p['preco']}</p>
                </div>
            """, unsafe_allow_html=True)
            if st.button("Ver Detalhes", key=id_p):
                st.session_state.pagina = id_p
                st.rerun()