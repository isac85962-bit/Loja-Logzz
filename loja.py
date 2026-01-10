import streamlit as st

# 1. CONFIGURAÇÕES E DESIGN UX/UI (ESTILIZAÇÃO CORRIGIDA)
st.set_page_config(page_title="Top Ofertas | Oficial", page_icon="🦊", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    html, body, [class*="st-"] { font-family: 'Inter', sans-serif; }
    
    .stApp { background-color: #F8F9FA; }
    .block-container { padding-top: 0rem; }

    /* HEADER LARANJA TOP OFERTAS */
    .header-top {
        background: linear-gradient(90deg, #FF8C00, #FFA500);
        padding: 15px 10%;
        display: flex; align-items: center; justify-content: space-between;
        margin: -6rem -5rem 0 -5rem;
        color: white; box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }

    /* BARRA DE URGÊNCIA */
    .urgency-bar {
        background: #000; color: #FFD700;
        text-align: center; padding: 8px; font-size: 13px;
        margin: 0 -5rem 20px -5rem; font-weight: bold;
        letter-spacing: 1px;
    }

    /* WHATSAPP FLUTUANTE */
    .whatsapp-float {
        position: fixed; width: 60px; height: 60px; bottom: 40px; right: 40px;
        background-color: #25d366; color: #FFF; border-radius: 50px;
        text-align: center; font-size: 30px; box-shadow: 2px 2px 10px rgba(0,0,0,0.2);
        z-index: 1000; display: flex; align-items: center; justify-content: center;
        transition: 0.3s;
    }

    /* CARDS DE PRODUTO */
    .product-card {
        background: white; border-radius: 15px; padding: 20px;
        text-align: center; transition: 0.4s; border: 1px solid #EEE;
        height: 100%;
    }
    
    .price-now { color: #FF8C00; font-size: 26px; font-weight: 800; }
    .price-before { color: #BBB; text-decoration: line-through; font-size: 14px; }

    /* CORREÇÃO DAS PERGUNTAS FREQUENTES (TEXTO VISÍVEL) */
    .faq-box { 
        background: #FFFFFF; 
        padding: 40px; 
        border-radius: 15px; 
        margin-top: 40px; 
        border-left: 8px solid #FF8C00;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    }
    .faq-box h3 { color: #333333 !important; font-weight: 900; margin-bottom: 25px; }
    .faq-item { margin-bottom: 20px; }
    .faq-question { color: #222222 !important; font-weight: 700; font-size: 16px; display: block; margin-bottom: 5px; }
    .faq-answer { color: #444444 !important; font-size: 15px; line-height: 1.5; }

    /* BOTÃO CTA */
    .stButton > button {
        background: #FF8C00 !important; color: white !important;
        border-radius: 12px !important; font-weight: 800 !important;
        border: none; width: 100%; height: 50px;
    }

    /* RODAPÉ */
    .footer-dark { background: #111; color: #777; padding: 50px 10%; margin: 50px -5rem -5rem -5rem; text-align: center; }
    </style>

    <a href="https://wa.me/5500000000000" class="whatsapp-float" target="_blank">
        <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" width="35">
    </a>
""", unsafe_allow_html=True)

# 2. BANCO DE DADOS
produtos = {
    "cinta": {
        "nome": "Cinta Modeladora Yoga Premium",
        "tagline": "🔥 Atenção: Recupere sua silhueta e confiança em segundos!",
        "preco_antigo": "197,90", "preco": "97,90",
        "img": "https://logzz-s3.s3.us-east-2.amazonaws.com/uploads/files/products/20240714-131356prok2m05.jpg",
        "link": "https://entrega.logzz.com.br/pay/mem6qq3rw/vlqxc-1-unidade",
        "copy": "Tecnologia Soft-Touch que molda sem machucar. Ideal para uso diário e recuperação pós-parto."
    },
    "depilador": {
        "nome": "Depilador Laser-Light SkinLiss 2026",
        "tagline": "✨ Pele de seda sem dor, cortes ou alergias!",
        "preco_antigo": "159,00", "preco": "84,90",
        "img": "https://a-static.mlcdn.com.br/470x352/depilador-yes-finishing-touch-sem-fio-ativacao-sensor-de-luz-rosto-e-corpo-depiladorlaser/connectcellcomercio/depiladorroxo16/958b6b6bada9045715419c0988f0a3b6.jpeg",
        "link": "https://entrega.logzz.com.br/pay/mem0go36g/azjol-skinliss-9999",
        "copy": "Remoção instantânea com micro-oscilação. Seguro para todas as áreas do corpo e rosto."
    }
}

# 3. LÓGICA DE NAVEGAÇÃO
if 'pagina' not in st.session_state: st.session_state.pagina = "home"
if 'produto_id' not in st.session_state: st.session_state.produto_id = None

st.markdown('<div class="header-top"><h2>🦊 Top Ofertas</h2><span>🚚 Frete Grátis para todo Brasil</span></div>', unsafe_allow_html=True)
st.markdown('<div class="urgency-bar">⚡ OFERTA TERMINA EM POUCOS MINUTOS - APROVEITE O PREÇO DE ATACADO!</div>', unsafe_allow_html=True)

if st.session_state.pagina == "detalhes":
    p = produtos[st.session_state.produto_id]
    if st.button("⬅ VOLTAR À VITRINE"):
        st.session_state.pagina = "home"
        st.rerun()

    col1, col2 = st.columns([1, 1.2])
    with col1: st.image(p["img"], use_container_width=True)
    with col2:
        st.markdown(f"<p style='color:#FF8C00; font-weight:bold;'>{p['tagline']}</p>", unsafe_allow_html=True)
        st.title(p["nome"])
        st.markdown(f"<span class='price-now'>R$ {p['preco']}</span>", unsafe_allow_html=True)
        st.write("---")
        st.markdown(f"### 💎 Descrição Premium\n{p['copy']}")
        st.link_button("QUERO COMPRAR AGORA 🛒", p["link"])

else:
    st.image("https://http2.mlstatic.com/D_NQ_648500-MLA73797871625_012024-OO.webp", use_container_width=True)
    
    cols = st.columns(3)
    for idx, (pid, p) in enumerate(produtos.items()):
        with cols[idx % 3]:
            st.markdown(f"""
                <div class="product-card">
                    <img src="{p['img']}" style="width:100%; border-radius:10px;">
                    <p style="margin-top:10px; font-weight:700;">{p['nome']}</p>
                    <p class="price-now">R$ {p['preco']}</p>
                </div>
            """, unsafe_allow_html=True)
            if st.button("VER DETALHES", key=pid):
                st.session_state.produto_id = pid
                st.session_state.pagina = "detalhes"
                st.rerun()

    # --- SEÇÃO FAQ CORRIGIDA ---
    st.markdown("""
        <div class="faq-box">
            <h3>🙋‍♂️ Perguntas Frequentes</h3>
            <div class="faq-item">
                <span class="faq-question">O site é confiável?</span>
                <span class="faq-answer">Sim! Somos parceiros oficiais da Logzz e oferecemos pagamento seguro na entrega para sua total tranquilidade.</span>
            </div>
            <div class="faq-item">
                <span class="faq-question">Como acompanho meu pedido?</span>
                <span class="faq-answer">Assim que seu pedido for despachado, você receberá automaticamente o código de rastreio via e-mail e WhatsApp.</span>
            </div>
            <div class="faq-item">
                <span class="faq-question">E se eu não gostar do produto?</span>
                <span class="faq-answer">Você tem garantia total de 7 dias. Se não ficar satisfeito, devolvemos seu dinheiro sem burocracia.</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("""<div class="footer-dark"><p>© 2026 Top Ofertas Brasil. Todos os direitos reservados.</p></div>""", unsafe_allow_html=True)