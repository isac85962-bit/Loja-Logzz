import streamlit as st

# 1. Configurações e CSS de Alta Densidade
st.set_page_config(page_title="Top Ofertas - Oficial", page_icon="🦊", layout="wide")

st.markdown("""
    <style>
    /* Fundo geral */
    .stApp { background-color: #F5F5F5; }
    
    /* Remove espaçamentos desnecessários do Streamlit */
    .block-container { padding-top: 1rem; padding-bottom: 5rem; }

    /* HEADER: Barra Superior Laranja Vibrante */
    .header-container {
        background-color: #FFF159; /* Amarelo ML */
        padding: 15px 20px;
        border-bottom: 1px solid #ddd;
        display: flex; align-items: center; justify-content: space-between;
        margin: -6rem -5rem 1rem -5rem; /* Força ocupar topo total */
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }
    
    /* BARRA DE BENEFÍCIOS (O segredo para não ficar seco) */
    .benefit-bar {
        background-color: white;
        padding: 15px;
        margin: 10px 0 30px 0;
        border-radius: 8px;
        display: flex; justify-content: space-around;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        font-size: 14px; color: #333;
    }
    
    /* ESTILO DOS CARDS DE PRODUTO */
    .card-box {
        background: white;
        border-radius: 8px;
        border: 1px solid #e6e6e6;
        padding: 0px; /* Padding zero para imagem encostar */
        transition: 0.3s;
        height: 100%;
        overflow: hidden; /* Para o botão não sair */
    }
    .card-box:hover {
        box-shadow: 0 10px 20px rgba(0,0,0,0.15);
        transform: translateY(-2px);
    }
    .card-content { padding: 15px; text-align: left; }
    .tag-frete {
        background-color: #00a650; color: white;
        font-size: 10px; padding: 2px 6px; border-radius: 3px;
        font-weight: bold; display: inline-block; margin-bottom: 5px;
    }
    .preco-destaque { font-size: 22px; color: #333; font-weight: 400; }
    .parcelamento { font-size: 12px; color: #00a650; }

    /* Estilo do Botão Streamlit para parecer parte do Card */
    .stButton > button {
        width: 100%;
        border-radius: 0 0 8px 8px !important; /* Arredonda só embaixo */
        background-color: #3483fa !important; /* Azul Compra */
        color: white !important;
        border: none;
        font-weight: bold;
        margin-top: 0px;
    }

    /* FOOTER (Rodapé) */
    .footer {
        background-color: #333; color: white;
        padding: 40px; text-align: center;
        margin: 50px -5rem -5rem -5rem;
    }
    </style>
""", unsafe_allow_html=True)

# 2. BANCO DE DADOS (Seus Produtos)
produtos = {
    "cinta": {
        "nome": "Cinta Colete Modeladora Ampla - Reduz Medidas",
        "preco": "99,99",
        "img": "https://logzz-s3.s3.us-east-2.amazonaws.com/uploads/files/products/20240714-131356prok2m05.jpg",
        "categoria": "Moda e Beleza",
        "link": "https://entrega.logzz.com.br/pay/mem6qq3rw/vlqxc-1-unidade",
        "descricao": "Cinta de alta compressão. Não enrola, corrige postura e afina a cintura.",
        "topicos": ["✅ 12 Barbatanas de Silicone", "✅ Tecido Respirável", "✅ Ajuste em 3 níveis"]
    },
    "depilador": {
        "nome": "Depilador SkinLiss Pro - Sem Dor",
        "preco": "89,90",
        "img": "https://a-static.mlcdn.com.br/470x352/depilador-yes-finishing-touch-sem-fio-ativacao-sensor-de-luz-rosto-e-corpo-depiladorlaser/connectcellcomercio/depiladorroxo16/958b6b6bada9045715419c0988f0a3b6.jpeg",
        "categoria": "Moda e Beleza",
        "link": "https://entrega.logzz.com.br/pay/mem0go36g/azjol-skinliss-9999",
        "descricao": "Remova pelos indesejados em segundos com a tecnologia de luz ativa.",
        "topicos": ["✅ Bateria Recarregável", "✅ Portátil", "✅ Para todas as áreas"]
    },
     "mop": {
        "nome": "Mop Giratório Limpeza Prática 360",
        "preco": "129,90",
        "img": "https://m.media-amazon.com/images/I/61pInh3S8zL._AC_SL1200_.jpg",
        "categoria": "Casa",
        "link": "#",
        "descricao": "Limpeza completa sem sujar as mãos. Centrifuga e seca.",
        "topicos": ["✅ Balde reforçado", "✅ Cabo extensor", "✅ Microfibra absorvente"]
    }
}

# 3. Lógica de Navegação
if 'detalhe_id' not in st.session_state: st.session_state.detalhe_id = None

