import streamlit as st

# 1. Configuração de Estilo e Página
st.set_page_config(page_title="Top Ofertas - Oficial", page_icon="🛍️", layout="wide")

# Pixel do Facebook
id_pixel = "2011090373033062" 
st.markdown(f"""
<script>
!function(f,b,e,v,n,t,s)
{{if(f.fbq)return;n=f.fbq=function(){{n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)}};
if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];
s.parentNode.insertBefore(t,s)}}(window, document,'script',
'https://connect.facebook.net/en_US/fbevents.js');
fbq('init', '{id_pixel}');
fbq('track', 'PageView');
</script>
""", unsafe_allow_html=True)

# CSS Customizado - Identidade Top Ofertas
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #ffffff; }
    .header-top { background-color: #FF8C00; padding: 10px; text-align: center; font-weight: bold; color: black; border-radius: 0 0 15px 15px; margin-bottom: 20px; }
    .produto-card { border: 1px solid #222; border-radius: 15px; padding: 20px; background-color: #0f0f0f; transition: 0.3s; text-align: center; }
    .produto-card:hover { border-color: #FF8C00; box-shadow: 0 0 15px rgba(255,140,0,0.2); }
    .banner-box { background: linear-gradient(90deg, #FF8C00 0%, #ffae42 100%); padding: 40px; border-radius: 20px; text-align: center; color: black; margin-bottom: 30px; }
    .stButton>button { background-color: #FF8C00 !important; color: black !important; border-radius: 10px !important; font-weight: bold !important; height: 50px; border: none; }
    .stButton>button:hover { background-color: #e67e00 !important; }
    h1, h2, h3 { color: #FF8C00 !important; }
    </style>
""", unsafe_allow_html=True)

# 2. Banco de Dados dos Produtos
produtos = {
    "cinta": {
        "nome": "Cinta Colete Modeladora Premium",
        "preco": "99,99",
        "img": "https://logzz-s3.s3.us-east-2.amazonaws.com/uploads/files/products/20240714-131356prok2m05.jpg",
        "link": "https://entrega.logzz.com.br/pay/mem6qq3rw/vlqxc-1-unidade",
        "regioes": ["SC", "SP", "PR"],
        "desc": "A Cinta Colete Modeladora é o segredo para uma silhueta perfeita e correção postural instantânea. Feita com material respirável de alta durabilidade.",
        "beneficios": ["✅ Redução imediata de medidas", "✅ Suporte lombar reforçado", "✅ Invisível sob a roupa"]
    },
    "depilador": {
        "nome": "Depilador SkinLiss Pro",
        "preco": "89,90",
        "img": "https://a-static.mlcdn.com.br/470x352/depilador-yes-finishing-touch-sem-fio-ativacao-sensor-de-luz-rosto-e-corpo-depiladorlaser/connectcellcomercio/depiladorroxo16/958b6b6bada9045715419c0988f0a3b6.jpeg",
        "link": "https://entrega.logzz.com.br/pay/mem0go36g/azjol-skinliss-9999",
        "regioes": ["SP", "RJ", "MG"],
        "desc": "Tecnologia de micro-oscilação que remove os pelos sem dor e sem irritação. Ideal para todas as partes do corpo.",
        "beneficios": ["✅ 100% Indolor", "✅ Bateria recarregável via USB", "✅ Sensor de contato inteligente"]
    }
}

# 3. Gerenciamento de Navegação (Session State)
if 'pagina' not in st.session_state:
    st.session_state.pagina = 'home'

def ir_para(nome_pagina):
    st.session_state.pagina = nome_pagina
    st.rerun()

# --- PÁGINA: VITRINE (HOME) ---
if st.session_state.pagina == 'home':
    st.markdown('<div class="header-top">🔥 OFERTAS DA SEMANA COM PAGAMENTO NA ENTREGA</div>', unsafe_allow_html=True)
    
    # Header Estilo Mercado Livre
    col_logo, col_search = st.columns([1, 2])
    with col_logo:
        st.title("TOP OFERTAS")
    with col_search:
        busca = st.text_input("", placeholder="🔍 O que você está procurando hoje?", label_visibility="collapsed")

    # Banner Promocional
    st.markdown("""
        <div class="banner-box">
            <h1>OFERTAS BLACK OUT ⚡</h1>
            <p>Produtos selecionados com entrega grátis e pagamento somente no ato do recebimento!</p>
        </div>
    """, unsafe_allow_html=True)

    st.subheader("Explore nossos Destaques")
    
    # Filtro de Busca Simples
    exibir = {k: v for k, v in produtos.items() if busca.lower() in v['nome'].lower()} if busca else produtos

    cols = st.columns(3)
    for idx, (id_p, p) in enumerate(exibir.items()):
        with cols[idx % 3]:
            st.markdown(f'<div class="produto-card">', unsafe_allow_html=True)
            st.image(p["img"], use_container_width=True)
            st.write(f"### {p['nome']}")
            st.write(f"## R$ {p['preco']}")
            if st.button("VER DETALHES", key=id_p):
                ir_para(id_p)
            st.markdown('</div>', unsafe_allow_html=True)

# --- PÁGINA: DETALHES DO PRODUTO ---
elif st.session_state.pagina in produtos:
    p = produtos[st.session_state.pagina]
    
    if st.button("⬅️ VOLTAR PARA A VITRINE"):
        ir_para('home')

    st.write("---")
    col_img, col_info = st.columns([1, 1])

    with col_img:
        st.image(p["img"], use_container_width=True)
    
    with col_info:
        st.title(p["nome"])
        st.markdown(f"<h2 style='color: #00ff00;'>R$ {p['preco']}</h2>", unsafe_allow_html=True)
        st.write("⭐⭐⭐⭐⭐ (4.9/5 - 124 avaliações)")
        
        st.write("---")
        st.subheader("📍 Verificar Disponibilidade")
        cep = st.text_input("Informe seu CEP para ver estoque na região:", placeholder="00000-000")
        
        if cep:
            st.success("✅ PRODUTO DISPONÍVEL! Entrega em até 24h.")
            st.link_button("🔥 COMPRAR E PAGAR NA ENTREGA", p["link"])
        
        st.write("---")
        st.subheader("Descrição do Produto")
        st.write(p["desc"])
        for ben in p["beneficios"]:
            st.write(ben)

# Rodapé Fixo
st.sidebar.write("---")
st.sidebar.markdown("### Suporte 24h")
st.sidebar.link_button("Falar no WhatsApp 💬", "https://wa.me/5547997270179")