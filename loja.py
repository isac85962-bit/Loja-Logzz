import streamlit as st

# 1. Configurações e CSS (AQUI ESTÁ A MÁGICA DAS CORES)
st.set_page_config(page_title="Top Ofertas - Oficial", page_icon="🦊", layout="wide")

st.markdown("""
    <style>
    /* Fundo levemente cinza para destacar o Laranja */
    .stApp { background-color: #F5F5F5; }
    .block-container { padding-top: 0rem; padding-bottom: 5rem; }

    /* HEADER: O Laranja Oficial da Top Ofertas */
    .header-container {
        background: linear-gradient(90deg, #FF8C00 0%, #FFA500 100%);
        padding: 15px 10%;
        display: flex; align-items: center; justify-content: space-between;
        margin: -6rem -5rem 20px -5rem;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        color: white;
    }
    
    /* Barra de Pesquisa */
    .search-bar {
        background: white; padding: 10px 20px; width: 50%;
        border-radius: 30px; color: #888; display: flex; align-items: center;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1); font-size: 14px;
    }

    /* CARD DE PRODUTO */
    .card-box {
        background: white; border-radius: 12px;
        padding: 15px; position: relative;
        transition: 0.3s; height: 100%; border: 1px solid #EEE;
    }
    .card-box:hover {
        box-shadow: 0 10px 20px rgba(255, 140, 0, 0.15); /* Sombra Laranja suave */
        transform: translateY(-5px); border-color: #FF8C00;
    }
    
    /* Elementos do Card */
    .badge-off {
        background: #FF0000; color: white; font-size: 10px; font-weight: bold;
        padding: 4px 8px; border-radius: 4px; position: absolute; top: 10px; right: 10px;
        z-index: 10;
    }
    .img-container {
        height: 180px; display: flex; align-items: center; justify-content: center;
        margin-bottom: 10px; border-bottom: 1px solid #f9f9f9;
    }
    .titulo-prod { font-size: 14px; color: #333; height: 40px; overflow: hidden; margin-bottom: 5px; font-weight: 500;}
    .preco-antigo { text-decoration: line-through; color: #BBB; font-size: 12px; }
    .preco-atual { font-size: 26px; color: #FF8C00; font-weight: bold; } /* Preço Laranja */
    .frete-full { color: #00A650; font-weight: bold; font-size: 12px; display: flex; align-items: center; gap: 5px;}
    .stars { color: #FFD700; font-size: 12px; margin-bottom: 5px; }

    /* BOTÃO LARANJA (Cor da Marca) */
    .stButton > button {
        width: 100%; border-radius: 8px !important;
        background-color: #FF8C00 !important; color: white !important; /* Laranja */
        border: none; font-weight: bold; height: 45px;
        box-shadow: 0 4px 0 #cc7000; /* Efeito 3D no botão */
        margin-top: 10px;
        transition: 0.2s;
    }
    .stButton > button:hover {
        background-color: #e67e00 !important;
        box-shadow: 0 2px 0 #cc7000;
        transform: translateY(2px);
    }
    
    /* Rodapé Escuro */
    .footer {
        background-color: #222; color: white;
        padding: 40px; text-align: center;
        margin: 50px -5rem -5rem -5rem;
    }
    </style>
""", unsafe_allow_html=True)

# 2. BANCO DE DADOS (Links Atualizados)
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
        "img": "https://images-americanas.b2w.io/produtos/01/00/item/133668/2/133668276_1GG.jpg", 
        "link": "#",
        "stars": "⭐⭐⭐⭐ (4.7)",
        "descricao": "Esqueça o pano de chão. Limpeza rápida e prática.",
        "topicos": ["✅ Centrifuga e Seca", "✅ Cabo Extensível", "✅ Microfibra"]
    },
    "fone": {
        "nome": "Fone Bluetooth TWS Gamer Sem Fio",
        "preco_antigo": "99,90", "preco": "59,90",
        "img": "https://images-americanas.b2w.io/produtos/4462635954/imagens/fone-de-ouvido-sem-fio-bluetooth-tws-f9-5-com-power-bank/4462635954_1_large.jpg",
        "link": "#",
        "stars": "⭐⭐⭐⭐⭐ (5.0)",
        "descricao": "Som de alta qualidade com preço imbatível.",
        "topicos": ["✅ Bluetooth 5.0", "✅ Bateria longa duração", "✅ Grave Potente"]
    }
}

# 3. Lógica de Navegação
if 'detalhe_id' not in st.session_state: st.session_state.detalhe_id = None

# --- HEADER LARANJA ---
st.markdown(f"""
    <div class="header-container">
        <div style="display:flex; align-items:center; gap:15px;">
            <img src="https://raw.githubusercontent.com/isac85962-bit/Loja-Logzz/main/WhatsApp%20Image%202026-01-09%20at%2017.29.39.jpeg" width="55" style="border-radius:50%; border:3px solid rgba(255,255,255,0.5);">
            <span style="font-weight:900; font-size:26px; letter-spacing:1px;">TOP OFERTAS</span>
        </div>
        <div class="search-bar">🔍 O que você procura hoje?</div>
        <div style="font-size:24px; cursor:pointer;">🛒 <span style="font-size:14px; font-weight:bold;">(0)</span></div>
    </div>
""", unsafe_allow_html=True)

