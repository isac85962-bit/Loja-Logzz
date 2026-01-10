import streamlit as st

# 1. Configurações de Página e Estilo
st.set_page_config(page_title="Top Ofertas - Oficial", page_icon="🦊", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #F7F7F7; }
    
    /* Barra Superior Compacta */
    .top-bar {
        background-color: #FF8C00; 
        padding: 8px 5%;
        margin: -6rem -5rem 1rem -5rem;
        display: flex; align-items: center; gap: 15px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }

    /* Estilo dos Banners de Categoria */
    .banner-categoria {
        padding: 30px; border-radius: 12px; color: white;
        margin: 20px 0 10px 0; font-family: sans-serif;
    }
    .banner-casa { background: linear-gradient(90deg, #FF8C00, #FFA500); }
    .banner-saude { background: linear-gradient(90deg, #2ecc71, #27ae60); }

    /* Card de Produto */
    .card-produto {
        background: white; padding: 15px; border-radius: 10px;
        border: 1px solid #EEE; text-align: center; height: 100%;
    }
    .preco-top { color: #FF8C00; font-size: 20px; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# 2. BANCO DE DADOS EDITÁVEL
# Aqui você pode adicionar novos produtos e editar as características em tópicos
produtos = {
    "cinta": {
        "nome": "Cinta Colete Modeladora Ampla",
        "preco": "99,99",
        "img": "https://logzz-s3.s3.us-east-2.amazonaws.com/uploads/files/products/20240714-131356prok2m05.jpg",
        "categoria": "Saúde",
        "link": "https://entrega.logzz.com.br/pay/mem6qq3rw/vlqxc-1-unidade",
        "descricao": "A cinta original para correção postural e redução de medidas.",
        "topicos": ["✅ Reduz medidas na hora", "✅ Melhora a postura", "✅ Material PowerNet respirável"]
    },
    "depilador": {
        "nome": "Depilador SkinLiss Pro",
        "preco": "89,90",
        "img": "https://a-static.mlcdn.com.br/470x352/depilador-yes-finishing-touch-sem-fio-ativacao-sensor-de-luz-rosto-e-corpo-depiladorlaser/connectcellcomercio/depiladorroxo16/958b6b6bada9045715419c0988f0a3b6.jpeg",
        "categoria": "Saúde",
        "link": "https://entrega.logzz.com.br/pay/mem0go36g/azjol-skinliss-9999",
        "descricao": "Depilação indolor e eficaz para todas as partes do corpo.",
        "topicos": ["✅ Tecnologia de Micro-oscilação", "✅ Bateria Recarregável", "✅ Luz LED integrada"]
    }
}

# 3. Gerenciamento de Navegação
if 'detalhe_id' not in st.session_state: st.session_state.detalhe_id = None

# Header Fixo
st.markdown(f"""
    <div class="top-bar">
        <img src="https://raw.githubusercontent.com/isac85962-bit/Loja-Logzz/main/WhatsApp%20Image%202026-01-09%20at%2017.29.39.jpeg" width="45" style="border-radius:50%">
        <h2 style="color:white; margin:0;">TOP OFERTAS</h2>
    </div>
""", unsafe_allow_html=True)

# --- VISÃO: DETALHES DO PRODUTO ---
if st.session_state.detalhe_id:
    p = produtos[st.session_state.detalhe_id]
    if st.button("⬅️ Voltar para a Vitrine"):
        st.session_state.detalhe_id = None
        st.rerun()
    
    col_img, col_info = st.columns([1, 1])
    with col_img: st.image(p["img"], use_container_width=True)
    with col_info:
        st.title(p["nome"])
        st.markdown(f"<p class='preco-top'>R$ {p['preco']}</p>", unsafe_allow_html=True)
        st.write("---")
        st.write(f"### 📝 Descrição\n{p['descricao']}")
        st.write("### 📌 Características:")
        for t in p["topicos"]: st.write(t)
        st.write("---")
        st.link_button("🔥 COMPRAR AGORA (Pagar na Entrega)", p["link"])

# --- VISÃO: HOME ---
else:
    # 4. BANNER ROTATIVO (Carrossel Simulado)
    # Você pode trocar os links pelas imagens que criar no Canva
    banners = [
        "https://images.tcdn.com.br/img/editor/up/649983/Banner_Topo_Desktop_1.jpg",
        "https://images.tcdn.com.br/img/editor/up/649983/Banner_Topo_Desktop_2.jpg"
    ]
    st.image(banners[0], use_container_width=True) # Exibe o banner principal

    # --- SEÇÃO SAÚDE ---
    st.markdown('<div class="banner-categoria banner-saude"><h2>✨ SAÚDE E BELEZA</h2><p>Cuide de você com os melhores preços</p></div>', unsafe_allow_html=True)
    
    prod_saude = [id for id, p in produtos.items() if p["categoria"] == "Saúde"]
    cols = st.columns(4)
    for idx, pid in enumerate(prod_saude):
        p = produtos[pid]
        with cols[idx]:
            st.markdown(f"""
                <div class="card-produto">
                    <img src="{p['img']}" style="width:100%; border-radius:5px; height:150px; object-fit:contain;">
                    <p style="font-weight:bold; margin-top:10px;">{p['nome']}</p>
                    <p class="preco-top">R$ {p['preco']}</p>
                </div>
            """, unsafe_allow_html=True)
            if st.button("Ver Detalhes", key=pid):
                st.session_state.detalhe_id = pid
                st.rerun()