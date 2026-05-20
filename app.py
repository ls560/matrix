import streamlit as st

# 1. НАЛАШТУВАННЯ СТОРІНКИ
st.set_page_config(page_title="Нумерологічний Калькулятор", page_icon="🔮", layout="centered")

st.markdown("""
    <style>
    .block-container { max-width: 450px !important; padding: 1rem !important; }
    .field-label { text-align: center; font-size: 15px; font-weight: 600; margin: 10px 0 5px 0; color: #4A3B32; }
    .result-container {
        font-family: sans-serif;
        background-color: #ffffff;
        padding: 20px;
        border-radius: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        margin-top: 20px;
        text-align: center;
    }
    .watermark {
        margin-top: 15px;
        font-size: 10px;
        color: #aaa;
        font-style: italic;
    }
    .grid { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; margin-top: 15px; }
    .item { padding: 10px; background: #f9f9f9; border-radius: 10px; }
    </style>
""", unsafe_allow_html=True)

# 2. ФОРМА ВВЕДЕННЯ
st.markdown('<div class="field-label">Ваше Ім'я</div>', unsafe_allow_html=True)
user_name = st.text_input("Ім'я", label_visibility="collapsed")

st.markdown('<div class="field-label">Дата народження</div>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1: day = st.selectbox("День", list(range(1, 32)), index=16)
with col2: month = st.selectbox("Місяць", list(range(1, 13)), index=11)
with col3: year = st.selectbox("Рік", list(range(1940, 2030)), index=49)

# 3. ЛОГІКА РОЗРАХУНКУ
if st.button("Розрахувати", use_container_width=True):
    all_content = f"{day}{month}{year}"
    digits = [int(d) for d in all_content]
    
    num1 = sum(digits)
    num2 = sum([int(d) for d in str(num1)])
    
    # Матриця з емодзі
    matrix = {
        'Характер 1️⃣': all_content.count('1'),
        'Енергія 2️⃣': all_content.count('2'),
        'Цікавість 3️⃣': all_content.count('3'),
        'Здоров'я 4️⃣': all_content.count('4'),
        'Логіка 5️⃣': all_content.count('5'),
        'Праця 6️⃣': all_content.count('6'),
        'Удача 7️⃣': all_content.count('7'),
        'Обов'язок 8️⃣': all_content.count('8'),
        'Пам'ять 9️⃣': all_content.count('9')
    }
    
    st.markdown(f"""
    <div class="result-container">
        <h3>✨ Результати для {user_name if user_name else 'Вас'} ✨</h3>
        <p>Число долі: <b>{num2}</b></p>
        <div class="grid">
    """, unsafe_allow_html=True)
    
    for key, value in matrix.items():
        st.markdown(f"<div class='item'><b>{key}</b><br>{value if value > 0 else '—'}</div>", unsafe_allow_html=True)
        
    st.markdown("""
        </div>
        <div class="watermark">by light of my shadow</div>
    </div>
    """, unsafe_allow_html=True)
