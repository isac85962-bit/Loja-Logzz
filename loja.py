import streamlit as st

# 1. CONFIGURAÇÕES GERAIS E ESTILO
st.set_page_config(page_title="Top Ofertas | Checkout Seguro", page_icon="🦊", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    html, body, [class*="st-"] { font-family: 'Inter', sans-serif; color: #1A1A1A !important; }
    .stApp { background-color: #FFFFFF; }

    /* Estilo do Carrinho no Header */
    .cart-badge {
        background-color: #FF4B4B; color: white; border-radius: 50%;
        padding: 2px 8px; font-size: 12px; position: relative; top: -10px; left: -5px;
    }

    .header-top {
        background: linear-gradient(90deg, #FF8C00, #FFA500);
        padding: 20px 10%; display: flex; align-items: center; justify-content: space-between;
        margin: -6rem -5rem 20px -5rem; color: white !important;
    }

    /* Card de Produto */
    .product-card {
        background: #FFFFFF; border-radius: 15px; padding: 20px;
        text-align: center; border: 1px solid #E0E0E0; margin-bottom: 20px;
    }

    /* Checkout Estilizado */
    .checkout-box {
        background: #F9F9F9; padding: 30px; border-radius: 15px;
        border: 1px solid #DDD; margin-top: 20px;
    }
    
    .stButton > button {
        background: #FF8C00 !important; color: white !important;
        border-radius: 10px !important; font-weight: 900 !important;
        width: 100%; height: 50px; border: none;
    }
    </style>
""", unsafe_allow_html=True)

# 2. INICIALIZAÇÃO DO CARRINHO (MEMÓRIA DO SITE)
if 'carrinho' not in st.session_state:
    st.session_state.carrinho = []
if 'pagina' not in st.session_state:
    st.session_state.pagina = "home"

# 3. BANCO DE DADOS DE PRODUTOS
produtos = {
    "cinta": {"nome": "Cinta Modeladora Yoga Premium", "preco": 97.90, "img": "https://logzz-s3.s3.us-east-2.amazonaws.com/uploads/files/products/20240714-131356prok2m05.jpg"},
    "depilador": {"nome": "Depilador SkinLiss Pro Max", "preco": 84.90, "img": "https://a-static.mlcdn.com.br/470x352/depilador-yes-finishing-touch-sem-fio-ativacao-sensor-de-luz-rosto-e-corpo-depiladorlaser/connectcellcomercio/depiladorroxo16/958b6b6bada9045715419c0988f0a3b6.jpeg"},
    "massagem": {"nome": "Massageador Cervical Inteligente", "preco": 137.90, "img": "https://m.media-amazon.com/images/I/61K9UqL8T9L._AC_SL1500_.jpg"}
}

# 4. HEADER DINÂMICO COM CONTADOR DE ITENS
col_logo, col_cart = st.columns([4, 1])
with col_logo:
    st.markdown(f'<div class="header-top"><h1>🦊 TOP OFERTAS</h1></div>', unsafe_allow_html=True)
with col_cart:
    qtd_itens = len(st.session_state.carrinho)
    if st.button(f"🛒 Carrinho ({qtd_itens})"):
        st.session_state.pagina = "checkout"
        st.rerun()

# --- PÁGINA DE CHECKOUT (CARRINHO) ---
if st.session_state.pagina == "checkout":
    st.title("🛒 Seu Carrinho de Compras")
    
    if not st.session_state.carrinho:
        st.warning("Seu carrinho está vazio!")
        if st.button("VOLTAR PARA AS COMPRAS"):
            st.session_state.pagina = "home"
            st.rerun()
    else:
        total = 0
        for i, item in enumerate(st.session_state.carrinho):
            with st.container():
                c1, c2, c3 = st.columns([1, 2, 1])
                c1.image(item['img'], width=80)
                c2.markdown(f"**{item['nome']}**")
                c2.write(f"R$ {item['preco']:.2f}")
                if c3.button("Remover", key=f"rem_{i}"):
                    st.session_state.carrinho.pop(i)
                    st.rerun()
                total += item['preco']
        
        st.markdown(f"""
            <div class="checkout-box">
                <h3>Resumo do Pedido</h3>
                <p>Subtotal: R$ {total:.2f}</p>
                <p style="color: green; font-weight: bold;">Frete: GRÁTIS</p>
                <hr>
                <h2 style="color: #FF8C00;">Total: R$ {total:.2f}</h2>
            </div>
        """, unsafe_allow_html=True)
        
        if st.button("FINALIZAR PEDIDO (PAGAR NA ENTREGA)"):
            st.success("✅ Pedido enviado com sucesso! Aguarde o contato no WhatsApp.")
            st.session_state.carrinho = [] # Limpa o carrinho

        if st.button("CONTINUAR COMPRANDO"):
            st.session_state.pagina = "home"
            st.rerun()

# --- PÁGINA HOME (VITRINE) ---
else:
    st.markdown("### 🔥 Ofertas do Dia")
    cols = st.columns(3)
    
    for i, (id_p, p) in enumerate(produtos.items()):
        with cols[i]:
            st.markdown(f"""
                <div class="product-card">
                    <img src="{p['img']}" style="width:100%; border-radius:10px;">
                    <p style="font-weight:bold; margin-top:10px;">{p['nome']}</p>
                    <p style="color:#FF8C00; font-size:20px; font-weight:900;">R$ {p['preco']:.2f}</p>
                </div>
            """, unsafe_allow_html=True)
            if st.button(f"ADICIONAR AO CARRINHO", key=id_p):
                st.session_state.carrinho.append(p)
                st.toast(f"{p['nome']} adicionado!")
                st.rerun()

    # FAQ VISÍVEL ABAIXO
    st.write("---")
    st.markdown("### 🙋‍♂️ Dúvidas?")
    with st.expander("O site é seguro?"):
        st.write("Sim, usamos criptografia de ponta e você pode pagar na entrega.")