import streamlit as st

# Налаштування сторінки
st.set_page_config(page_title="Нумерологія", page_icon="🔮", layout="centered")

# CSS для стилів (використовуємо потрійні лапки для безпеки)
st.markdown("""
    <style>
    .block-container { max-width: 420px !important; }
    .field-label { text-align: center; font-size: 15px; font-weight: 600; margin: 10px 0 5px 0; }
    .result-container {
        margin-top: 20px;
        padding: 20px;
        background-color: #f0f2f6;
        border-radius: 15px;
        text-align: center;
    }
    .watermark { font-size: 10px; color: #888; margin-top: 10px; font-style: italic; }
    </style>
""", unsafe_allow_html=True)

# Форма введення
st.markdown("<div class='field-label'>Ваше Ім'я</div>", unsafe_allow_html=True)
user_name = st.text_input("Ім'я", label_visibility="collapsed")

st.markdown("<div class='field-label'>Дата народження</div>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1: day = st.selectbox("День", list(range(1, 32)), index=16)
with col2: month = st.selectbox("Місяць", list(range(1, 13)), index=11)
with col3: year = st.selectbox("Рік", list(range(1940, 2030)), index=49)

# Логіка
if st.button("Розрахувати", use_container_width=True):
    all_digits = [int(d) for d in f"{day}{month}{year}"]
    s1 = sum(all_digits)
    s2 = sum([int(d) for d in str(s1)])
    
    st.markdown(f"""
        <div class='result-container'>
            <h3>✨ {user_name if user_name else 'Результат'} ✨</h3>
            <p>Ваші числа: <b>{s1}</b> та <b>{s2}</b></p>
            <div class='watermark'>by light of my shadow</div>
        </div>
    """, unsafe_allow_html=True)
