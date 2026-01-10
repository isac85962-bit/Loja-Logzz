import streamlit as st

# 1. CONFIGURAÇÕES E DESIGN COM CORES FORÇADAS (FIX VISIBILIDADE)
st.set_page_config(page_title="Top Ofertas | Oficial 2026", page_icon="🦊", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    
    /* Forçar cores globais para evitar textos invisíveis */
    html, body, [class*="st-"] { 
        font-family: 'Inter', sans-serif; 
        color: #1A1A1A !important; 
    }
    
    .stApp { background-color: #FFFFFF; }

    /* Cabeçalho */
    .header-top {
        background: linear-gradient(90deg, #FF8C00, #FFA500);
        padding: 20px 10%;
        display: flex; align-items: center; justify-content: space-between;
        margin: -6rem -5rem 20px -5rem;
        color: white !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    .header-top h1, .header-top span { color: white !important; }

    /* Barra de Urgência */
    .urgency-bar {
        background: #000000; color: #FFD700 !important;
        text-align: center; padding: 10px; font-size: 14px;
        margin: 0 -5rem 30px -5rem; font-weight: bold;
    }

    /* WhatsApp Flutuante */
    .whatsapp-float {
        position: fixed; width: 60px; height: 60px; bottom: 40px; right: 40px;
        background-color: #25d366; border-radius: 50px;
        display: flex; align-items: center; justify-content: center;
        z-index: 1000; box-shadow: 2px 2px 15px rgba(0,0,0,0.3);
    }

    /* Cards de Produto */
    .product-card {
        background: #FFFFFF; border-radius: 15px; padding: 20px;
        text-align: center; border: 1px solid #E0E0E0;
        transition: 0.3s; margin-bottom: 20px;
    }
    .product-card:hover { border-color: #FF8C00; transform: translateY(-5px); }
    .product-card p { color: #333333 !important; }

    /* SEÇÃO FAQ - VISIBILIDADE MÁXIMA */
    .faq-container {
        background: #F9F9F9; padding: 40px; border-radius: 20px;
        margin: 40px 0; border: 1px solid #EEEEEE;
    }
    .faq-q { color: #111111 !important; font-weight: 800; font-size: 18px; margin-top: 20px; display: block; }
    .faq-a { color: #444444 !important; font-size: 16px; margin-bottom: 10px; display: block; line-height: 1.6; }

    /* Botão de Compra */
    .stButton > button {
        background: #FF8C00 !important; color: white !important;
        border-radius: 10px !important; font-weight: 900 !important;
        height: 55px; border: none; width: 100%; font-size: 18px !important;
    }

    /* Rodapé */
    .footer {
        background: #111111; color: #BBBBBB !important; padding: 60px 10%;
        margin: 50px -5rem -5rem -5rem; text-align: center;
    }
    .footer h4 { color: #FF8C00 !important; }
    </style>

    <a href="https://wa.me/5500000000000" class="whatsapp-float" target="_blank">
        <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" width="35">
    </a>
""", unsafe_allow_html=True)

# 2. BANCO DE DATOS (PRODUTOS + CATEGORIAS + COPY AIDA)
produtos = {
    "cinta": {
        "nome": "Cinta Modeladora Yoga Premium 2026",
        "preco": "97,90", "antes": "197,00",
        "img": "https://logzz-s3.s3.us-east-2.amazonaws.com/uploads/files/products/20240714-131356prok2m05.jpg",
        "link": "https://entrega.logzz.com.br/pay/mem6qq3rw/vlqxc-1-unidade",
        "aida": "🔥 **ATENÇÃO:** Recupere sua silhueta instantaneamente!\n\n✨ **DESEJO:** Sinta-se poderosa em qualquer roupa com nossa tecnologia de compressão invisível.\n\n⚡ **AÇÃO:** Poucas unidades com Frete Grátis!"
    },
    "depilador": {
        "nome": "Depilador SkinLiss Pro Max",
        "preco": "84,90", "antes": "159,00",
        "img": "https://a-static.mlcdn.com.br/470x352/depilador-yes-finishing-touch-sem-fio-ativacao-sensor-de-luz-rosto-e-corpo-depiladorlaser/connectcellcomercio/depiladorroxo16/958b6b6bada9045715419c0988f0a3b6.jpeg",
        "link": "https://entrega.logzz.com.br/pay/mem0go36g/azjol-skinliss-9999",
        "aida": "🔥 **ATENÇÃO:** Depilação sem dor e sem cortes agora é real!\n\n✨ **DESEJO:** Pele de seda em minutos, no conforto da sua casa.\n\n⚡ **AÇÃO:** Pague apenas na entrega clicando abaixo!"
    },
    "massagem": {
        "nome": "Massageador Cervical Inteligente",
        "preco": "137,90", "antes": "249,00",
        "img": "https://m.media-amazon.com/images/I/61K9UqL8T9L._AC_SL1500_.jpg",
        "link": "#",
        "aida": "🔥 **TENDÊNCIA 2026:** O fim das dores no pescoço após o trabalho.\n\n✨ **DESEJO:** Relaxamento profundo com tecnologia de infravermelho.\n\n⚡ **AÇÃO:** Oferta de lançamento exclusiva!"
    }
}

# 3. NAVEGAÇÃO
if 'page' not in st.session_state: st.session_state.page = "home"
if 'prod_id' not in st.session_state: st.session_state.prod_id = None

st.markdown('<div class="header-top"><h1>🦊 TOP OFERTAS</h1><span>⭐ Qualidade Garantida</span></div>', unsafe_allow_html=True)
st.markdown('<div class="urgency-bar">⚠️ ÚLTIMAS HORAS: FRETE GRÁTIS + PAGAMENTO NA ENTREGA ⚠️</div>', unsafe_allow_html=True)

# --- PÁGINA DE DETALHES ---
if st.session_state.page == "detalhes":
    p = produtos[st.session_state.prod_id]
    if st.button("⬅ VOLTAR PARA A VITRINE"):
        st.session_state.page = "home"
        st.rerun()
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.image(p["img"], use_container_width=True)
    with col2:
        st.subheader(p["nome"])
        st.markdown(f"#### <span style='color:#BBB; text-decoration:line-through;'>De R$ {p['antes']}</span>", unsafe_allow_html=True)
        st.markdown(f"## <span style='color:#FF8C00;'>Por R$ {p['preco']}</span>", unsafe_allow_html=True)
        st.write("---")
        st.markdown(p["aida"]) # COPY AIDA (OPÇÃO A)
        st.write("---")
        st.link_button("COMPRAR AGORA (PAGAR NA ENTREGA) 🛒", p["link"])

# --- PÁGINA HOME ---
else:
    st.image("https://http2.mlstatic.com/D_NQ_648500-MLA73797871625_012024-OO.webp", use_container_width=True)
    
    # OPÇÃO C: Categorias
    t1, t2 = st.tabs(["🔥 OFERTAS EM DESTAQUE", "🚀 TENDÊNCIAS 2026"])
    
    with t1:
        c = st.columns(3)
        for i, (pid, p) in enumerate(list(produtos.items())[:2]):
            with c[i]:
                st.markdown(f"""<div class="product-card">
                    <img src="{p['img']}" style="width:100%; border-radius:10px;">
                    <p style="font-weight:bold; margin-top:15px;">{p['nome']}</p>
                    <p style="color:#FF8C00; font-size:22px; font-weight:900;">R$ {p['preco']}</p>
                </div>""", unsafe_allow_html=True)
                if st.button("VER DETALHES", key=pid):
                    st.session_state.prod_id = pid
                    st.session_state.page = "detalhes"
                    st.rerun()

    with t2:
        c = st.columns(3)
        with c[0]:
            p = produtos["massagem"]
            st.markdown(f"""<div class="product-card">
                <span style="background:#000; color:#FFD700; padding:2px 10px; border-radius:5px; font-size:10px;">NOVIDADE</span>
                <img src="{p['img']}" style="width:100%; border-radius:10px; margin-top:10px;">
                <p style="font-weight:bold; margin-top:15px;">{p['nome']}</p>
                <p style="color:#FF8C00; font-size:22px; font-weight:900;">R$ {p['preco']}</p>
            </div>""", unsafe_allow_html=True)
            st.button("VER LANÇAMENTO", key="trend1")

    # OPÇÃO B: FAQ (TEXTOS AGORA 100% VISÍVEIS)
    st.markdown("""
        <div class="faq-container">
            <h2 style="text-align:center; color:#111 !important; margin-bottom:30px;">🙋‍♂️ Dúvidas Frequentes</h2>
            
            <span class="faq-q">1. O site é realmente seguro?</span>
            <span class="faq-a">Sim! Nossa parceria com a Logzz permite que você pague apenas quando o produto chegar na sua porta. Risco zero para você.</span>
            
            <span class="faq-q">2. Qual o prazo de entrega?</span>
            <span class="faq-a">Entregamos em todo o Brasil de 3 a 9 dias úteis. Você recebe o código de rastreio no seu WhatsApp em até 24h.</span>
            
            <span class="faq-q">3. E se eu quiser devolver?</span>
            <span class="faq-a">Você tem 7 dias de garantia total. Se não gostar, devolvemos seu dinheiro sem perguntas.</span>
            
            <span class="faq-q">4. Como falo com o suporte?</span>
            <span class="faq-a">Basta clicar no ícone do WhatsApp que está aparecendo no canto da sua tela para falar com um atendente humano agora.</span>
        </div>
    """, unsafe_allow_html=True)

# RODAPÉ FINAL
st.markdown("""
    <div class="footer">
        <div style="display:flex; justify-content:space-around; flex-wrap:wrap; text-align:left;">
            <div style="max-width:300px;">
                <h4>SOBRE A FOX</h4>
                <p>Sua loja de confiança para produtos inovadores. Focamos em facilitar sua vida com tecnologia e preço justo.</p>
            </div>
            <div style="max-width:300px;">
                <h4>AJUDA</h4>
                <p>Rastrear Pedido<br>Políticas de Reembolso<br>Termos de Uso</p>
            </div>
            <div style="max-width:300px;">
                <h4>CONTATO</h4>
                <p>atendimento@foxofertas.com<br>Seg a Sex: 09h às 18h</p>
            </div>
        </div>
        <hr style="border-color:#333; margin:40px 0;">
        <p style="font-size:12px;">© 2026 FOX TOP OFERTAS - CNPJ 00.000.000/0001-00 - Jaraguá do Sul, SC</p>
    </div>
""", unsafe_allow_html=True)