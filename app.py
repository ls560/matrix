import streamlit as st

# Налаштування сторінки, щоб додаток гарно виглядав на мобільному
st.set_page_config(page_title="Нумерологічний Калькулятор", page_icon="🔮", layout="centered")

# Приховуємо стандартні елементи Streamlit для чистого дизайну
hide_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_style, unsafe_allow_html=True)

# 1. ВВЕДЕННЯ ДАНИХ (Ім'я, Дата, Колір)
st.markdown("<h2 style='text-align: center; color: #4A3B32;'>Ваше Ім'я</h2>", unsafe_allow_html=True)
user_name = st.text_input("Введіть ім'я", value="", label_visibility="collapsed")

st.markdown("<h2 style='text-align: center; color: #4A3B32;'>Ваша дата народження</h2>", unsafe_allow_html=True)

# Зручний вибір дати у рядок
col_d, col_m, col_y = st.columns(3)
with col_d:
    day = st.selectbox("День", list(range(1, 32)), index=16)  # 17 за замовчуванням
with col_m:
    months = ["Січень", "Лютий", "Березень", "Квітень", "Травень", "Червень", "Липень", "Серпень", "Вересень", "Жовтень", "Листопад", "Грудень"]
    month = st.selectbox("Місяць", months, index=11)  # Грудень за замовчуванням
with col_y:
    year = st.selectbox("Рік", list(range(1940, 2027)), index=49)  # 1989 за замовчуванням

# Вибір улюбленого кольору (міняє фоновий акцент матриці)
st.markdown("<h3 style='text-align: center; color: #4A3B32; font-size: 16px;'>Улюблений колір теми</h3>", unsafe_allow_html=True)
color_theme = st.selectbox("Колір", ["Класичний беж", "Ніжна троянда", "М'ятний", "Глибокий синій"], label_visibility="collapsed")

# Визначаємо палітру залежно від вибору кольору
if color_theme == "Класичний беж":
    bg_main, bg_header, text_dark = "#D1BFA7", "#A89480", "#2E2520"
elif color_theme == "Ніжна троянда":
    bg_main, bg_header, text_dark = "#E8C5C8", "#C99A9E", "#382022"
elif color_theme == "М'ятний":
    bg_main, bg_header, text_dark = "#C5E0DC", "#99BDB6", "#1C2E2B"
else:
    bg_main, bg_header, text_dark = "#C2D3E8", "#90AECF", "#182636"

st.markdown("<br>", unsafe_allow_html=True)

