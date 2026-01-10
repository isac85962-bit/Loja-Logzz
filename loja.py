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

# 3. Estilo CSS Personalizado
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { width: 100%; border-radius: 8px; font-weight: bold; height: 50px; }
    .btn-comprar { background-color: #FF8C00 !important; color: white !important; font-size: 20px !important; }
    .produto-card { text-align: center; padding: 15px; border: 1px solid #333; border-radius: 15px; background-color: #161b22; transition: 0.3s; cursor: pointer; }
    .produto-card:hover { border-color: #FF8C00; }
    .desc-box { background-color: #161b22; padding: 20px; border-radius: 15px; border: 1px solid #333; }
    </style>
    """, unsafe_allow_html=True)

# 4. Banco de Dados dos Produtos (Configuração de Regiões aqui)
produtos = {
    "cinta": {
        "nome": "Cinta Colete Modeladora",
        "preco": "99,99",
        "img": "https://logzz-s3.s3.us-east-2.amazonaws.com/uploads/files/products/20240714-131356prok2m05.jpg",
        "link": "https://entrega.logzz.com.br/pay/mem6qq3rw/vlqxc-1-unidade",
        "regioes": ["SC", "SP", "PR"], # Atende SC, SP e PR
        "desc": "A nossa Cinta Colete Premium foi desenhada para oferecer compressão máxima com conforto total. Ideal para uso diário, auxilia na postura e modela a cintura instantaneamente.",
        "beneficios": ["✅ Não enrola", "✅ Material Respirável", "✅ Ajuste Duplo"]
    },
    "depilador": {
        "nome": "Depilador SkinLiss",
        "preco": "99,99",
        "img": "https://a-static.mlcdn.com.br/470x352/depilador-yes-finishing-touch-sem-fio-ativacao-sensor-de-luz-rosto-e-corpo-depiladorlaser/connectcellcomercio/depiladorroxo16/958b6b6bada9045715419c0988f0a3b6.jpeg",
        "link": "https://entrega.logzz.com.br/pay/mem0go36g/azjol-skinliss-9999",
        "regioes": ["SP"], # SÓ atende SP
        "desc": "Diga adeus à dor! O Depilador SkinLiss utiliza tecnologia de micro-oscilação para remover pelos indesejados sem cortes ou irritações. Portátil e recarregável.",
        "beneficios": ["✅ Sem dor", "✅ Sensor de Luz", "✅ Para todo o corpo"]
    }
}

# 5. Lógica de Navegação
if 'pagina' not in st.session_state:
    st.session_state.pagina = 'home'

def mudar_pagina(nome_pag):
    st.session_state.pagina = nome_pag
    st.rerun()

# --- PÁGINA: VITRINE (HOME) ---
if st.session_state.pagina == 'home':
    st.title("🛍️ Top Ofertas")
    st.write("<p style='text-align: center;'>Toque no produto para ver detalhes e disponibilidade</p>", unsafe_allow_html=True)
    st.write("---")
    
    cols = st.columns(2)
    for i, (id_p, p) in enumerate(produtos.items()):
        with cols[i % 2]:
            st.markdown(f'<div class="produto-card">', unsafe_allow_html=True)
            st.image(p["img"], use_container_width=True)
            st.subheader(p["nome"])
            st.write(f"### R$ {p['preco']}")
            if st.button(f"Ver Detalhes", key=id_p):
                mudar_pagina(id_p)
            st.markdown('</div>', unsafe_allow_html=True)

# --- PÁGINA: DETALHES DO PRODUTO ---
elif st.session_state.pagina in produtos:
    p = produtos[st.session_state.pagina]
    
    if st.button("⬅️ Voltar para a Loja"):
        mudar_pagina('home')
        
    col1, col2 = st.columns([1, 1.2])
    
    with col1:
        st.image(p["img"], use_container_width=True)
        
    with col2:
        st.title(p["nome"])
        st.write(f"## R$ {p['preco']}")
        st.write("---")
        
        # Verificador de CEP dinâmico
        st.subheader("🚚 Verificar Entrega")
        cep = st.text_input("Digite seu CEP:", placeholder="00000-000")
        
        if cep:
            # Simulamos a verificação da região pelo início do CEP (Exemplo simplificado)
            # Na vida real, você pode melhorar essa lógica
            if "SC" in p["regioes"] or "SP" in p["regioes"]: 
                # Aqui você pode customizar: Se o produto atende a região, sucesso!
                st.success(f"✅ Disponível para entrega rápida em sua região!")
                st.write("⏱️ **Prazo:** Receba em até 24h e pague na entrega.")
                st.link_button("🔥 FINALIZAR PEDIDO AGORA", p["link"], type="primary")
            else:
                st.error("❌ Desculpe, este produto específico não está disponível para sua região no momento.")

        st.markdown('<div class="desc-box">', unsafe_allow_html=True)
        st.write("### Descrição")
        st.write(p["desc"])
        for b in p["beneficios"]:
            st.write(b)
        st.markdown('</div>', unsafe_allow_html=True)

# 6. Suporte Lateral
st.sidebar.title("Suporte")
st.sidebar.link_button("Dúvidas no WhatsApp 💬", "https://wa.me/5547997270179")