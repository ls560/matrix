import streamlit as st

# --- ЛОГІКА РОЗРАХУНКУ ---
def get_root(num):
    while num > 9 and num not in [11, 22, 33]:
        num = sum(int(d) for d in str(num))
    return num

def calculate_pythagoras(day, month, year):
    s_date = f"{day:02d}{month:02d}{year}"
    f_n = sum(int(d) for d in s_date)
    s_n = get_root(f_n)
    day_str = str(day).lstrip('0')
    first_digit = int(day_str[0])
    t_n = abs(f_n - (2 * first_digit))
    fo_n = sum(int(d) for d in str(t_n))
    all_digits = s_date + str(f_n) + str(s_n) + str(t_n) + str(fo_n)
    counts = {str(i): all_digits.count(str(i)) for i in range(1, 10)}
    
    return {
        "counts": counts,
        "extra": [f_n, s_n, t_n, fo_n],
        "destiny": s_n,
        "lines": {
            "🎯 Цілі": counts['1'] + counts['4'] + counts['7'],
            "🏠 Сім'я": counts['2'] + counts['5'] + counts['8'],
            "⚓ Звички": counts['3'] + counts['6'] + counts['9'],
            "🍎 Темперамент": counts['3'] + counts['5'] + counts['7'],
            "🧘 Духовність": counts['1'] + counts['5'] + counts['9'],
            "💰 Побут": counts['4'] + counts['5'] + counts['6'],
            "💎 Стабільність": counts['3'] + counts['6'] + counts['9']
        }
    }

# --- ДИЗАЙН ТА НАЛАШТУВАННЯ ---
st.set_page_config(page_title="Matrix Premium 2026", layout="wide")

