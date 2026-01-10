import streamlit as st

# 1. Configuração da Página e Estilo Profissional
st.set_page_config(page_title="Top Ofertas - Oficial", page_icon="🛍️", layout="wide")

st.markdown("""
    <style>
    /* Cabeçalho Amarelo Estilo Mercado Livre */
    .header-container {
        background-color: #FFF159;
        padding: 10px 50px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 20px;
    }
    .logo-text {
        color: #2D3277;
        font-size: 24px;
        font-weight: bold;
        text-decoration: none;
    }
    /* Estilização dos Cards */
    .produto-card {
        border: 1px solid #ddd;
        border-radius: 8px;
        padding: 15px;
        background-color: white;
        transition: 0.3s;
        margin-bottom: 20px;
        color: #333;
    }
    .produto-card:hover {
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    .stButton>button {
        background-color: #3483FA !important;
        color: white !important;
        border-radius: 6px !important;
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# 2. Banco de Dados de Produtos com Categorias e Regiões
produtos = [
    {
        "nome": "Cinta Colete Modeladora",
        "categoria": "Saúde",
        "preco": 99.99,
        "img": "https://logzz-s3.s3.us-east-2.amazonaws.com/uploads/files/products/20240714-131356prok2m05.jpg",
        "link": "https://entrega.logzz.com.br/pay/mem6qq3rw/vlqxc-1-unidade",
        "regioes": ["SC", "SP", "PR"],
        "desc": "Compressão máxima e conforto total."
    },
    {
        "nome": "Depilador SkinLiss",
        "categoria": "Beleza",
        "preco": 89.90,
        "img": "https://a-static.mlcdn.com.br/470x352/depilador-yes-finishing-touch-sem-fio-ativacao-sensor-de-luz-rosto-e-corpo-depiladorlaser/connectcellcomercio/depiladorroxo16/958b6b6bada9045715419c0988f0a3b6.jpeg",
        "link": "https://entrega.logzz.com.br/pay/mem0go36g/azjol-skinliss-9999",
        "regioes": ["SP", "RJ"],
        "desc": "Tecnologia indolor para pele sensível."
    }
]

# 3. Cabeçalho Superior (Logo e Busca)
col_logo, col_busca = st.columns([1, 3])

with col_logo:
    st.markdown('<a class="logo-text">TOP OFERTAS</a>', unsafe_allow_html=True)

with col_busca:
    termo_busca = st.text_input("", placeholder="Buscar produtos, marcas e muito mais...", label_visibility="collapsed")

# 4. Localização (CEP) e Categorias
col_cep, col_cat = st.columns([1, 2])

with col_cep:
    # Simulação de localização baseada em prefixo de CEP
    cep_cliente = st.text_input("📍 Informe seu CEP", placeholder="00000-000")
    # Lógica simples de região para o exemplo
    regiao_detectada = "SC" if cep_cliente.startswith("8") else "SP" if cep_cliente.startswith("0") else "Outros"

with col_cat:
    categoria_selecionada = st.selectbox("Categorias", ["Todas", "Saúde", "Beleza", "Tecnologia", "Casa"])

st.write("---")

# 5. Filtragem de Produtos
produtos_filtrados = [
    p for p in produtos 
    if (termo_busca.lower() in p["nome"].lower()) and 
       (categoria_selecionada == "Todas" or p["categoria"] == categoria_selecionada)
]

# 6. Exibição da Vitrine
if not produtos_filtrados:
    st.warning("Nenhum produto encontrado para sua busca.")
else:
    # Mostra apenas produtos disponíveis para a região do CEP se preenchido
    if cep_cliente:
        st.info(f"Mostrando ofertas com entrega rápida para a região do CEP: {cep_cliente}")
    
    cols = st.columns(3)
    for idx, p in enumerate(produtos_filtrados):
        with cols[idx % 3]:
            st.markdown(f"""
                <div class="produto-card">
                    <img src="{p['img']}" style="width:100%; border-radius:5px;">
                    <h4 style="margin-top:10px;">{p['nome']}</h4>
                    <p style="color: #00a650; font-size: 20px; font-weight: bold;">R$ {p['preco']}</p>
                    <p style="font-size: 12px; color: #666;">{p['desc']}</p>
                </div>
            """, unsafe_allow_html=True)
            
            # Verificação de disponibilidade por Região
            if cep_cliente and regiao_detectada not in p["regioes"]:
                st.error("Indisponível para seu CEP")
            else:
                st.link_button("Comprar agora", p["link"])

# Rodapé de Suporte
st.sidebar.markdown("### Atendimento")
st.sidebar.link_button("WhatsApp Suporte 💬", "https://wa.me/5547997270179")