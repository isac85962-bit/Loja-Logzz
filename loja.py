import streamlit as st

# 1. Design & Persuasão Visual
st.set_page_config(page_title="Top Ofertas | Oficial", page_icon="🦊", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; }
    .block-container { padding-top: 0rem; }

    /* Header Slim Profissional */
    .header-top {
        background: linear-gradient(90deg, #FF8C00, #FFA500);
        padding: 15px 10%;
        display: flex; align-items: center; justify-content: space-between;
        margin: -6rem -5rem 0 -5rem;
        color: white; box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }

    /* Gatilho de Urgência Realista */
    .urgency-banner {
        background: #000; color: #00FF00;
        text-align: center; padding: 8px; font-size: 14px;
        margin: 0 -5rem 20px -5rem; font-weight: bold;
        letter-spacing: 1px;
    }

    /* Card de Produto Otimizado */
    .product-card {
        background: white; border: 1px solid #F0F0F0;
        border-radius: 15px; padding: 20px; transition: 0.4s;
        text-align: center; height: 100%;
    }
    .product-card:hover { transform: translateY(-10px); border-color: #FF8C00; box-shadow: 0 15px 30px rgba(255,140,0,0.1); }
    
    .price-now { color: #FF8C00; font-size: 28px; font-weight: 900; }
    .price-before { color: #BBB; text-decoration: line-through; font-size: 14px; }

    /* Botão de Chamada para Ação (CTA) */
    .stButton > button {
        background: #FF8C00 !important; color: white !important;
        border-radius: 10px !important; font-weight: 800 !important;
        font-size: 18px !important; height: 55px; border: none; width: 100%;
        box-shadow: 0 4px 15px rgba(255,140,0,0.3);
    }
    </style>
""", unsafe_allow_html=True)

# 2. BANCO DE DADOS COM COPY AIDA
produtos = {
    "cinta": {
        "nome": "Cinta Modeladora Ultra-Shaper Premium",
        "tagline": "Atenção: Recupere sua silhueta e sua confiança em segundos!",
        "preco_antigo": "197,90", "preco": "97,90",
        "img": "https://logzz-s3.s3.us-east-2.amazonaws.com/uploads/files/products/20240714-131356prok2m05.jpg",
        "link": "https://entrega.logzz.com.br/pay/mem6qq3rw/vlqxc-1-unidade",
        "copy_aida": """
            **Por que você precisa disso hoje?**
            * **🔥 INTERESSE:** Diferente das cintas comuns que enrolam e machucam, nossa tecnologia *Soft-Touch* molda seu corpo sem tirar o fôlego.
            * **✨ DESEJO:** Imagine-se vestindo aquela roupa que está guardada há meses. Sinta-se poderosa, com a postura alinhada e medidas reduzidas instantaneamente.
            * **⚡ AÇÃO:** Estoque limitado para a promoção de verão. Garanta a sua com Frete Grátis!
        """
    },
    "depilador": {
        "nome": "Depilador Laser-Light SkinLiss 2026",
        "tagline": "Chega de sofrer com ceras e giletes que escurecem sua pele!",
        "preco_antigo": "159,00", "preco": "84,90",
        "img": "https://a-static.mlcdn.com.br/470x352/depilador-yes-finishing-touch-sem-fio-ativacao-sensor-de-luz-rosto-e-corpo-depiladorlaser/connectcellcomercio/depiladorroxo16/958b6b6bada9045715419c0988f0a3b6.jpeg",
        "link": "https://entrega.logzz.com.br/pay/mem0go36g/azjol-skinliss-9999",
        "copy_aida": """
            **O fim da dor na depilação:**
            * **🔥 INTERESSE:** Tecnologia de micro-oscilação que remove o pelo pela raiz sem cortes e sem irritação. Ideal para áreas sensíveis.
            * **✨ DESEJO:** Tenha uma pele de seda todos os dias, sem gastar fortunas em clínicas. Use no rosto, pernas e área do biquíni com total segurança.
            * **⚡ AÇÃO:** Clique abaixo para receber em casa e pagar apenas na entrega!
        """
    }
}

# --- LOGICA ---
if 'detalhe' not in st.session_state: st.session_state.detalhe = None

# Header e Urgência
st.markdown('<div class="header-top"><h1>🦊 Top Ofertas</h1><span>⭐ 4.9/5 Satisfação</span></div>', unsafe_allow_html=True)
st.markdown('<div class="urgency-banner">⚠️ AVISO: DEVIDO AO SUCESSO NO TIKTOK, RESTAM POUCAS UNIDADES EM ESTOQUE!</div>', unsafe_allow_html=True)

# --- PÁGINA DE PRODUTO ---
if st.session_state.detalhe:
    p = produtos[st.session_state.detalhe]
    if st.button("⬅ VOLTAR À VITRINE"):
        st.session_state.detalhe = None
        st.rerun()

    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.image(p["img"], use_container_width=True)
    with col2:
        st.markdown(f"<p style='color:#FF8C00; font-weight:bold;'>{p['tagline']}</p>", unsafe_allow_html=True)
        st.title(p["nome"])
        st.markdown(f"<span class='price-before'>De R$ {p['preco_antigo']}</span><br><span class='price-now'>R$ {p['preco']}</span>", unsafe_allow_html=True)
        st.success("✅ Disponível para pagamento na entrega!")
        
        st.write("---")
        st.markdown(p["copy_aida"])
        st.write("---")
        
        st.link_button("QUERO COMPRAR COM DESCONTO AGORA 🛒", p["link"])

# --- VITRINE ---
else:
    st.image("https://http2.mlstatic.com/D_NQ_648500-MLA73797871625_012024-OO.webp", use_container_width=True)
    st.write("### 💎 Ofertas Exclusivas")
    
    cols = st.columns(4)
    for idx, (id_p, p) in enumerate(produtos.items()):
        with cols[idx]:
            st.markdown(f"""
                <div class="product-card">
                    <img src="{p['img']}" style="width:100%; border-radius:10px;">
                    <h4 style="margin-top:15px; font-size:16px;">{p['nome']}</h4>
                    <p class="price-before">R$ {p['preco_antigo']}</p>
                    <p class="price-now">R$ {p['preco']}</p>
                    <p style="color:#00A650; font-size:12px;">🚚 FRETE GRÁTIS</p>
                </div>
            """, unsafe_allow_html=True)
            if st.button("QUERO VER MAIS", key=id_p):
                st.session_state.detalhe = id_p
                st.rerun()

# --- RODAPÉ ---
st.markdown("""<div style='background:#111; color:#777; padding:40px; text-align:center; margin-top:50px;'>
    <p><b>Top Ofertas Brasil</b><br>Sua segurança é nossa prioridade. Pagamento na entrega via Logzz.</p>
</div>""", unsafe_allow_html=True)