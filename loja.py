import streamlit as st

# 1. Configurações e CSS de Alta Densidade
st.set_page_config(page_title="Top Ofertas - Oficial", page_icon="🦊", layout="wide")

st.markdown("""
    <style>
    /* Fundo geral mais escuro para destacar os cards */
    .stApp { background-color: #E5E5E5; }
    .block-container { padding-top: 0rem; padding-bottom: 5rem; }

    /* HEADER: Amarelo Mercado Livre vibrante */
    .header-container {
        background-color: #FFF159;
        padding: 15px 10%;
        display: flex; align-items: center; justify-content: space-between;
        margin: -6rem -5rem 20px -5rem;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    
    /* BARRA DE PESQUISA (Visual) */
    .search-bar {
        background: white; padding: 8px 15px; width: 50%;
        border-radius: 4px; color: #888; display: flex; align-items: center;
        box-shadow: 0 1px 2px rgba(0,0,0,0.1); font-size: 14px;
    }

    /* CARD DE PRODUTO */
    .card-box {
        background: white; border-radius: 8px;
        padding: 15px; position: relative;
        transition: 0.3s; height: 100%; border: 1px solid #ddd;
    }
    .card-box:hover {
        box-shadow: 0 10px 20px rgba(0,0,0,0.2); transform: translateY(-3px);
    }
    
    /* Elementos do Card */
    .badge-off {
        background: #FF4040; color: white; font-size: 10px; font-weight: bold;
        padding: 2px 6px; border-radius: 3px; position: absolute; top: 10px; right: 10px;
    }
    .img-container {
        height: 180px; display: flex; align-items: center; justify-content: center;
        margin-bottom: 10px; border-bottom: 1px solid #f0f0f0;
    }
    .titulo-prod { font-size: 14px; color: #333; height: 40px; overflow: hidden; margin-bottom: 5px; line-height: 1.2; }
    .preco-antigo { text-decoration: line-through; color: #999; font-size: 12px; }
    .preco-atual { font-size: 24px; color: #333; font-weight: 400; }
    .frete-full { color: #00A650; font-weight: bold; font-size: 12px; font-style: italic; }
    .stars { color: #FFD700; font-size: 12px; margin-bottom: 5px; }

    /* Botão Integrado */
    .stButton > button {
        width: 100%; border-radius: 6px !important;
        background-color: #3483FA !important; color: white !important;
        border: none; font-weight: bold; height: 40px;
    }
    </style>
""", unsafe_allow_html=True)

# 2. BANCO DE DADOS (Atualizei a imagem do MOP que estava quebrada)
produtos = {
    "cinta": {
        "nome": "Cinta Modeladora Yoga Premium Alta Compressão",
        "preco_antigo": "159,90", "preco": "99,99",
        "img": "https://logzz-s3.s3.us-east-2.amazonaws.com/uploads/files/products/20240714-131356prok2m05.jpg",
        "link": "https://entrega.logzz.com.br/pay/mem6qq3rw/vlqxc-1-unidade",
        "stars": "⭐⭐⭐⭐⭐ (4.9)",
        "descricao": "Reduza medidas instantaneamente com conforto total.",
        "topicos": ["✅ Não enrola", "✅ Corrige postura", "✅ Invisível na roupa"]
    },
    "depilador": {
        "nome": "Depilador Elétrico SkinLiss Finishing Touch",
        "preco_antigo": "120,00", "preco": "89,90",
        "img": "https://a-static.mlcdn.com.br/470x352/depilador-yes-finishing-touch-sem-fio-ativacao-sensor-de-luz-rosto-e-corpo-depiladorlaser/connectcellcomercio/depiladorroxo16/958b6b6bada9045715419c0988f0a3b6.jpeg",
        "link": "https://entrega.logzz.com.br/pay/mem0go36g/azjol-skinliss-9999",
        "stars": "⭐⭐⭐⭐⭐ (4.8)",
        "descricao": "Pele lisinha sem dor e sem alergias.",
        "topicos": ["✅ Bateria Recarregável", "✅ Luz Ativa", "✅ Portátil"]
    },
     "mop": {
        "nome": "Mop Giratório 360 Limpeza Pesada + Refil",
        "preco_antigo": "189,90", "preco": "129,90",
        "img": "https://m.media-amazon.com/images/I/71wWk-iW9WL._AC_SL1500_.jpg", 
        "link": "#",
        "stars": "⭐⭐⭐⭐ (4.7)",
        "descricao": "Esqueça o pano de chão. Limpeza rápida e prática.",
        "topicos": ["✅ Centrifuga e Seca", "✅ Cabo Extensível", "✅ Microfibra"]
    },
    "fone": {
        "nome": "Fone Bluetooth Pro 5s Cancelamento de Ruído",
        "preco_antigo": "99,90", "preco": "59,90",
        "img": "https://m.media-amazon.com/images/I/51rP8-wC2UL._AC_SL1000_.jpg",
        "link": "#",
        "stars": "⭐⭐⭐⭐⭐ (5.0)",
        "descricao": "Som de alta qualidade com preço imbatível.",
        "topicos": ["✅ Bluetooth 5.0", "✅ Bateria longa duração", "✅ Grave Potente"]
    }
}

