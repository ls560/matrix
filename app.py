import streamlit as st

# 1. НАЛАШТУВАННЯ
st.set_page_config(page_title="Нумерологія", page_icon="🔮", layout="centered")

# CSS для стилізації (використовуємо подвійні лапки для безпеки)
st.markdown("""
    <style>
    .block-container { max-width: 450px !important; padding: 1rem !important; }
    .intro-text { font-size: 16px; color: #333; margin-bottom: 20px; line-height: 1.4; }
    .field-label { font-size: 14px; font-weight: 600; margin: 10px 0 5px 0; }
    .matrix-card { background: #fdfbf7; padding: 15px; border-radius: 15px; border: 1px solid #ddd; margin-top: 20px; }
    .grid { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 8px; margin-top: 10px; }
    .cell { padding: 8px; background: white; border-radius: 8px; text-align: center; border: 1px solid #eee; }
    .cta-text { margin-top: 20px; padding: 15px; background: #FFF0F3; border-radius: 10px; font-size: 13px; line-height: 1.4; }
    .watermark { text-align: center; font-size: 9px; color: #aaa; margin-top: 10px; font-style: italic; }
    .matrix-header-watermark { font-size: 9px; opacity: 0.7; font-style: italic; display: block; margin-top: -2px; }
    </style>
""", unsafe_allow_html=True)

# 2. ІНТЕРФЕЙС
st.markdown("<div class='intro-text'>Твоя дата народження — це більше ніж просто цифри. Введи свою дату та подивися, що приховує твоя матриця.</div>", unsafe_allow_html=True)

user_name = st.text_input("Ваше Ім'я")

st.markdown("<div class='field-label'>Дата народження</div>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
day = col1.selectbox("День", list(range(1, 32)), index=29)
month = col2.selectbox("Місяць", list(range(1, 13)), index=3)
year = col3.selectbox("Рік", list(range(1940, 2030)), index=46)

selected_color = st.selectbox("Оберіть улюблений колір:", ["Червоний", "Помаранчевий", "Жовтий", "Зелений", "Блакитний", "Синій", "Фіолетовий", "Рожевий", "Беж"])

# 3. РОЗРАХУНОК
if st.button("Розрахувати", use_container_width=True):
    all_content = f"{day}{month}{year}"
    digits = [int(d) for d in all_content]
    num_sum = sum(digits)
    num2 = sum([int(d) for d in str(num_sum)])
    
    # Словник без емодзі в назвах ключів для стабільності
    matrix = {
        'Характер': all_content.count('1'),
        'Енергія': all_content.count('2'),
        'Цікавість': all_content.count('3'),
        'Здоровя': all_content.count('4'),
        'Логіка': all_content.count('5'),
        'Праця': all_content.count('6'),
        'Удача': all_content.count('7'),
        'Обовязок': all_content.count('8'),
        'Памят': all_content.count('9')
    }

    # Вивід результату
    st.markdown(f"""
    <div class="matrix-card">
        <h3>✨ {user_name if user_name else 'Матриця'} ✨</h3>
        <p>Колір: <b>{selected_color}</b> | Число долі: <b>{num2}</b></p>
        <div style="font-size:10px; margin-bottom:10px;">by light of my shadow</div>
        <div class="grid">
    """, unsafe_allow_html=True)
    
    for k, v in matrix.items():
        st.markdown(f"<div class='cell'><b>{k}</b><br>{v if v > 0 else '—'}</div>", unsafe_allow_html=True)
    
    st.markdown("""
        </div>
    </div>
    <div class='cta-text'>
        Бачиш ці цифри? Це лише поверхня айсберга. Зроби скріншот цієї карти та надішли мені в Direct. Я подивлюся твою матрицю глибше і скажу, де твоя справжня сила, як у тебе працюють гроші, які в тебе приховані таланти і що саме зараз блокує твій потенціал.
    </div>
    <div class='watermark'>by light of my shadow</div>
    """, unsafe_allow_html=True)
