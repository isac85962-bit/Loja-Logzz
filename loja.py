import streamlit as st
import time

# 1. Configurações e Design UX/UI
st.set_page_config(page_title="Top Ofertas | Oficial", page_icon="🦊", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; }
    .block-container { padding-top: 0rem; padding-bottom: 2rem; }

    /* Header Slim & Moderno */
    .header-top {
        background: #FF8C00;
        padding: 10px 10%;
        display: flex; align-items: center; justify-content: space-between;
        margin: -6rem -5rem 0 -5rem;
        color: white;
    }

    /* Banner de Urgência (Fininho no topo) */
    .urgency-bar {
        background: #333; color: #FFD700;
        text-align: center; padding: 5px; font-size: 13px;
        margin: 0 -5rem 20px -5rem; font-weight: bold;
    }

    /* Cards Ultra Clean */
    .product-card {
        background: white; border: 1px solid #F0F0F0;
        border-radius: 12px; padding: 15px; transition: 0.3s;
        text-align: center; cursor: pointer;
    }
    .product-card:hover { border-color: #FF8C00; box-shadow: 0 12px 24px rgba(0,0,0,0.08); }
    
    .price-tag { color: #FF8C00; font-size: 24px; font-weight: 800; }
    .old-price { color: #999; text-decoration: line-through; font-size: 14px; }
    
    /* Botão Persuasivo */
    .stButton > button {
        background: #FF8C00 !important; color: white !important;
        border-radius: 50px !important; font-weight: bold !important;
        border: none; width: 100%; transition: 0.3s;
    }
    .stButton > button:hover { background: #E67E00 !important; transform: scale(1.02); }

    /* Footer Profissional */
    .main-footer {
        background: #1A1A1A; color: #999; padding: 40px 10%;
        margin: 50px -5rem -2rem -5rem; text-align: left;
    }
    </style>
""", unsafe_allow_html=True)

# 2. Banco de Dados com Gatilhos
produtos = {
    "cinta": {
        "nome": "Cinta Modeladora Yoga Premium - Edição 2026",
        "preco_antigo": "197,00", "preco": "97,90",
        "img": "https://logzz-s3.s3.us-east-2.amazonaws.com/uploads/files/products/20240714-131356prok2m05.jpg",
        "estoque": 7, "vendas": 1452,
        "link": "https://entrega.logzz.com.br/pay/mem6qq3rw/vlqxc-1-unidade"
    },
    "depilador": {
        "nome": "Depilador SkinLiss Pro Max - Recarregável",
        "preco_antigo": "149,00", "preco": "84,90",
        "img": "https://a-static.mlcdn.com.br/470x352/depilador-yes-finishing-touch-sem-fio-ativacao-sensor-de-luz-rosto-e-corpo-depiladorlaser/connectcellcomercio/depiladorroxo16/958b6b6bada9045715419c0988f0a3b6.jpeg",
        "estoque": 12, "vendas": 890,
        "link": "https://entrega.logzz.com.br/pay/mem0go36g/azjol-skinliss-9999"
    }
}

# 3. Cabeçalho e Urgência
st.markdown('<div class="header-top"><h2>🦊 Top Ofertas</h2><span>🚚 Frete Grátis hoje</span></div>', unsafe_allow_html=True)
st.markdown('<div class="urgency-bar">⚡ OFERTA TERMINA EM 07:42 - APROVEITE O PREÇO DE ATACADO!</div>', unsafe_allow_html=True)

if 'detalhe' not in st.session_state: st.session_state.detalhe = None

# --- PÁGINA DE DETALHES (FOCO EM CONVERSÃO) ---
if st.session_state.detalhe:
    p = produtos[st.session_state.detalhe]
    if st.button("⬅ VOLTAR PARA A LOJA"):
        st.session_state.detalhe = None
        st.rerun()

    c1, c2 = st.columns([1, 1])
    with c1:
        st.image(p["img"], use_container_width=True)
    with c2:
        st.markdown(f"**🔥 {p['vendas']} pessoas compraram isso nas últimas 24h**")
        st.title(p["nome"])
        st.markdown(f"⭐ ⭐ ⭐ ⭐ ⭐ (4.9/5)")
        st.markdown(f"<span class='old-price'>De R$ {p['preco_antigo']}</span>", unsafe_allow_html=True)
        st.markdown(f"<span class='price-tag'>R$ {p['preco']}</span>", unsafe_allow_html=True)
        st.info(f"😱 Restam apenas {p['estoque']} unidades no estoque promocional!")
        
        st.write("---")
        st.write("**✅ Por que comprar conosco?**")
        st.write("• Pagamento seguro na porta (Logzz)")
        st.write("• Garantia de 30 dias contra defeitos")
        st.write("• Suporte via WhatsApp pós-venda")
        
        st.link_button("QUERO GARANTIR O MEU AGORA 🛒", p["link"])

    # Seção de Depoimentos (Simulados para Persuasão)
    st.write("---")
    st.subheader("Quem já comprou, aprova! ✅")
    d1, d2, d3 = st.columns(3)
    d1.success("**Maria S.** - 'Chegou muito rápido em SP. O material é ótimo!'")
    d2.success("**Carlos J.** - 'Minha esposa amou. Pagamos na entrega, muito seguro.'")
    d3.success("**Patrícia R.** - 'Melhor preço que achei. Atendimento nota 10.'")

# --- VITRINE CLEAN ---
else:
    st.subheader("🔥 Ofertas do Dia")
    cols = st.columns(4)
    for idx, (id_p, p) in enumerate(produtos.items()):
        with cols[idx]:
            st.markdown(f"""
                <div class="product-card">
                    <img src="{p['img']}" style="width:100%; border-radius:8px; margin-bottom:10px;">
                    <p style="font-size:14px; font-weight:500; height:40px; overflow:hidden;">{p['nome']}</p>
                    <span class="old-price">R$ {p['preco_antigo']}</span><br>
                    <span class="price-tag">R$ {p['preco']}</span><br>
                    <small style="color:#00A650;">⚡ Frete Grátis</small>
                </div>
            """, unsafe_allow_html=True)
            if st.button("VER DETALHES", key=id_p):
                st.session_state.detalhe = id_p
                st.rerun()

# --- RODAPÉ PERSUASIVO ---
st.markdown(f"""
    <div class="main-footer">
        <div style="display:flex; justify-content:space-between;">
            <div style="width:30%;">
                <h3 style="color:white;">FOX TOP OFERTAS</h3>
                <p>Sua loja de confiança com entrega garantida e pagamento facilitado.</p>
            </div>
            <div>
                <h4 style="color:white;">SUPORTE</h4>
                <p>E-mail: contato@topofertas.com<br>WhatsApp: (00) 00000-0000</p>
            </div>
            <div>
                <h4 style="color:white;">SEGURANÇA</h4>
                <p>✅ Site Criptografado<br>✅ Pagamento via Logzz</p>
            </div>
        </div>
        <hr style="border-color:#333;">
        <p style="text-align:center; font-size:12px;">© 2026 Top Ofertas - CNPJ: 00.000.000/0001-00. Proibida reprodução total ou parcial.</p>
    </div>
""", unsafe_allow_html=True)