# 3. Lógica de Navegação
if 'detalhe_id' not in st.session_state: st.session_state.detalhe_id = None

# --- HEADER (Onde a mágica visual acontece) ---
st.markdown(f"""
    <div class="header-container">
        <div style="display:flex; align-items:center; gap:10px;">
            <img src="https://raw.githubusercontent.com/isac85962-bit/Loja-Logzz/main/WhatsApp%20Image%202026-01-09%20at%2017.29.39.jpeg" width="45" style="border-radius:50%; border:2px solid white;">
            <span style="font-weight:bold; font-size:20px; color:#2d3277;">TOP OFERTAS</span>
        </div>
        <div class="search-bar">🔍 Buscar produtos, marcas e muito mais...</div>
        <div style="font-size:24px;">🛒</div>
    </div>
""", unsafe_allow_html=True)

# --- TELA DE DETALHES ---
if st.session_state.detalhe_id:
    p = produtos[st.session_state.detalhe_id]
    
    st.markdown(f"<div style='padding:0 5%;'><button style='background:none; border:none; color:#3483fa; cursor:pointer; font-weight:bold;'>⬅ Voltar</button></div>", unsafe_allow_html=True)
    if st.button("⬅️ VOLTAR PARA OFERTAS"):
        st.session_state.detalhe_id = None
        st.rerun()

    with st.container():
        st.markdown('<div style="background:white; padding:30px; border-radius:8px; margin:20px 5%; box-shadow:0 2px 10px rgba(0,0,0,0.1);">', unsafe_allow_html=True)
        c1, c2 = st.columns([1, 1])
        with c1: st.image(p["img"], use_container_width=True)
        with c2:
            st.markdown(f"""
                <span style="font-size:12px; color:#999;">Novo | +500 vendidos</span>
                <h1 style="font-size:22px; margin:5px 0;">{p['nome']}</h1>
                <div style="color:#FFD700; margin-bottom:10px;">{p['stars']} (120 avaliações)</div>
                <div style="background:#333; color:white; padding:5px 10px; border-radius:4px; display:inline-block; font-size:12px; margin-bottom:10px;">OFERTA DO DIA</div>
                <p style="text-decoration:line-through; color:#ccc; margin:0;">R$ {p['preco_antigo']}</p>
                <p style="font-size:36px; color:#333; font-weight:300; margin:0;">R$ {p['preco']}</p>
                <p style="color:#00a650; font-size:14px; font-weight:bold;">em 12x sem juros</p>
                <p style="color:#00a650; font-weight:bold;">⚡ Chegará grátis amanhã!</p>
            """, unsafe_allow_html=True)
            st.write("---")
            for t in p["topicos"]: st.markdown(f"<p style='margin:5px 0;'>{t}</p>", unsafe_allow_html=True)
            st.write("")
            st.link_button("COMPRAR AGORA", p["link"], use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

# --- TELA INICIAL (VITRINE) ---
else:
    # Banner Rotativo
    st.image("https://http2.mlstatic.com/D_NQ_648500-MLA73797871625_012024-OO.webp", use_container_width=True)
    
    # Faixa de Benefícios
    st.markdown("""
        <div style="background:white; padding:15px; margin:10px 0; border-radius:5px; display:flex; justify-content:space-around; font-size:13px; box-shadow:0 1px 2px rgba(0,0,0,0.05);">
            <span>💳 <b>Até 12x sem juros</b></span>
            <span>🚚 <b>Frete Grátis</b> para todo Brasil</span>
            <span>🛡️ <b>Compra Garantida</b></span>
        </div>
        <h3 style="margin:20px 0; color:#333;">🔥 Ofertas em Destaque</h3>
    """, unsafe_allow_html=True)

    # GRID DE PRODUTOS
    cols = st.columns(4)
    ids = list(produtos.keys())
    
    for i, col in enumerate(cols):
        if i < len(ids):
            pid = ids[i]
            p = produtos[pid]
            with col:
                st.markdown(f"""
                    <div class="card-box">
                        <span class="badge-off">25% OFF</span>
                        <div class="img-container"><img src="{p['img']}" style="max-height:100%; max-width:100%;"></div>
                        <p class="titulo-prod">{p['nome']}</p>
                        <div class="stars">{p['stars']}</div>
                        <span class="preco-antigo">R$ {p['preco_antigo']}</span>
                        <div class="preco-atual">R$ {p['preco']}</div>
                        <div class="frete-full">Chega amanhã ⚡</div>
                    </div>
                """, unsafe_allow_html=True)
                if st.button("Ver Detalhes", key=pid):
                    st.session_state.detalhe_id = pid
                    st.rerun()

# --- RODAPÉ ---
st.markdown("""
    <div style="margin-top:50px; background:#333; color:#fff; padding:30px; text-align:center; font-size:12px;">
        <p>Copyright © 2026 Top Ofertas - Todos os direitos reservados.</p>
        <p>CNPJ: 00.000.000/0001-00 | Jaraguá do Sul, SC</p>
    </div>
""", unsafe_allow_html=True)