import streamlit as st

# 1. Configuração da Página
st.set_page_config(page_title="Top Ofertas - Oficial", page_icon="🛍️", layout="wide")

# 2. SEU NOVO PIXEL ATUALIZADO
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

# 3. Estilo Visual
st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 10px; background-color: #FF8C00; color: white; font-weight: bold; height: 45px; border: none; }
    .produto-card { text-align: center; padding: 20px; border: 1px solid #333; border-radius: 15px; background-color: #111; margin-bottom: 20px; }
    h1 { color: #FF8C00; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# 4. Conteúdo da Loja
st.title("🛍️ Top Ofertas")
st.write("<p style='text-align: center;'>As melhores ofertas com pagamento na entrega!</p>", unsafe_allow_html=True)

produtos = [
    {
        "nome": "Cinta Colete Modeladora", 
        "preco": "99,99", 
        "link": "https://entrega.logzz.com.br/pay/mem6qq3rw/vlqxc-1-unidade",
        "img": "https://logzz-s3.s3.us-east-2.amazonaws.com/uploads/files/products/20240714-131356prok2m05.jpg"
    },
    {
        "nome": "Depilador SkinLiss", 
        "preco": "99,99", 
        "link": "https://entrega.logzz.com.br/pay/mem0go36g/azjol-skinliss-9999",
        "img": "https://a-static.mlcdn.com.br/470x352/depilador-yes-finishing-touch-sem-fio-ativacao-sensor-de-luz-rosto-e-corpo-depiladorlaser/connectcellcomercio/depiladorroxo16/958b6b6bada9045715419c0988f0a3b6.jpeg"
    }
]

# Vitrine em 2 colunas para melhor visualização
cols = st.columns(2)
for i, p in enumerate(produtos):
    with cols[i]:
        st.markdown('<div class="produto-card">', unsafe_allow_html=True)
        st.image(p["img"], width=250)
        st.subheader(p["nome"])
        st.write(f"## R$ {p['preco']}")
        st.link_button("COMPRAR AGORA", p["link"])
        st.markdown('</div>', unsafe_allow_html=True)

# 5. Suporte Lateral
st.sidebar.title("Top Ofertas")
st.sidebar.link_button("Falar no WhatsApp 💬", "https://wa.me/5547997270179")