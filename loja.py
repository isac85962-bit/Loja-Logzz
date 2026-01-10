import streamlit as st

# 1. Configuração da Página
st.set_page_config(page_title="Top Ofertas - Oficial", page_icon="🛍️", layout="wide")

# 2. SEU PIXEL (ID: 2011090373033062)
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
    .status-estoque { background-color: #222; padding: 10px; border-radius: 10px; border-left: 5px solid #FF8C00; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# 4. Cabeçalho
st.title("🛍️ Top Ofertas")

# --- NOVO: VERIFICADOR DE DISPONIBILIDADE ---
st.markdown('<div class="status-estoque">', unsafe_allow_html=True)
st.write("### 🚚 Verificar Disponibilidade e Prazo")
cep = st.text_input("Digite seu CEP para consultar estoque na região:", placeholder="Ex: 01001-000")

if cep:
    if len(cep.replace("-","")) >= 8:
        st.success("✅ **Estoque Disponível!** Temos unidades prontas para envio imediato na sua região.")
        st.info("⚡ **Prazo:** Entrega em até 24h com pagamento na porta!")
    else:
        st.warning("Por favor, digite um CEP válido com 8 números.")
st.markdown('</div>', unsafe_allow_html=True)

# 5. Vitrine de Produtos
produtos = [
    {"nome": "Cinta Colete Modeladora", "preco": "99,99", "link": "https://entrega.logzz.com.br/pay/mem6qq3rw/vlqxc-1-unidade", "img": "https://logzz-s3.s3.us-east-2.amazonaws.com/uploads/files/products/20240714-131356prok2m05.jpg"},
    {"nome": "Depilador SkinLiss", "preco": "99,99", "link": "https://entrega.logzz.com.br/pay/mem0go36g/azjol-skinliss-9999", "img": "https://a-static.mlcdn.com.br/470x352/depilador-yes-finishing-touch-sem-fio-ativacao-sensor-de-luz-rosto-e-corpo-depiladorlaser/connectcellcomercio/depiladorroxo16/958b6b6bada9045715419c0988f0a3b6.jpeg"}
]

cols = st.columns(2)
for i, p in enumerate(produtos):
    with cols[i]:
        st.markdown('<div class="produto-card">', unsafe_allow_html=True)
        st.image(p["img"], width=250)
        st.subheader(p["nome"])
        st.write(f"## R$ {p['preco']}")
        st.link_button("COMPRAR AGORA", p["link"])
        st.markdown('</div>', unsafe_allow_html=True)

# 6. Barra Lateral com Regiões Atendidas
st.sidebar.title("📍 Regiões Atendidas")
st.sidebar.info("Entregamos com motoboy em todas as capitais e regiões metropolitanas de SP, RJ, MG, PR, SC e RS.")
st.sidebar.write("---")
st.sidebar.link_button("Dúvidas no WhatsApp 💬", "https://wa.me/5547997270179")