# Кнопка розрахунку
if st.button("Розрахувати", use_container_width=True):
    
    # ТУТ ТВОЯ ЛОГІКА РОЗРАХУНКУ (зараз підставимо цифри зі скріншоту як приклад)
    # Коли додаси свій алгоритм, просто заміни ці змінні на автоматичні розрахунки:
    date_str = f"{day:02d}.{months.index(month)+1:02d}.{year}"
    chyslo_doli = "11"
    temperament = "3"
    
    character = "11111"
    health = "—"
    luck = "7"
    goal = "6"
    
    energy = "2"
    logic = "—"
    duty = "88"
    family = "3"
    
    interest = "33"
    work = "6"
    memory = "999"
    habits = "6"
    
    self_esteem = "8"
    household = "1"
    
    additional_numbers = "38, 11, 36, 9"
    code_line = "11111/ 2/ 33/ —/ —/ 6/ 7/ 88/ 999/ ЧД 11"

    # Вітання з ім'ям, якщо воно введене
    if user_name:
        st.markdown(f"<h3 style='text-align: center; color: {text_dark};'>✨ Матриця для імені: {user_name} ✨</h3>", unsafe_allow_html=True)

    # 2. СТИЛІЗОВАНА МОБІЛЬНА ТАБЛИЦЯ (HTML)
    matrix_html = f"""
    <div style="font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; max-width: 400px; margin: 0 auto; background-color: {bg_main}; padding: 12px; border-radius: 20px; box-shadow: 0px 4px 15px rgba(0,0,0,0.05); color: {text_dark};">
        
        <table style="width: 100%; border-collapse: collapse; margin-bottom: 8px; text-align: center; background-color: {bg_header}; border-radius: 14px 14px 0 0; overflow: hidden;">
            <tr>
                <td style="padding: 15px; font-size: 22px; font-weight: bold; width: 40%;">{date_str}</td>
                <td style="padding: 10px; border-left: 1px solid rgba(0,0,0,0.1); width: 30%;">
                    <span style="font-size: 11px; opacity: 0.8; display:block;">Число Долі</span>
                    <span style="font-size: 22px; font-weight: bold;">{chyslo_doli}</span>
                </td>
                <td style="padding: 10px; border-left: 1px solid rgba(0,0,0,0.1); width: 30%;"><span style="font-size: 11px; opacity: 0.8; display:block;">Темперамент</span>
                    <span style="font-size: 22px; font-weight: bold;">{temperament}</span>
                </td>
            </tr>
        </table>

        <table style="width: 100%; border-collapse: collapse; text-align: center; background-color: #ffffff; border-radius: 0 0 14px 14px; overflow: hidden;">
            <tr style="border-bottom: 1px solid #E0E0E0;">
                <td style="padding: 10px; width: 25%; border-right: 1px solid #E0E0E0;">
                    <span style="font-size: 11px; color: #888888; display:block;">Характер</span>
                    <span style="font-size: 18px; font-weight: bold;">{character}</span>
                </td>
                <td style="padding: 10px; width: 25%; border-right: 1px solid #E0E0E0;">
                    <span style="font-size: 11px; color: #888888; display:block;">Здоров'я</span>
                    <span style="font-size: 18px; font-weight: bold;">{health}</span>
                </td>
                <td style="padding: 10px; width: 25%; border-right: 1px solid #E0E0E0;">
                    <span style="font-size: 11px; color: #888888; display:block;">Удача</span>
                    <span style="font-size: 18px; font-weight: bold;">{luck}</span>
                </td>
                <td style="padding: 10px; width: 25%; background-color: {bg_main}40;">
                    <span style="font-size: 11px; color: #888888; display:block;">Ціль</span>
                    <span style="font-size: 18px; font-weight: bold;">{goal}</span>
                </td>
            </tr>
            <tr style="border-bottom: 1px solid #E0E0E0;">
                <td style="padding: 10px; border-right: 1px solid #E0E0E0;">
                    <span style="font-size: 11px; color: #888888; display:block;">Енергія</span>
                    <span style="font-size: 18px; font-weight: bold;">{energy}</span>
                </td>
                <td style="padding: 10px; border-right: 1px solid #E0E0E0;">
                    <span style="font-size: 11px; color: #888888; display:block;">Логіка</span>
                    <span style="font-size: 18px; font-weight: bold;">{logic}</span>
                </td>
                <td style="padding: 10px; border-right: 1px solid #E0E0E0;">
                    <span style="font-size: 11px; color: #888888; display:block;">Обов'язок</span>
                    <span style="font-size: 18px; font-weight: bold;">{duty}</span>
                </td>
                <td style="padding: 10px; background-color: {bg_main}40;">
                    <span style="font-size: 11px; color: #888888; display:block;">Сім'я</span>
                    <span style="font-size: 18px; font-weight: bold;">{family}</span>
                </td>
            </tr>
            <tr style="border-bottom: 1px solid #E0E0E0;">
                <td style="padding: 10px; border-right: 1px solid #E0E0E0;">
                    <span style="font-size: 11px; color: #888888; display:block;">Цікавість</span>
                    <span style="font-size: 18px; font-weight: bold;">{interest}</span>
                </td>
                <td style="padding: 10px; border-right: 1px solid #E0E0E0;">
                    <span style="font-size: 11px; color: #888888; display:block;">Праця</span>
                    <span style="font-size: 18px; font-weight: bold;">{work}</span>
                </td>
                <td style="padding: 10px; border-right: 1px solid #E0E0E0;">
                    <span style="font-size: 11px; color: #888888; display:block;">Пам'ять</span>
                    <span style="font-size: 18px; font-weight: bold;">{memory}</span>
                </td>
                <td style="padding: 10px; background-color: {bg_main}40;">
                    <span style="font-size: 11px; color: #888888; display:block;">Звички</span>
                    <span style="font-size: 18px; font-weight: bold;">{habits}</span>
                </td>
            </tr>
            <tr><td style="padding: 10px; border-right: 1px solid #E0E0E0; background-color: {bg_main}40;">
                    <span style="font-size: 11px; color: #888888; display:block;">Самооцінка</span>
                    <span style="font-size: 18px; font-weight: bold;">{self_esteem}</span>
                </td>
                <td style="padding: 10px; border-right: 1px solid #E0E0E0; background-color: {bg_main}40;">
                    <span style="font-size: 11px; color: #888888; display:block;">Побут</span>
                    <span style="font-size: 18px; font-weight: bold;">{household}</span>
                </td>
                <td colspan="2" style="padding: 6px; font-size: 11px; text-align: center; color: #555555; background-color: #FAF6F0;">
                    <b style="color:#888;">Додаткові Числа:</b><br>{additional_numbers}<br>
                    <span style="font-size: 10px; letter-spacing: 0.5px; font-weight: bold; color: {text_dark};">{code_line}</span>
                </td>
            </tr>
        </table>
    </div>
    """
    
    st.markdown(matrix_html, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Кнопка копіювання (функція Streamlit)
    st.copy_to_clipboard(f"Результат розрахунку для {user_name if user_name else 'Гість'} ({date_str}): {code_line}")
    st.info("📋 Результат автоматично скопійовано в буфер обміну!")
