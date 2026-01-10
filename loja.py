import streamlit as st

# 1. Configuração da Página
st.set_page_config(page_title="Top Ofertas - Oficial", page_icon="🛍️", layout="wide")

# 2. Pixel do Facebook (ID: 2011090373033062)
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

# 3. Estilo Visual Top Ofertas
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #ffffff; }
    .stButton>button { 
        width: 100%; border-radius: 12px; font-weight: bold; height: 55px; 
        background-color: #FF8C00 !important; color: white !important; border: none;
    }
    .produto-card { 
        text-align: center; padding: 20px; border: 2px solid #1a1a1a; 
        border-radius: 20px; background-color: #0f0f0f; transition: 0.4s;
    }
    .produto-card:hover { border-color: #FF8C00; }
    h1, h2, h3 { color: #FF8C00 !important; }
    </style>
    """, unsafe_allow_html=True)

# 4. Dados dos Produtos
produtos = {
    "cinta": {
        "nome": "Cinta Colete Modeladora",
        "preco": "99,99",
        "img": "https://logzz-s3.s3.us-east-2.amazonaws.com/uploads/files/products/20240714-131356prok2m05.jpg",
        "link": "https://entrega.logzz.com.br/pay/mem6qq3rw/vlqxc-1-unidade",
        "regioes": ["SC", "SP", "PR"],
        "desc": "Compressão máxima com conforto total para uso diário."
    },
    "depilador": {
        "nome": "Depilador SkinLiss",
        "preco": "99,99",
        "img": "https://a-static.mlcdn.com.br/470x352/depilador-yes-finishing-touch-sem-fio-ativacao-sensor-de-luz-rosto-e-corpo-depiladorlaser/connectcellcomercio/depiladorroxo16/958b6b6bada9045715419c0988f0a3b6.jpeg",
        "link": "https://entrega.logzz.com.br/pay/mem0go36g/azjol-skinliss-9999",
        "regioes": ["SP", "RJ"],
        "desc": "Tecnologia de micro-oscilação para remoção indesejada sem dor."
    }
}

# 5. Navegação Simples
if 'pagina' not in st.session_state: st.session_state.pagina = 'home'

if st.session_state.pagina == 'home':
    st.markdown("<h1 style='text-align: center;'>🛍️ Top Ofertas</h1>", unsafe_allow_html=True)
    cols = st.columns(2)
    for i, (id_p, p) in enumerate(produtos.items()):
        with cols[i]:
            st.markdown(f'<div class="produto-card">', unsafe_allow_html=True)
            st.image(p["img"], use_container_width=True)
            st.subheader(p["nome"])
            st.write(f"### R$ {p['preco']}")
            if st.button("VER DETALHES", key=id_p):
                st.session_state.pagina = id_p
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.pagina in produtos:
    p = produtos[st.session_state.pagina]
    if st.button("⬅️ VOLTAR"):
        st.session_state.pagina = 'home'
        st.rerun()
    
    col1, col2 = st.columns(2)
    with col1: st.image(p["img"], use_container_width=True)
    with col2:
        st.title(p["nome"])
        st.write(f"## R$ {p['preco']}")
        cep = st.text_input("Verificar CEP:")
        if cep:
            st.success("✅ DISPONÍVEL PARA SUA REGIÃO!")
            st.link_button("🔥 COMPRAR AGORA", p["link"])
        st.write(p["desc"])

st.sidebar.link_button("SUPORTE WHATSAPP 💬", "https://wa.me/5547997270179")