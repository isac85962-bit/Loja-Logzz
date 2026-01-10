import streamlit as st

# 1. Configurações Iniciais
st.set_page_config(page_title="Top Ofertas - Oficial", page_icon="🦊", layout="wide")

# 2. Estilo CSS (Foco em Cartões Brancos e Laranja Oficial)
st.markdown("""
    <style>
    .stApp { background-color: #F7F7F7; color: #333; }
    
    /* Cabeçalho Compacto */
    .top-bar {
        background-color: #FF8C00; 
        padding: 10px 5%;
        margin: -6rem -5rem 2rem -5rem;
        display: flex;
        align-items: center;
        gap: 15px;
    }

    /* Card de Produto na Vitrine */
    .card-vitrine {
        background: white;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #EAEAEA;
        text-align: center;
        transition: 0.3s;
    }
    .card-vitrine:hover { box-shadow: 0 10px 20px rgba(0,0,0,0.05); }

    /* Container de Detalhes (Inspirado na sua imagem) */
    .detalhe-container {
        background: white;
        padding: 30px;
        border-radius: 15px;
        border-top: 5px solid #FF8C00;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    }

    /* Botão de Compra */
    .stButton>button {
        background-color: #FF8C00 !important;
        color: white !important;
        border-radius: 8px !important;
        font-weight: bold !important;
        height: 50px;
        width: 100%;
        border: none;
    }
    </style>
""", unsafe_allow_html=True)

# 3. BANCO DE DADOS (Aqui você edita e adiciona produtos)
produtos = {
    "cinta": {
        "nome": "Cinta Colete Modeladora Premium",
        "preco": "99,99",
        "img": "https://logzz-s3.s3.us-east-2.amazonaws.com/uploads/files/products/20240714-131356prok2m05.jpg",
        "link": "https://entrega.logzz.com.br/pay/mem6qq3rw/vlqxc-1-unidade",
        "resumo": "Compressão máxima e correção postural.",
        "descricao_completa": """
            ### 🦊 Detalhes do Produto
            A nossa Cinta Colete é a única com tecnologia **Dual-Compression**, que molda a cintura sem tirar o seu fôlego. 
            
            **Por que escolher a Top Ofertas?**
            * ✨ **Invisível:** Use por baixo de qualquer roupa.
            * 🌬️ **Respirável:** Não esquenta e não causa irritação.
            * 📐 **Tamanhos:** Ajustável para todos os corpos.
        """
    },
    "depilador": {
        "nome": "Depilador SkinLiss Finishing Touch",
        "preco": "89,90",
        "img": "https://a-static.mlcdn.com.br/470x352/depilador-yes-finishing-touch-sem-fio-ativacao-sensor-de-luz-rosto-e-corpo-depiladorlaser/connectcellcomercio/depiladorroxo16/958b6b6bada9045715419c0988f0a3b6.jpeg",
        "link": "https://entrega.logzz.com.br/pay/mem0go36g/azjol-skinliss-9999",
        "resumo": "Depilação indolor com sensor de luz.",
        "descricao_completa": """
            ### 🦊 Detalhes do Produto
            O SkinLiss remove os pelos instantaneamente através de micro-oscilações. 
            
            **Diferenciais:**
            * 🔋 **Recarregável:** Acompanha cabo USB.
            * 💡 **Sensor LED:** Só funciona ao tocar na pele (segurança total).
            * 🧼 **Hipoalergênico:** Ideal para peles sensíveis.
        """
    }
}

# 4. Navegação
if 'produto_id' not in st.session_state: st.session_state.produto_id = None

# Header com Mascote
st.markdown(f"""
    <div class="top-bar">
        <img src="https://raw.githubusercontent.com/isac85962-bit/Loja-Logzz/main/WhatsApp%20Image%202026-01-09%20at%2017.29.39.jpeg" width="50" style="border-radius:50%">
        <h2 style="color:white; margin:0;">TOP OFERTAS</h2>
    </div>
""", unsafe_allow_html=True)

# --- PÁGINA DE DETALHES ---
if st.session_state.produto_id:
    p = produtos[st.session_state.produto_id]
    
    if st.button("⬅️ Voltar para as Ofertas"):
        st.session_state.produto_id = None
        st.rerun()

    st.markdown('<div class="detalhe-container">', unsafe_allow_html=True)
    col1, col2 = st.columns([1, 1.2])
    
    with col1:
        st.image(p["img"], use_container_width=True)
    
    with col2:
        st.caption("Top Ofertas - Vendedor Oficial")
        st.title(p["nome"])
        st.markdown(f"<h2 style='color:#FF8C00;'>R$ {p['preco']}</h2>", unsafe_allow_html=True)
        
        st.write("---")
        cep = st.text_input("📍 Informe seu CEP para entrega rápida:")
        if cep:
            st.success("✅ Disponível para sua região! Pagamento na entrega disponível.")
            st.link_button("🔥 COMPRAR AGORA (Pagamento na Entrega)", p["link"])
        
        st.markdown(p["descricao_completa"])
    st.markdown('</div>', unsafe_allow_html=True)

# --- PÁGINA HOME (VITRINE) ---
else:
    st.markdown("""
        <div style="background:#FFD700; padding:15px; border-radius:10px; text-align:center; margin-bottom:20px">
            <h4 style="margin:0">🚚 FRETE GRÁTIS E PAGAMENTO NO ATO DA ENTREGA! 🦊</h4>
        </div>
    """, unsafe_allow_html=True)

    cols = st.columns(4)
    for idx, (id_p, p) in enumerate(produtos.items()):
        with cols[idx]:
            st.markdown(f"""
                <div class="card-vitrine">
                    <img src="{p['img']}" style="width:100%; border-radius:8px">
                    <p style="font-weight:bold; margin-top:10px">{p['nome']}</p>
                    <p style="color:#FF8C00; font-size:20px; font-weight:bold">R$ {p['preco']}</p>
                </div>
            """, unsafe_allow_html=True)
            if st.button("Ver Detalhes", key=id_p):
                st.session_state.produto_id = id_p
                st.rerun()