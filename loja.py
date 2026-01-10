import streamlit as st

# 1. CSS e Persuasão
st.set_page_config(page_title="Top Ofertas | Tendências 2026", page_icon="🦊", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; }
    
    /* Banner de Categoria Estilizado */
    .trend-banner {
        background: linear-gradient(135deg, #1a1a1a 0%, #444 100%);
        color: #FF8C00; padding: 20px; border-radius: 15px;
        margin: 20px 0; text-align: center; border: 1px solid #FF8C00;
    }
    
    /* Badge de "Tendência 2026" */
    .badge-trend {
        background: #FF8C00; color: white; padding: 2px 8px;
        border-radius: 5px; font-size: 10px; font-weight: bold;
        display: inline-block; margin-bottom: 10px;
    }

    .header-top {
        background: #FF8C00; padding: 15px 10%;
        display: flex; align-items: center; justify-content: space-between;
        margin: -6rem -5rem 20px -5rem; color: white;
    }
    </style>
""", unsafe_allow_html=True)

# 2. Banco de Dados com Novos Nichos
produtos = {
    "massageador": {
        "nome": "Massageador Cervical Inteligente Pro 2026",
        "preco_antigo": "249,00", "preco": "137,90",
        "img": "https://m.media-amazon.com/images/I/61K9UqL8T9L._AC_SL1500_.jpg",
        "categoria": "Saúde Tech",
        "link": "#"
    },
    "pet_cam": {
        "nome": "Alimentador Inteligente com Câmera WiFi",
        "preco_antigo": "499,00", "preco": "297,50",
        "img": "https://m.media-amazon.com/images/I/51u98Iq9S1L._AC_SL1000_.jpg",
        "categoria": "Pet Care",
        "link": "#"
    }
}

# 3. Cabeçalho
st.markdown('<div class="header-top"><h1>🦊 Top Ofertas</h1><span>🔥 Tendências 2026</span></div>', unsafe_allow_html=True)

# Lógica simples de exibição
tab1, tab2 = st.tabs(["🚀 LANÇAMENTOS 2026", "🏠 MAIS VENDIDOS"])

with tab1:
    st.markdown("""
        <div class="trend-banner">
            <h2 style="margin:0;">OPORTUNIDADE: Nichos que mais faturam em 2026</h2>
            <p style="color:white;">Produtos testados com alta taxa de conversão no TikTok e Instagram Ads.</p>
        </div>
    """, unsafe_allow_html=True)
    
    c1, c2 = st.columns(2)
    
    with c1:
        st.markdown('<div class="badge-trend">NICHO: SAÚDE & BEM-ESTAR</div>', unsafe_allow_html=True)
        p = produtos["massageador"]
        st.image(p["img"], width=250)
        st.subheader(p["nome"])
        st.markdown(f"~~De R$ {p['preco_antigo']}~~ por **R$ {p['preco']}**")
        st.button("ADICIONAR AO ESTOQUE", key="m1")

    with c2:
        st.markdown('<div class="badge-trend">NICHO: PET TECH</div>', unsafe_allow_html=True)
        p = produtos["pet_cam"]
        st.image(p["img"], width=250)
        st.subheader(p["nome"])
        st.markdown(f"~~De R$ {p['preco_antigo']}~~ por **R$ {p['preco']}**")
        st.button("ADICIONAR AO ESTOQUE", key="p1")

with tab2:
    st.write("Aqui ficam seus produtos atuais (Cinta, Depilador)...")

# --- RODAPÉ ---
st.markdown("""
    <div style="background:#f4f4f4; padding:20px; text-align:center; border-radius:10px; margin-top:30px;">
        <h4>💡 Dica de Mestre para Lucrar:</h4>
        <p>Em 2026, o cliente não quer apenas 'preço'. Ele quer 'tempo'. <br>
        Venda produtos que <b>economizam tempo</b> ou <b>melhoram o sono</b>. Esses são os dois maiores desejos da década.</p>
    </div>
""", unsafe_allow_html=True)