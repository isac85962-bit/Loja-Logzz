import streamlit as st

# 1. CONFIGURAÇÕES E DESIGN UX/UI (O SEGREDO DA CONVERSÃO)
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

    /* BARRA DE URGÊNCIA (PSICOLOGIA DE VENDAS) */
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
    .whatsapp-float:hover { transform: scale(1.1); background-color: #128C7E; }

    /* CARDS DE PRODUTO CLEAN */
    .product-card {
        background: white; border-radius: 15px; padding: 20px;
        text-align: center; transition: 0.4s; border: 1px solid #EEE;
        height: 100%;
    }
    .product-card:hover { transform: translateY(-10px); border-color: #FF8C00; box-shadow: 0 15px 30px rgba(255,140,0,0.1); }
    
    .price-now { color: #FF8C00; font-size: 26px; font-weight: 800; }
    .price-before { color: #BBB; text-decoration: line-through; font-size: 14px; }

    /* BOTÃO CTA ESTILO "COMPRA GARANTIDA" */
    .stButton > button {
        background: #FF8C00 !important; color: white !important;
        border-radius: 12px !important; font-weight: 800 !important;
        border: none; width: 100%; height: 50px; transition: 0.3s;
    }
    .stButton > button:hover { background: #E67E00 !important; transform: scale(1.03); }

    /* FAQ E FOOTER */
    .faq-box { background: #FFF; padding: 30px; border-radius: 15px; margin-top: 40px; border-left: 5px solid #FF8C00; }
    .footer-dark { background: #111; color: #777; padding: 50px 10%; margin: 50px -5rem -5rem -5rem; text-align: center; }
    </style>

    <a href="https://wa.me/5547997270179" class="whatsapp-float" target="_blank">
        <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" width="35">
    </a>
""", unsafe_allow_html=True)

# 2. BANCO DE DADOS INTEGRADO (PRODUTOS + TENDÊNCIAS + COPY AIDA)
produtos = {
    "cinta": {
        "nome": "Cinta Modeladora Yoga Premium",
        "tagline": "🔥 Atenção: Recupere sua silhueta e confiança em segundos!",
        "preco_antigo": "197,90", "preco": "97,90",
        "img": "https://logzz-s3.s3.us-east-2.amazonaws.com/uploads/files/products/20240714-131356prok2m05.jpg",
        "link": "https://entrega.logzz.com.br/pay/mem6qq3rw/vlqxc-1-unidade",
        "cat": "Saúde",
        "copy": "Tecnologia Soft-Touch que molda sem machucar. Ideal para uso diário e recuperação pós-parto."
    },
    "depilador": {
        "nome": "Depilador Laser-Light SkinLiss 2026",
        "tagline": "✨ Pele de seda sem dor, cortes ou alergias!",
        "preco_antigo": "159,00", "preco": "84,90",
        "img": "https://a-static.mlcdn.com.br/470x352/depilador-yes-finishing-touch-sem-fio-ativacao-sensor-de-luz-rosto-e-corpo-depiladorlaser/connectcellcomercio/depiladorroxo16/958b6b6bada9045715419c0988f0a3b6.jpeg",
        "link": "https://entrega.logzz.com.br/pay/mem0go36g/azjol-skinliss-9999",
        "cat": "Beleza",
        "copy": "Remoção instantânea com micro-oscilação. Seguro para todas as áreas do corpo e rosto."
    },
    "mop": {
        "nome": "Mop Giratório 360 Limpeza Pesada",
        "tagline": "🏠 Esqueça o pano de chão e proteja suas mãos!",
        "preco_antigo": "189,90", "preco": "129,90",
        "img": "https://images-americanas.b2w.io/produtos/01/00/item/133668/2/133668276_1GG.jpg",
        "link": "#",
        "cat": "Casa",
        "copy": "Limpa, lava e seca. O sistema de centrifugação garante 0% de contato com a sujeira."
    }
}

# 3. LÓGICA DE NAVEGAÇÃO
if 'pagina' not in st.session_state: st.session_state.pagina = "home"
if 'produto_id' not in st.session_state: st.session_state.produto_id = None

# HEADER E BANNER DE URGÊNCIA
st.markdown('<div class="header-top"><h2>🦊 Top Ofertas</h2><span>🚚 Frete Grátis para todo Brasil</span></div>', unsafe_allow_html=True)
st.markdown('<div class="urgency-bar">⚡ OFERTA TERMINA EM 05:14 - APROVEITE O PREÇO DE ATACADO!</div>', unsafe_allow_html=True)

# --- PÁGINA: DETALHES DO PRODUTO (CONVERSÃO MÁXIMA) ---
if st.session_state.pagina == "detalhes":
    p = produtos[st.session_state.produto_id]
    if st.button("⬅ VOLTAR À LOJA"):
        st.session_state.pagina = "home"
        st.rerun()

    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.image(p["img"], use_container_width=True)
    with col2:
        st.markdown(f"<p style='color:#FF8C00; font-weight:bold; margin:0;'>{p['tagline']}</p>", unsafe_allow_html=True)
        st.title(p["nome"])
        st.markdown(f"⭐ ⭐ ⭐ ⭐ ⭐ (4.9/5 de satisfação)")
        st.markdown(f"<span class='price-before'>De R$ {p['preco_antigo']}</span><br><span class='price-now'>R$ {p['preco']}</span>", unsafe_allow_html=True)
        st.info("🔥 Mais de 1.400 unidades vendidas este mês!")
        
        st.write("---")
        st.markdown(f"### 💎 Descrição Premium\n{p['copy']}")
        st.write("• **Pagamento:** Pague na entrega via Logzz\n• **Garantia:** 30 dias de satisfação\n• **Envio:** Imediato com rastreio")
        
        st.link_button("QUERO GARANTIR O MEU AGORA 🛒", p["link"])

# --- PÁGINA: HOME (VITRINE) ---
else:
    # Banner Principal Rotativo (Simulado)
    st.image("https://http2.mlstatic.com/D_NQ_648500-MLA73797871625_012024-OO.webp", use_container_width=True)
    
    # Seções de Categorias
    tab1, tab2, tab3 = st.tabs(["🔥 TODAS AS OFERTAS", "🏠 CASA & COZINHA", "✨ SAÚDE & BELEZA"])
    
    with tab1:
        cols = st.columns(3)
        for idx, (pid, p) in enumerate(produtos.items()):
            with cols[idx % 3]:
                st.markdown(f"""
                    <div class="product-card">
                        <img src="{p['img']}" style="width:100%; border-radius:10px;">
                        <p style="margin-top:10px; font-weight:700; height:45px; overflow:hidden;">{p['nome']}</p>
                        <p class="price-before">R$ {p['preco_antigo']}</p>
                        <p class="price-now">R$ {p['preco']}</p>
                        <p style="color:#00A650; font-size:12px; font-weight:bold;">⚡ Chega em 3 dias</p>
                    </div>
                """, unsafe_allow_html=True)
                if st.button("VER DETALHES", key=pid):
                    st.session_state.produto_id = pid
                    st.session_state.pagina = "detalhes"
                    st.rerun()

    # --- SEÇÃO FAQ (QUEBRA DE OBJEÇÕES) ---
    st.markdown("""
        <div class="faq-box">
            <h3 style="color:#333; margin-bottom:20px;">🙋‍♂️ Perguntas Frequentes</h3>
            <p><b>O site é confiável?</b><br>Sim! Somos parceiros da Logzz e oferecemos pagamento na entrega para sua total segurança.</p>
            <p><b>Como acompanho meu pedido?</b><br>Assim que o despacho for feito, você receberá o código de rastreio via e-mail e WhatsApp.</p>
            <p><b>E se eu não gostar do produto?</b><br>Você tem 7 dias para devolução grátis e reembolso total.</p>
        </div>
    """, unsafe_allow_html=True)

# --- RODAPÉ PROFISSIONAL ---
st.markdown("""
    <div class="footer-dark">
        <div style="display:flex; justify-content:space-around; flex-wrap:wrap; text-align:left;">
            <div style="width:250px;">
                <h4 style="color:white;">FOX TOP OFERTAS</h4>
                <p style="font-size:13px;">Sua curadoria de produtos inteligentes e inovadores. Qualidade testada e aprovada.</p>
            </div>
            <div style="width:250px;">
                <h4 style="color:white;">CONTATO</h4>
                <p style="font-size:13px;">WhatsApp: (00) 00000-0000<br>E-mail: suporte@topofertas.com</p>
            </div>
            <div style="width:250px;">
                <h4 style="color:white;">SEGURANÇA</h4>
                <p style="font-size:13px;">🛡️ Compra Garantida<br>📦 Entrega Rápida<br>🔒 Site Seguro</p>
            </div>
        </div>
        <hr style="border-color:#333; margin:30px 0;">
        <p style="font-size:11px;">© 2026 Top Ofertas Brasil. CNPJ: 00.000.000/0001-00. Todos os direitos reservados.</p>
    </div>
""", unsafe_allow_html=True)