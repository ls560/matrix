import streamlit as st

# 1. НАЛАШТУВАННЯ СТОРІНКИ ДЛЯ МОБІЛЬНИХ ПРИСТРОЇВ
st.set_page_config(
    page_title="Нумерологічний Калькулятор", 
    page_icon="🔮", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Стилізація інтерфейсу через CSS: робимо інтерфейс компактним, як на телефоні
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
    </style>
""", unsafe_allow_html=True)

# 2. НАЛАШТУВАННЯ КОЛІРНИХ ТЕМ
st.markdown("<h3 style='text-align: center; color: #4A3B32; font-size: 16px; margin-bottom: 5px;'>Оберіть колір теми:</h3>", unsafe_allow_html=True)
theme_choice = st.selectbox(
    "Тема", 
    ["Класичний беж (як на фото)", "Ніжна троянда", "Свіжа м'ята", "Шляхетний сірий"], 
    label_visibility="collapsed"
)

# Визначаємо кольори залежно від обраної теми
if theme_choice == "Класичний беж (як на фото)":
    main_bg = "#C4B29E"     # Колір фону картки
    header_bg = "#A3907C"   # Колір верхньої панелі (де дата)
    text_color = "#2E2520"  # Колір тексту
    accent_bg = "#FAF6F0"   # Світлий фон для додаткових чисел
elif theme_choice == "Ніжна троянда":
    main_bg = "#E5BFC3"
    header_bg = "#C49297"
    text_color = "#3B2224"
    accent_bg = "#FDF8F9"
elif theme_choice == "Свіжа м'ята":
    main_bg = "#BBDCD5"
    header_bg = "#91BAB2"
    text_color = "#1D332F"
    accent_bg = "#F5FAF9"
else:
    main_bg = "#CCD4DB"
    header_bg = "#9FAAB5"
    text_color = "#242A30"
    accent_bg = "#F7FAFC"

st.markdown("<hr style='margin: 15px 0; border: 0; border-top: 1px solid #ddd;'>", unsafe_allow_html=True)

# 3. ПОЛЯ ВВЕДЕННЯ ДАНИХ (Ім'я та Дата народження)
st.markdown("<h3 style='text-align: center; color: #4A3B32; font-size: 20px; margin-bottom: 5px;'>Ваше Ім'я</h3>", unsafe_allow_html=True)
user_name = st.text_input("Ім'я", value="", placeholder="Введіть ваше ім'я...", label_visibility="collapsed")

st.markdown("<h3 style='text-align: center; color: #4A3B32; font-size: 20px; margin-top: 15px; margin-bottom: 5px;'>Ваша дата народження</h3>", unsafe_allow_html=True)

# Створюємо 3 випадаючі списки в один рядок, як на скріншоті
col_d, col_m, col_y = st.columns(3)
with col_d:
    day = st.selectbox("День", list(range(1, 32)), index=16) # 17 за замовчуванням
with col_m:
    months = ["Січень", "Лютий", "Березень", "Квітень", "Травень", "Червень", "Липень", "Серпень", "Вересень", "Жовтень", "Листопад", "Грудень"]
    month_name = st.selectbox("Місяць", months, index=11) # Грудень за замовчуванням
with col_y:
    year = st.selectbox("Рік", list(range(1940, 2030)), index=49) # 1989 за замовчуванням

st.markdown("<br>", unsafe_allow_html=True)

# КНОПКА "РОЗРАХУВАТИ"
if st.button("Розрахувати", use_container_width=True):
    month_num = months.index(month_name) + 1
    date_str = f"{day:02d}.{month_num:02d}.{year}"
    
    # -------------------------------------------------------------------------
    # АВТОМАТИЧНА ЛОГІКА РОЗРАХУНКУ ПІФАГОРОВОЇ МАТРИЦІ
    # -------------------------------------------------------------------------
    digits = [int(d) for d in f"{day}{month_num}{year}"]
    
    # Крок 1: Перше робоче число (сума всіх цифр дати)
    num1 = sum(digits)
    
    # Крок 2: Друге робоче число (сума цифр першого робочого числа)
    num2 = sum([int(d) for d in str(num1)])
    
    # Крок 3: Третє робоче число (перше число мінус подвоєна перша цифра дня)
    day_str = f"{day:02d}"
    first_day_digit = int(day_str[0]) if int(day_str[0]) != 0 else int(day_str[1])
    num3 = num1 - (2 * first_day_digit)
    
    # Крок 4: Четверте робоче число (сума цифр третього робочого числа)
    num4 = sum([int(d) for d in str(num3)])
    
    additional_numbers = f"{num1}, {num2}, {num3}, {num4}"
    
    # Рахуємо кількість кожної цифри в даті та робочих числах
    all_content = f"{day}{month_num}{year}{num1}{num2}{num3}{num4}"def get_cell(digit):
        count = all_content.count(str(digit))
        return str(digit) * count if count > 0 else "—"
    
    # Заповнюємо клітинки квадрата
    character = get_cell(1)
    energy = get_cell(2)
    interest = get_cell(3)
    health = get_cell(4)
    logic = get_cell(5)
    work = get_cell(6)
    luck = get_cell(7)
    duty = get_cell(8)
    memory = get_cell(9)
    
    # Розрахунок лінійних показників (суми цифр по лініях)
    chyslo_doli = num2
    
    c1 = all_content.count('1') + all_content.count('2') + all_content.count('3')
    temperament = str(c1) if c1 > 0 else "—"
    
    r1 = all_content.count('1') + all_content.count('4') + all_content.count('7')
    goal = str(r1) if r1 > 0 else "—"
    
    r2 = all_content.count('2') + all_content.count('5') + all_content.count('8')
    family = str(r2) if r2 > 0 else "—"
    
    r3 = all_content.count('3') + all_content.count('6') + all_content.count('9')
    habits = str(r3) if r3 > 0 else "—"
    
    self_esteem = str(all_content.count('1') + all_content.count('4') + all_content.count('7'))
    household = str(all_content.count('2') + all_content.count('5') + all_content.count('8'))
    
    code_line = f"{character}/ {energy}/ {interest}/ {health}/ {logic}/ {work}/ {luck}/ {duty}/ {memory}/ ЧД {chyslo_doli}"

    # 4. ВІДОБРАЖЕННЯ МОБІЛЬНОЇ КАРТКИ (HTML/CSS)
    if user_name:
        st.markdown(f"<h3 style='text-align: center; color: {text_color}; font-weight: bold;'>✨ {user_name} ✨</h3>", unsafe_allow_html=True)
        
    matrix_html = f"""
    <div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; 
                max-width: 100%; margin: 0 auto; background-color: {main_bg}; padding: 12px; border-radius: 24px; 
                box-shadow: 0px 10px 25px rgba(0,0,0,0.08); color: {text_color};">
        
        <table style="width: 100%; border-collapse: collapse; margin-bottom: 8px; text-align: center; background-color: {header_bg}; border-radius: 16px 16px 0 0; overflow: hidden; color: #ffffff;">
            <tr>
                <td style="padding: 16px 10px; font-size: 22px; font-weight: bold; width: 40%; border-right: 1px solid rgba(255,255,255,0.2);">{date_str}</td>
                <td style="padding: 10px; border-right: 1px solid rgba(255,255,255,0.2); width: 30%;">
                    <span style="font-size: 11px; opacity: 0.85; display:block; margin-bottom: 2px;">Число Долі</span>
                    <span style="font-size: 22px; font-weight: bold;">{chyslo_doli}</span>
                </td>
                <td style="padding: 10px; width: 30%;">
                    <span style="font-size: 11px; opacity: 0.85; display:block; margin-bottom: 2px;">Темперамент</span>
                    <span style="font-size: 22px; font-weight: bold;">{temperament}</span>
                </td>
            </tr>
        </table>

        <table style="width: 100%; border-collapse: collapse; text-align: center; background-color: #ffffff; border-radius: 0 0 16px 16px; overflow: hidden;">
            <tr style="border-bottom: 1px solid #EAEAEA;">
                <td style="padding: 12px 6px; width: 25%; border-right: 1px solid #EAEAEA;">
                    <span style="font-size: 11px; color: #8A8A8F; display:block; margin-bottom: 4px;">Характер</span>
                    <span style="font-size: 18px; font-weight: bold; color: {text_color};">{character}</span>
                </td>
                <td style="padding: 12px 6px; width: 25%; border-right: 1px solid #EAEAEA;">
                    <span style="font-size: 11px; color: #8A8A8F; display:block; margin-bottom: 4px;">Здоров'я</span>
                    <span style="font-size: 18px; font-weight: bold; color: {text_color};">{health}</span>
                </td>
                <td style="padding: 12px 6px; width: 25%; border-right: 1px solid #EAEAEA;">
                    <span style="font-size: 11px; color: #8A8A8F; display:block; margin-bottom: 4px;">Удача</span><span style="font-size: 18px; font-weight: bold; color: {text_color};">{luck}</span>
                </td>
                <td style="padding: 12px 6px; width: 25%; background-color: {main_bg}25;">
                    <span style="font-size: 11px; color: #8A8A8F; display:block; margin-bottom: 4px;">Ціль</span>
                    <span style="font-size: 18px; font-weight: bold; color: {text_color};">{goal}</span>
                </td>
            </tr>
            <tr style="border-bottom: 1px solid #EAEAEA;">
                <td style="padding: 12px 6px; border-right: 1px solid #EAEAEA;">
                    <span style="font-size: 11px; color: #8A8A8F; display:block; margin-bottom: 4px;">Енергія</span>
                    <span style="font-size: 18px; font-weight: bold; color: {text_color};">{energy}</span>
                </td>
                <td style="padding: 12px 6px; border-right: 1px solid #EAEAEA;">
                    <span style="font-size: 11px; color: #8A8A8F; display:block; margin-bottom: 4px;">Логіка</span>
                    <span style="font-size: 18px; font-weight: bold; color: {text_color};">{logic}</span>
                </td>
                <td style="padding: 12px 6px; border-right: 1px solid #EAEAEA;">
                    <span style="font-size: 11px; color: #8A8A8F; display:block; margin-bottom: 4px;">Обов'язок</span>
                    <span style="font-size: 18px; font-weight: bold; color: {text_color};">{duty}</span>
                </td>
                <td style="padding: 12px 6px; background-color: {main_bg}25;">
                    <span style="font-size: 11px; color: #8A8A8F; display:block; margin-bottom: 4px;">Сім'я</span>
                    <span style="font-size: 18px; font-weight: bold; color: {text_color};">{family}</span>
                </td>
            </tr>
            <tr style="border-bottom: 1px solid #EAEAEA;">
                <td style="padding: 12px 6px; border-right: 1px solid #EAEAEA;">
                    <span style="font-size: 11px; color: #8A8A8F; display:block; margin-bottom: 4px;">Цікавість</span>
                    <span style="font-size: 18px; font-weight: bold; color: {text_color};">{interest}</span>
                </td>
                <td style="padding: 12px 6px; border-right: 1px solid #EAEAEA;">
                    <span style="font-size: 11px; color: #8A8A8F; display:block; margin-bottom: 4px;">Праця</span>
                    <span style="font-size: 18px; font-weight: bold; color: {text_color};">{work}</span>
                </td>
                <td style="padding: 12px 6px; border-right: 1px solid #EAEAEA;">
                    <span style="font-size: 11px; color: #8A8A8F; display:block; margin-bottom: 4px;">Пам'ять</span>
                    <span style="font-size: 18px; font-weight: bold; color: {text_color};">{memory}</span>
                </td>
                <td style="padding: 12px 6px; background-color: {main_bg}25;">
                    <span style="font-size: 11px; color: #8A8A8F; display:block; margin-bottom: 4px;">Звички</span>
                    <span style="font-size: 18px; font-weight: bold; color: {text_color};">{habits}</span>
                </td>
            </tr>
            <tr>
                <td style="padding: 12px 6px; border-right: 1px solid #EAEAEA; background-color: {main_bg}25;">
                    <span style="font-size: 11px; color: #8A8A8F; display:block; margin-bottom: 4px;">Самооцінка</span>
                    <span style="font-size: 18px; font-weight: bold; color: {text_color};">{self_esteem}</span>
                </td>
                <td style="padding: 12px 6px; border-right: 1px solid #EAEAEA; background-color: {main_bg}25;">
                    <span style="font-size: 11px; color: #8A8A8F; display:block; margin-bottom: 4px;">Побут</span>
                    <span style="font-size: 18px; font-weight: bold; color: {text_color};">{household}</span>
                </td><td colspan="2" style="padding: 8px 4px; font-size: 12px; text-align: center; background-color: {accent_bg};">
                    <span style="color: #8A8A8F; font-size: 11px; display: block; margin-bottom: 2px;">Додаткові Числа</span>
                    <b style="color: {text_color}; font-size: 13px;">{additional_numbers}</b>
                    <div style="font-size: 10px; margin-top: 4px; letter-spacing: 0.3px; font-weight: bold; opacity: 0.8;">{code_line}</div>
                </td>
            </tr>
        </table>
    </div>
    """
    
    st.markdown(matrix_html, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Кнопка автоматичного копіювання в один клік
    st.copy_to_clipboard(f"Результат розрахунку для {user_name if user_name else 'Гість'} ({date_str}): {code_line}")
    st.success("📋 Результат скопійовано! Можна вставити в Telegram.")
