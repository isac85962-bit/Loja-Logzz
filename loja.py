import streamlit as st

# 1. Configuração e Estilo de Alta Fidelidade
st.set_page_config(page_title="Top Ofertas - Oficial", page_icon="🛍️", layout="wide")

st.markdown("""
    <style>
    /* Fundo e Fonte */
    .stApp { background-color: #f5f5f5; color: #333333; }
    
    /* Cabeçalho Superior Amarelo */
    .main-header {
        background-color: #FFF159;
        padding: 15px 5%;
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin: -6rem -5rem 2rem -5rem;
    }
    
    /* Card de Produto Estilo Mercado Livre */
    .card-resumo {
        background-color: white;
        padding: 15px;
        border-radius: 8px;
        border: 1px solid #eeeeee;
        transition: 0.3s;
        cursor: pointer;
        text-align: center;
        height: 450px;
    }
    .card-resumo:hover {
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        border-color: #3483fa;
    }
    
    /* Imagens dos Produtos */
    .img-produto {
        max-height: 200px;
        object-fit: contain;
        margin-bottom: 15px;
    }

    /* Botões */
    .stButton>button {
        background-color: #3483fa !important;
        color: white !important;
        border: none !important;
        font-weight: bold !important;
        border-radius: 6px !important;
    }
    
    /* Preço em Destaque */
    .preco-texto {
        font-size: 24px;
        font-weight: 500;
        color: #333;
    }
    </style>
""", unsafe_allow_html=True)

# 2. Banco de Dados com Descrição e Detalhes
produtos = {
    "cinta": {
        "nome": "Cinta Colete Modeladora Ampla Carmigras",
        "preco": "99,90",
        "img": "https://logzz-s3.s3.us-east-2.amazonaws.com/uploads/files/products/20240714-131356prok2m05.jpg",
        "link": "https://entrega.logzz.com.br/pay/mem6qq3rw/vlqxc-1-unidade",
        "regioes": ["SC", "SP", "PR"],
        "desc": "A cinta original que você viu na TV. Modela sua cintura e melhora a postura instantaneamente.",
        "especificacoes": ["Material: Neoprene de alta qualidade", "Fechamento: Zíper e Velcro", "Cor: Preto"]
    },
    "depilador": {
        "nome": "Depilador SkinLiss - Finishing Touch",
        "preco": "89,90",
        "img": "https://a-static.mlcdn.com.br/470x352/depilador-yes-finishing-touch-sem-fio-ativacao-sensor-de-luz-rosto-e-corpo-depiladorlaser/connectcellcomercio/depiladorroxo16/958b6b6bada9045715419c0988f0a3b6.jpeg",
        "link": "https://entrega.logzz.com.br/pay/mem0go36g/azjol-skinliss-9999",
        "regioes": ["SP", "RJ", "MG"],
        "desc": "Depilação sem dor com tecnologia de micro-oscilação. Seguro para peles sensíveis.",
        "especificacoes": ["Bateria: Recarregável USB", "Uso: Seco", "Luz: LED Integrada"]
    }
}

# 3. Lógica de Navegação
if 'detalhe' not in st.session_state:
    st.session_state.detalhe = None

# Cabeçalho Principal (Fica em todas as páginas)
st.markdown('<div class="main-header"><h2 style="color:#2d3277; margin:0;">Top Ofertas - Oficial</h2></div>', unsafe_allow_html=True)

# --- VISÃO: DETALHES DO PRODUTO ---
if st.session_state.detalhe:
    p = produtos[st.session_state.detalhe]
    
    if st.button("⬅️ Voltar para a vitrine"):
        st.session_state.detalhe = None
        st.rerun()

    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.image(p["img"], use_container_width=True)
        
    with col2:
        st.title(p["nome"])
        st.markdown(f'<p class="preco-texto">R$ {p["preco"]}</p>', unsafe_allow_html=True)
        st.write("Disponível em estoque!")
        
        st.write("---")
        cep = st.text_input("📍 Informe seu CEP para entrega rápida:", placeholder="00000-000")
        if cep:
            st.success("✅ Disponível para sua região com pagamento na entrega!")
            st.link_button("COMPRAR AGORA", p["link"])
        
        st.subheader("Descrição")
        st.write(p["desc"])
        for esp in p["especificacoes"]:
            st.write(f"• {esp}")

# --- VISÃO: VITRINE ---
else:
    # Banner Rotativo (Simulado)
    st.image("https://images.tcdn.com.br/img/editor/up/649983/Banner_Topo_Desktop_1.jpg", use_container_width=True)
    
    st.subheader("Ofertas que você pode gostar")
    
    cols = st.columns(4) # 4 colunas para imagens menores
    for idx, (id_p, p) in enumerate(produtos.items()):
        with cols[idx]:
            st.markdown(f"""
                <div class="card-resumo">
                    <img src="{p['img']}" class="img-produto" style="width:100%;">
                    <h4 style="font-size:16px;">{p['nome']}</h4>
                    <p style="color:#00a650; font-weight:bold; font-size:20px;">R$ {p['preco']}</p>
                    <p style="font-size:12px; color:#666;">Frete Grátis</p>
                </div>
            """, unsafe_allow_html=True)
            
            if st.button(f"Ver detalhes", key=id_p):
                st.session_state.detalhe = id_p
                st.rerun()