# --- HEADER (Onde fica o Mascote) ---
st.markdown(f"""
    <div class="header-container">
        <div style="display:flex; align-items:center; gap:15px;">
            <img src="https://raw.githubusercontent.com/isac85962-bit/Loja-Logzz/main/WhatsApp%20Image%202026-01-09%20at%2017.29.39.jpeg" width="50" style="border-radius:50%; border:2px solid white;">
            <div>
                <h2 style="margin:0; color:#2d3277; font-size:24px;">Top OFERTAS</h2>
                <small style="color:#2d3277;">O melhor preço do Brasil</small>
            </div>
        </div>
        <div style="background:white; padding:8px 15px; border-radius:20px; box-shadow:0 2px 5px rgba(0,0,0,0.1);">
            🔍 Buscar produtos...
        </div>
    </div>
""", unsafe_allow_html=True)

# --- TELA DE DETALHES DO PRODUTO ---
if st.session_state.detalhe_id:
    p = produtos[st.session_state.detalhe_id]
    
    if st.button("⬅️ Voltar para o início"):
        st.session_state.detalhe_id = None
        st.rerun()

    # Layout de Detalhes (Fundo Branco centralizado)
    with st.container():
        st.markdown('<div style="background:white; padding:30px; border-radius:10px; margin-top:20px;">', unsafe_allow_html=True)
        col1, col2 = st.columns([1, 1.2])
        
        with col1:
            st.image(p["img"], use_container_width=True)
        
        with col2:
            st.caption("Novo | +1000 vendidos")
            st.title(p["nome"])
            st.markdown(f"""
                <h1 style="color:#333; font-weight:300; font-size:36px;">R$ {p['preco']}</h1>
                <p style="color:#00a650; font-weight:bold;">em 12x R$ {float(p['preco'].replace(',','.'))/12:.2f} sem juros</p>
                <p style="color:#00a650; font-weight:bold;">Frete Grátis para todo o país 🚚</p>
            """, unsafe_allow_html=True)
            
            st.write("---")
            st.write(f"**O que você precisa saber:**")
            for t in p["topicos"]: st.write(t)
            
            st.write("")
            st.link_button("COMPRAR AGORA", p["link"], use_container_width=True)
            
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Descrição extra embaixo
        st.markdown(f"""
            <div style="background:white; padding:30px; border-radius:10px; margin-top:20px;">
                <h3>Descrição</h3>
                <p>{p['descricao']}</p>
            </div>
        """, unsafe_allow_html=True)

# --- TELA INICIAL (VITRINE) ---
else:
    # 1. Banner Principal (Carrossel Simulado)
    st.image("https://http2.mlstatic.com/D_NQ_648500-MLA73797871625_012024-OO.webp", use_container_width=True)

    # 2. BARRA DE CONFIANÇA (O toque profissional)
    st.markdown("""
        <div class="benefit-bar">
            <div>💳 <b>Pagamento Rápido</b><br><span style="color:grey; font-size:12px">Pague na entrega ou Pix</span></div>
            <div style="border-left:1px solid #eee; padding-left:20px;">🚚 <b>Frete Grátis</b><br><span style="color:grey; font-size:12px">Em produtos selecionados</span></div>
            <div style="border-left:1px solid #eee; padding-left:20px;">🛡️ <b>Compra Garantida</b><br><span style="color:grey; font-size:12px">Sua satisfação ou dinheiro de volta</span></div>
        </div>
    """, unsafe_allow_html=True)

    # 3. Listagem de Produtos
    st.markdown("### 🔥 Ofertas do Dia")
    
    colunas = st.columns(4) # Grid de 4
    ids_produtos = list(produtos.keys())
    
    for i, col in enumerate(colunas):
        if i < len(ids_produtos):
            pid = ids_produtos[i]
            p = produtos[pid]
            
            with col:
                # O HTML cria o visual do card
                st.markdown(f"""
                    <div class="card-box">
                        <div style="height:200px; display:flex; align-items:center; justify-content:center; padding:10px;">
                            <img src="{p['img']}" style="max-height:100%; max-width:100%;">
                        </div>
                        <div class="card-content">
                            <span class="tag-frete">CHEGA AMANHÃ</span>
                            <p style="font-size:14px; margin-bottom:5px; height:40px; overflow:hidden;">{p['nome']}</p>
                            <span class="preco-destaque">R$ {p['preco']}</span><br>
                            <span class="parcelamento">10x R$ 9,90 sem juros</span>
                        </div>
                    </div>
                """, unsafe_allow_html=True)
                
                # Botão do Streamlit colado visualmente no card
                if st.button("Ver Detalhes", key=pid):
                    st.session_state.detalhe_id = pid
                    st.rerun()

# --- RODAPÉ (FOOTER) ---
st.markdown("""
    <div class="footer">
        <p><b>Top Ofertas © 2026</b><br>
        CNPJ: 00.000.000/0001-00<br>
        Rua do Comércio, 123 - São Paulo, SP</p>
        <p style="font-size:12px; color:#888;">Imagens meramente ilustrativas.</p>
    </div>
""", unsafe_allow_html=True)