import streamlit as st

# 1. Configuração da Página
st.set_page_config(page_title="Top Ofertas - Oficial", page_icon="🛍️", layout="wide")

# 2. Pixel do Facebook
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

# 3. Estilo CSS - PADRÃO TOP OFERTAS
st.markdown("""
    <style>
    /* Fundo Geral */
    .stApp { background-color: #050505; color: #ffffff; }
    
    /* Botões */
    .stButton>button { 
        width: 100%; 
        border-radius: 12px; 
        font-weight: bold; 
        height: 55px; 
        background-color: #FF8C00 !important; 
        color: white !important;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover { 
        background-color: #e67e00 !important; 
        transform: scale(1.02);
    }

    /* Cards de Produto */
    .produto-card { 
        text-align: center; 
        padding: 20px; 
        border: 2px solid #1a1a1a; 
        border-radius: 20px; 
        background-color: #0f0f0f; 
        transition: 0.4s;
    }
    .produto-card:hover { border-color: #FF8C00; box-shadow: 0px 0px 15px rgba(255, 140, 0, 0.3); }

    /* Caixas de Texto e Detalhes */
    .desc-box { 
        background-color: #0f0f0f; 
        padding: 25px; 
        border-radius: 15px; 
        border: 1px solid #222; 
        margin-top: 20px;
    }
    
    /* Títulos */
    h1, h2, h3 { color: #FF8C00 !important; }
    
    /* Input de CEP */
    div[data-baseweb="input"] {
        border-radius: 10px;
        border: 1px solid #FF8C00;
    }
    </style>
    """, unsafe_allow_html=True)

# 4. Banco de Dados dos Produtos
produtos = {
    "cinta": {
        "nome": "Cinta Colete Modeladora",
        "preco": "99,99",
        "img": "https://logzz-s3.s3.us-east-2.amazonaws.com/uploads/files/products/20240714-131356prok2m05.jpg",
        "link": "https://entrega.logzz.com.br/pay/mem6qq3rw/vlqxc-1-unidade",
        "regioes": ["SC", "SP", "PR"], 
        "desc": "A nossa Cinta Colete Premium foi desenhada para oferecer compressão máxima com conforto total. Ideal para uso diário, auxilia na postura e modela a cintura instantaneamente.",
        "beneficios": ["✅ Não enrola durante o uso", "✅ Material altamente respirável", "✅ Ajuste duplo de alta compressão"]
    },
    "depilador": {
        "nome": "Depilador SkinLiss",
        "preco": "99,99",
        "img": "