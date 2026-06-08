import streamlit as st

st.set_page_config(page_title="Calculadora de Média - São Luís", page_icon="📊")

st.title("📊 Calculadora de Média - Colégio São Luís")
st.markdown("---")

# Inicializa as listas no estado da sessão para guardar a quantidade de notas
if 'qtd_av1' not in st.session_state:
    st.session_state.qtd_av1 = 2
if 'qtd_av2' not in st.session_state:
    st.session_state.qtd_av2 = 1

# --- SEÇÃO AV1 ---
st.subheader("Notas de AV1")
col1, col2 = st.columns(2)
with col1:
    if st.button("➕ Adicionar AV1"):
        st.session_state.qtd_av1 += 1
        st.rerun()
with col2:
    if st.button("➖ Remover AV1") and st.session_state.qtd_av1 > 1:
        st.session_state.qtd_av1 -= 1
        st.rerun()

notas_av1 = []
for i in range(st.session_state.qtd_av1):
    nota = st.number_input(f"Nota da AV1.{i+1}", min_value=0.0, max_value=10.0, step=0.1, key=f"av1_{i}")
    notas_av1.append(nota)

st.markdown("---")

# --- SEÇÃO AV2 ---
st.subheader("Notas de AV2")
col3, col4 = st.columns(2)
with col3:
    if st.button("➕ Adicionar AV2"):
        st.session_state.qtd_av2 += 1
        st.rerun()
with col4:
    if st.button("➖ Remover AV2") and st.session_state.qtd_av2 > 1:
        st.session_state.qtd_av2 -= 1
        st.rerun()

notas_av2 = []
for i in range(st.session_state.qtd_av2):
    nota = st.number_input(f"Nota da AV2.{i+1}", min_value=0.0, max_value=10.0, step=0.1, key=f"av2_{i}")
    notas_av2.append(nota)

st.markdown("---")

# --- SEÇÃO AV3 ---
st.subheader("Nota de AV3")
nota_av3 = st.number_input("Nota da AV3", min_value=0.0, max_value=10.0, step=0.1)

st.markdown("---")

# --- BOTÃO DE CÁLCULO ---
if st.button("🧮 Calcular Média Final", use_container_width=True):
    # Cálculo seguro das médias das listas (sem o operador que causou erro)
    if len(notas_av1) > 0:
        media_av1 = sum(notas_av1) / len(notas_av1)
    else:
        media_av1 = 0
        
    if len(notas_av2) > 0:
        media_av2 = sum(notas_av2) / len(notas_av2)
    else:
        media_av2 = 0
    
    # Fórmula do papel: ((4 * Média AV1) + (4 * AV3) + (2 * Média AV2)) / 10
    media_final = ((4 * media_av1) + (4 * nota_av3) + (2 * media_av2)) / 10
    
    # Exibir resultados bem destacados
    st.success(f"**Média Calculada da AV1:** {media_av1:.2f}")
    st.success(f"**Média Calculada da AV2:** {media_av2:.2f}")
    st.info(f"### 🎯 Média Final: {media_final:.2f}")
