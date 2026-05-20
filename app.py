import streamlit as st

# 1. НАЛАШТУВАННЯ СТОРІНКИ ДЛЯ МОБІЛЬНИХ ПРИСТРОЇВ
st.set_page_config(
    page_title="Нумерологічний Калькулятор", 
    page_icon="🔮", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Стилізація інтерфейсу через CSS
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
        max-width: 450px !important;
    }
    div[data-testid="stForm"] {
        border: none;
        padding: 0;
    }
    .stApp {
        background-color: #FAF6F0;
    }
    </style>
""", unsafe_allow_html=True)

# 2. ПОЛЯ ВВЕДЕННЯ ДАНИХ
st.markdown("<h3 style='text-align: center; color: #4A3B32; font-size: 20px; margin-bottom: 5px;'>Ваше Ім'я</h3>", unsafe_allow_html=True)
user_name = st.text_input("Ім'я", value="", placeholder="Введіть ваше ім'я...", label_visibility="collapsed")

st.markdown("<h3 style='text-align: center; color: #4A3B32; font-size: 20px; margin-top: 15px; margin-bottom: 5px;'>Ваша дата народження</h3>", unsafe_allow_html=True)

# 3 випадаючі списки для дати в один рядок
col_d, col_m, col_y = st.columns(3)
with col_d:
    day = st.selectbox("День", list(range(1, 32)), index=16)
with col_m:
    months = ["Січень", "Лютий", "Березень", "Квітень", "Травень", "Червень", "Липень", "Серпень", "Вересень", "Жовтень", "Листопад", "Грудень"]
    month_name = st.selectbox("Місяць", months, index=11)
with col_y:
    year = st.selectbox("Рік", list(range(1940, 2030)), index=49)

# 3. ВИБІР УЛЮБЛЕНОГО КОЛОРУ (ТЕМИ) СПИСКОМ
st.markdown("<h3 style='text-align: center; color: #4A3B32; font-size: 18px; margin-top: 15px; margin-bottom: 5px;'>Оберіть улюблений колір (тему):</h3>", unsafe_allow_html=True)
theme_choice = st.selectbox(
    "Оберіть колір", 
    ["Класичний беж", "Ніжна троянда", "Свіжа м'ята", "Шляхетний сірий"], 
    label_visibility="collapsed"
)

# Визначаємо кольори та текстову мітку для картки залежно від вибору
if theme_choice == "Класичний беж":
    main_bg, header_bg, text_color, accent_bg = "#C4B29E", "#A3907C", "#2E2520", "#FAF6F0"
    color_label = "Беж"
elif theme_choice == "Ніжна троянда":
    main_bg, header_bg, text_color, accent_bg = "#E5BFC3", "#C49297", "#3B2224", "#FDF8F9"
    color_label = "Рожевий"
elif theme_choice == "Свіжа м'ята":
    main_bg, header_bg, text_color, accent_bg = "#BBDCD5", "#91BAB2", "#1D332F", "#F5FAF9"
    color_label = "М'ята"
else:
    main_bg, header_bg, text_color, accent_bg = "#CCD4DB", "#9FAAB5", "#242A30", "#F7FAFC"
    color_label = "Сірий"

st.markdown("<br>", unsafe_allow_html=True)

# КНОПКА "РОЗРАХУВАТИ"
if st.button("Розрахувати", use_container_width=True):
    month_num = months.index(month_name) + 1
    date_str = f"{day:02d}.{month_num:02d}.{year}"
    
    # -------------------------------------------------------------------------
    # ЛОГІКА РОЗРАХУНКУ ПІФАГОРОВОЇ МАТРИЦІ
    # -------------------------------------------------------------------------
    digits = [int(d) for d in f"{day}{month_num}{year}"]
    num1 = sum(digits)
    num2 = sum([int(d) for d in str(num1)])
    
    day_str = f"{day:02d}"
    first_day_digit = int(day_str[0]) if int(day_str[0]) != 0 else int(day_str[1])
    num3 = num1 - (2 * first_day_digit)
    num4 = sum([int(d) for d in str(num3)])
    
    additional_numbers = f"{num1}, {num2}, {num3}, {num4}"
    all_content = f"{day}{month_num}{year}{num1}{num2}{num3}{num4}"
    
    # Підрахунок кількості цифр для клітинок
    character = str(1) * all_content.count('1') if all_content.count('1') > 0 else "—"
    energy = str(2) * all_content.count('2') if all_content.count('2') > 0 else "—"
    interest = str(3) * all_content.count('3') if all_content.count('3') > 0 else "—"
    health = str(4) * all_content.count('4') if all_content.count('4') > 0 else "—"
    logic = str(5) * all_content.count('5') if all_content.count('5') > 0 else "—"
    work = str(6) * all_content.count('6') if all_content.count('6') > 0 else "—"
    luck = str(7) * all_content.count('7') if all_content.count('7') > 0 else "—"
    duty = str(8) * all_content.count('8') if all_content.count('8') > 0 else "—"
    memory = str(9) * all_content.count('9') if all_content.count('9') > 0 else "—"
    
    # Розрахунок лінійних показників
    chyslo_doli = num2
    if chyslo_doli > 9 and chyslo_doli != 11:
        chyslo_doli = sum([int(d) for d in str(chyslo_doli)])
        
    temperament = str(all_content.count('1') + all_content.count('2') + all_content.count('3'))
    goal = str(all_content.count('1') + all_content.count('4') + all_content.count('7'))
    family = str(all_content.count('2') + all_content.count('5') + all_content.count('8'))
    habits = str(all_content.count('3') + all_content.count('6') + all_content.count('9'))
    
    self_esteem = str(all_content.count('1') + all_content.count('4') + all_content.count('7'))
    household = str(all_content.count('2') + all_content.count('5') + all_content.count('8'))
    
    code_line = f"{character}/ {energy}/ {interest}/ {health}/ {logic}/ {work}/ {luck}/ {duty}/ {memory}/ ЧД {chyslo_doli}"

    # 4. ВІДОБРАЖЕННЯ КАРТКИ В ОДИН СУЦІЛЬНИЙ РЯДОК ДЛЯ СТРИМЛІТ
    if user_name:
        st.markdown(f"<h3 style='text-align: center; color: {text_color}; font-weight: bold; margin-top: 10px;'>✨ {user_name} ✨</h3>", unsafe_allow_html=True)
        
    matrix_html = (
        f'<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; max-width: 100%; margin: 0 auto; background-color: {main_bg}; padding: 12px; border-radius: 24px; box-shadow: 0px 10px 25px rgba(0,0,0,0.08); color: {text_color};">'
        f'<table style="width: 100%; border-collapse: collapse; margin-bottom: 8px; text-align: center; background-color: {header_bg}; border-radius: 16px 16px 0 0; overflow: hidden; color: #ffffff;">'
        f'<tr><td style="padding: 16px 10px; font-size: 22px; font-weight: bold; width: 40%; border-right: 1px solid rgba(255,255,255,0.2);">{date_str}</td>'
        f'<td style="padding: 10px; border-right: 1px solid rgba(255,255,255,0.2); width: 30%;"><span style="font-size: 11px; opacity: 0.85; display:block; margin-bottom: 2px;">Колір / ЧД</span><span style="font-size: 20px; font-weight: bold;">{color_label} ({chyslo_doli})</span></td>'
        f'<td style="padding: 10px; width: 30%;"><span style="font-size: 11px; opacity: 0.85; display:block; margin-bottom: 2px;">Темперамент</span><span style="font-size: 22px; font-weight: bold;">{temperament}</span></td></tr>'
        f'</table>'
        f'<table style="width: 100%; border-collapse: collapse; text-align: center; background-color: #ffffff; border-radius: 0 0 16px 16px; overflow: hidden;">'
        f'<tr style="border-bottom: 1px solid #EAEAEA;">'
        f'<td style="padding: 12px 6px; width: 25%; border-right: 1px solid #EAEAEA;"><span style="font-size: 11px; color: #8A8A8F; display:block; margin-bottom: 4px;">Характер</span><span style="font-size: 18px; font-weight: bold; color: {text_color};">{character}</span></td>'
        f'<td style="padding: 12px 6px; width: 25%; border-right: 1px solid #EAEAEA;"><span style="font-size: 11px; color: #8A8A8F; display:block; margin-bottom: 4px;">Здоров'я</span><span style="font-size: 18px; font-weight: bold; color: {text_color};">{health}</span></td>'
        f'<td style="padding: 12px 6px; width: 25%; border-right: 1px solid #EAEAEA;"><span style="font-size: 11px; color: #8A8A8F; display:block; margin-bottom: 4px;">Удача</span><span style="font-size: 18px; font-weight: bold; color: {text_color};">{luck}</span></td>'
        f'<td style="padding: 12px 6px; width: 25%; background-color: {main_bg}25;"><span style="font-size: 11px; color: #8A8A8F; display:block; margin-bottom: 4px;">Ціль</span><span style="font-size: 18px; font-weight: bold; color: {text_color};">{goal}</span></td>'
        f'</tr>'
        f'<tr style="border-bottom: 1px solid #EAEAEA;">'
        f'<td style="padding: 12px 6px; border-right: 1px solid #EAEAEA;"><span style="font-size: 11px; color: #8A8A8F; display:block; margin-bottom: 4px;">Енергія</span><span style="font-size: 18px; font-weight: bold; color: {text_color};">{energy}</span></td>'
        f'<td style="padding: 12px 6px; border-right: 1px solid #EAEAEA;"><span style="font-size: 11px; color: #8A8A8F; display:block; margin-bottom: 4px;">Логіка</span><span style="font-size: 18px; font-weight: bold; color: {text_color};">{logic}</span></td>'
        f'<td style="padding: 12px 6px; border-right: 1px solid #EAEAEA;"><span style="font-size: 11px; color: #8A8A8F; display:block; margin-bottom: 4px;">Обов'язок</span><span style="font-size: 18px; font-weight: bold; color: {text_color};">{duty}</span></td>'
        f'<td style="padding: 12px 6px; background-color: {main_bg}25;"><span style="font-size: 11px; color: #8A8A8F; display:block; margin-bottom: 4px;">Сім'я</span><span style="font-size: 18px; font-weight: bold; color: {text_color};">{family}</span></td>'
        f'</tr>'
        f'<tr style="border-bottom: 1px solid #EAEAEA;">'
        f'<td style="padding: 12px 6px; border-right: 1px solid #EAEAEA;"><span style="font-size: 11px; color: #8A8A8F; display:block; margin-bottom: 4px;">Цікавість</span><span style="font-size: 18px; font-weight: bold; color: {text_color};">{interest}</span></td>'
        f'<td style="padding: 12px 6px; border-right: 1px solid #EAEAEA;"><span style="font-size: 11px; color: #8A8A8F; display:block; margin-bottom: 4px;">Праця</span><span style="font-size: 18px; font-weight: bold; color: {text_color};">{work}</span></td>'
        f'<td style="padding: 12px 6px; border-right: 1px solid #EAEAEA;"><span style="font-size: 11px; color: #8A8A8F; display:block; margin-bottom: 4px;">Пам'ять</span><span style="font-size: 18px; font-weight: bold; color: {text_color};">{memory}</span></td>'
        f'<td style="padding: 12px 6px; background-color: {main_bg}25;"><span style="font-size: 11px; color: #8A8A8F; display:block; margin-bottom: 4px;">Звички</span><span style="font-size: 18px; font-weight: bold; color: {text_color};">{habits}</span></td>'
        f'</tr>'
        f'<tr>'
        f'<td style="padding: 12px 6px; border-right: 1px solid #EAEAEA; background-color: {main_bg}25;"><span style="font-size: 11px; color: #8A8A8F; display:block; margin-bottom: 4px;">Самооцінка</span><span style="font-size: 18px; font-weight: bold; color: {text_color};">{self_esteem}</span></td>'
        f'<td style="padding: 12px 6px; border-right: 1px solid #EAEAEA; background-color: {main_bg}25;"><span style="font-size: 11px; color: #8A8A8F; display:block; margin-bottom: 4px;">Побут</span><span style="font-size: 18px; font-weight: bold; color: {text_color};">{household}</span></td>'
        f'<td colspan="2" style="padding: 8px 4px; font-size: 12px; text-align: center; background-color: {accent_bg};"><span style="color: #8A8A8F; font-size: 11px; display: block; margin-bottom: 2px;">Додаткові Числа</span><b style="color: {text_color}; font-size: 13px;">{additional_numbers}</b><div style="font-size: 10px; margin-top: 4px; letter-spacing: 0.3px; font-weight: bold; opacity: 0.8;">{code_line}</div></td>'
        f'</tr>'
        f'</table>'
        f'</div>'
    )
    
    st.markdown(matrix_html, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.copy_to_clipboard(f"Результат розрахунку для {user_name if user_name else 'Гість'} ({date_str}), колір: {theme_choice}: {code_line}")
    st.success("📋 Результат скопійовано! Можна вставити в Telegram.")