# --- TELA DE DETALHES ---
if st.session_state.detalhe_id:
    p = produtos[st.session_state.detalhe_id]
    
    st.markdown(f"<div style='padding:10px 5%;'><button style='background:none; border:none; color:#FF8C00; cursor:pointer; font-weight:bold; font-size:16px;'>⬅ Voltar para Loja</button></div>", unsafe_allow_html=True)
    if st.button("⬅️ VOLTAR"):
        st.session_state.detalhe_id = None
        st.rerun()

    with st.container():
        st.markdown('<div style="background:white; padding:40px; border-radius:15px; margin:10px 5%; box-shadow:0 5px 20px rgba(0,0,0,0.05);">', unsafe_allow_html=True)
        c1, c2 = st.columns([1, 1])
        with c1: st.image(p["img"], use_container_width=True)
        with c2:
            st.markdown(f"""
                <span style="background:#FF8C00; color:white; padding:4px 10px; border-radius:20px; font-size:12px; font-weight:bold;">MAIS VENDIDO</span>
                <h1 style="font-size:32px; margin:15px 0 5px 0; color:#333;">{p['nome']}</h1>
                <div style="color:#FFD700; margin-bottom:20px;">{p['stars']} (Ver avaliações)</div>
                
                <p style="text-decoration:line-through; color:#ccc; margin:0; font-size:16px;">De R$ {p['preco_antigo']}</p>
                <p style="font-size:48px; color:#FF8C00; font-weight:800; margin:0; line-height:1;">R$ {p['preco']}</p>
                <p style="color:#333; font-size:16px;">em até <b>12x sem juros</b> no cartão</p>
                
                <div style="margin:20px 0; padding:15px; background:#F9F9F9; border-radius:10px;">
                    <p style="color:#00A650; font-weight:bold; margin:0;">🚚 Frete Grátis para todo Brasil</p>
                    <small style="color:#666;">Chegará entre 2 a 5 dias úteis</small>
                </div>
            """, unsafe_allow_html=True)
            
            st.write("### O que você precisa saber:")
            for t in p["topicos"]: st.markdown(f"✅ {t}")
            
            st.write("")
            st.link_button("COMPRAR AGORA 🛒", p["link"], use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

# --- TELA INICIAL (VITRINE) ---
else:
    # Banner Topo
    st.image("https://http2.mlstatic.com/D_NQ_648500-MLA73797871625_012024-OO.webp", use_container_width=True)
    
    # Ícones de Confiança (Agora com toques laranja)
    st.markdown("""
        <div style="background:white; padding:20px; margin:20px 0; border-radius:10px; display:flex; justify-content:space-around; align-items:center; text-align:center; box-shadow:0 2px 10px rgba(0,0,0,0.02);">
            <div><div style="font-size:24px;">💳</div><b>Parcelamento</b><br><span style="color:grey; font-size:12px">Em até 12x sem juros</span></div>
            <div style="border-left:1px solid #eee; height:40px;"></div>
            <div><div style="font-size:24px;">🚚</div><b>Frete Grátis</b><br><span style="color:grey; font-size:12px">Para todo o Brasil</span></div>
            <div style="border-left:1px solid #eee; height:40px;"></div>
            <div><div style="font-size:24px;">🛡️</div><b>Compra Segura</b><br><span style="color:grey; font-size:12px">Site verificado 100%</span></div>
        </div>
        <h3 style="margin:30px 0 20px 0; color:#333; border-left:5px solid #FF8C00; padding-left:10px;">🔥 Ofertas Imperdíveis</h3>
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
                        <span class="badge-off">30% OFF</span>
                        <div class="img-container"><img src="{p['img']}" style="max-height:100%; max-width:100%;"></div>
                        <p class="titulo-prod">{p['nome']}</p>
                        <div class="stars">{p['stars']}</div>
                        <span class="preco-antigo">R$ {p['preco_antigo']}</span>
                        <div class="preco-atual">R$ {p['preco']}</div>
                        <div class="frete-full">⚡ Chega Amanhã</div>
                    </div>
                """, unsafe_allow_html=True)
                if st.button("Ver Detalhes", key=pid):
                    st.session_state.detalhe_id = pid
                    st.rerun()

# --- RODAPÉ ---
st.markdown("""
    <div class="footer">
        <p style="font-size:18px; font-weight:bold; color:#FF8C00;">🦊 Top Ofertas</p>
        <p>A sua loja de confiança e economia.</p>
        <hr style="border-color:#444; margin:20px 0;">
        <p style="font-size:12px; color:#888;">© 2026 Top Ofertas - Todos os direitos reservados.</p>
    </div>
""", unsafe_allow_html=True)