st.markdown("""
    <style>
    [data-testid="stMetricValue"] { font-size: 26px !important; color: #1E1E1E !important; font-weight: bold !important; }
    [data-testid="stMetricLabel"] { font-size: 14px !important; font-weight: 600 !important; color: #555 !important; }
    
    .stMetric { 
        background-color: #ffffff; 
        padding: 15px !important; 
        border-radius: 12px; 
        box-shadow: 0 4px 10px rgba(0,0,0,0.06); 
        border-left: 4px solid #d4af37;
        margin-bottom: 10px;
    }
    
    /* Нові стилі для компактних квадратних карток векторів */
    .vector-square-box {
        background-color: #ffffff;
        padding: 12px;
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.06);
        border-left: 4px solid #2c3e50;
        margin-bottom: 12px;
        min-height: 85px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    .vector-square-title {
        font-size: 13px;
        font-weight: 600;
        color: #555;
    }
    .vector-square-value {
        font-size: 22px;
        font-weight: bold;
        color: #1E1E1E;
        margin-top: 5px;
    }
    
    .cta-box {
        background: linear-gradient(135deg, #fdfbfb 0%, #ebedee 100%);
        padding: 30px;
        border-radius: 20px;
        border: 2px solid #d4af37;
        margin-top: 25px;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; margin-bottom: 5px;'>🔮 У твоїх цифрах заховано більше, ніж ти думаєш</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px; color: #555;'>Подивись, що про тебе насправді говорить твоя дата народження.</p>", unsafe_allow_html=True)

# Введення даних
c1, c2, c3 = st.columns(3)
with c1: d = st.number_input("📅 День", 1, 31, 1)
with c2: m = st.number_input("🌕 Місяць", 1, 12, 9)
with c3: y = st.number_input("⏳ Рік", 1900, 2026, 1980)

if st.button("✨ РОЗКРИТИ СЕКРЕТИ МОЄЇ ДАТИ", use_container_width=True):
    res = calculate_pythagoras(d, m, y)
    counts = res["counts"]
    def v(n): return str(n) * counts[str(n)] if counts[str(n)] > 0 else "—"

    st.write("---")
    
    # Головний контейнер: зліва матриця 3х3, справа — вектори
    col_matrix, col_vectors = st.columns([2.0, 1.5], gap="large")

    with col_matrix:
        st.markdown("<h3 style='color: #2c3e50; margin-bottom: 15px;'>🛡️ Твій Цифровий Профіль</h3>", unsafe_allow_html=True)
        m1, m2, m3 = st.columns(3)
        with m1:
            st.metric("👑 Характер", v(1))
            st.metric("⚡ Енергія", v(2))
            st.metric("🎨 Цікавість", v(3))
        with m2:
            st.metric("🩺 Здоров'я", v(4))
            st.metric("🧠 Логіка", v(5))
            st.metric("🛠️ Праця", v(6))
        with m3:
            st.metric("🍀 Удача", v(7))
            st.metric("⚖️ Обов'язок", v(8))
            st.metric("📚 Пам'ять", v(9))  # Додано 9-ку на своє місце

    with col_vectors:
        st.markdown("<h3 style='color: #2c3e50; margin-bottom: 15px;'>📈 Вектори життя</h3>", unsafe_allow_html=True)
        
        # Створюємо сітку з 2 стовпчиків всередині правої панелі, щоб картки були маленькими квадратами
        v_col1, v_col2 = st.columns(2)
        lines = res["lines"]
        
        # Перетворюємо словник у список для зручного розподілу по стовпчиках
        items = list(lines.items())
        
        with v_col1:
            for title, value in items[:3]:  # Перші 3 вектори
                st.markdown(f"""
                    <div class="vector-square-box">
                        <span class="vector-square-title">{title}</span>
                        <span class="vector-square-value">{value}</span>
                    </div>
                """, unsafe_allow_html=True)
                
        with v_col2:
            for title, value in items[3:]:  # Наступні 4 вектори
                st.markdown(f"""
                    <div class="vector-square-box">
                        <span class="vector-square-title">{title}</span>
                        <span class="vector-square-value">{value}</span>
                    </div>
                """, unsafe_allow_html=True)
        
        # Окремий яскравий блок для Числа Долі внизу під квадратами
        st.markdown(f"""
            <div class="vector-square-box" style="border-left: 4px solid #d4af37; background-color: #fffdf3; min-height: auto; flex-direction: row; justify-content: space-between; align-items: center;">
                <span class="vector-square-title" style="color: #b89214; font-size: 14px;">💎 Число Долі</span>
                <span style="font-size: 22px; font-weight: bold; color: white; background: #d4af37; padding: 2px 12px; border-radius: 8px;">{res["destiny"]}</span>
            </div>
        """, unsafe_allow_html=True)

    # ФІНАЛЬНИЙ ТЕКСТ
    st.markdown(f"""
        <div class="cta-box">
            <h2 style="color: #2c3e50; text-align: center; margin-top: 0; font-size: 22px;">📸 Бачиш ці цифри? Це лише поверхня айсберга!</h2>
            <p style="font-size: 16px; line-height: 1.6; color: #34495e; text-align: center;">
                За ними — значно глибший код твоєї особистості: як ти мислиш, де втрачаєш енергію та через що відкривається твій потенціал.<br><br>
                <b>Зроби скріншот цього екрану і надішли мені в Direct.</b> Я подивлюся твою матрицю глибше і скажу:<br>
                🎯 <b>Де твоя справжня сила?</b> | 💎 <b>Які в тебе природні таланти?</b> | 🚫 <b>Що блокує потенціал?</b><br>
                💸 <b>Звідки приходять гроші?</b> | 👔 <b>Які професії тобі підходять?</b> | ✨ <b>В чому твоя унікальність?</b>
            </p>
            <p style="font-size: 18px; font-weight: bold; color: #d4af37; text-align: center; margin-top: 15px; letter-spacing: 0.5px;">🚀 Чекаю твій скріншот для розбору!</p>
        </div>
    """, unsafe_allow_html=True)

    st.caption(f"Технічні дані: {', '.join(map(str, res['extra']))}")
