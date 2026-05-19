# Конкатенація всіх цифр для підрахунку в матриці
    all_content = f"{day}{month_num}{year}{num1}{num2}{num3}{num4}"
    
    # ТУТ БУЛА ПОМИЛКА — ЗАРАЗ ВСЕ РОЗДІЛЕНО ПРАВИЛЬНО:
    def get_cell(digit):
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
    
    # Розрахунок лінійних показників (кількість цифр у лініях)
    chyslo_doli = num2
    # Якщо потрібно згортати Число Долі до однозначного (крім 11):
    if chyslo_doli > 9 and chyslo_doli != 11:
        chyslo_doli = sum([int(d) for d in str(chyslo_doli)])
        
    temperament = str(all_content.count('1') + all_content.count('2') + all_content.count('3'))
    goal = str(all_content.count('1') + all_content.count('4') + all_content.count('7'))
    family = str(all_content.count('2') + all_content.count('5') + all_content.count('8'))
    habits = str(all_content.count('3') + all_content.count('6') + all_content.count('9'))
    
    self_esteem = str(all_content.count('1') + all_content.count('4') + all_content.count('7'))
    household = str(all_content.count('2') + all_content.count('5') + all_content.count('8'))
    
    code_line = f"{character}/ {energy}/ {interest}/ {health}/ {logic}/ {work}/ {luck}/ {duty}/ {memory}/ ЧД {chyslo_doli}"

    # 4. ВІДОБРАЖЕННЯ МОБІЛЬНОЇ КАРТКИ (HTML/CSS)
    if user_name:
        st.markdown(f"<h3 style='text-align: center; color: {text_color}; font-weight: bold; margin-top: 10px;'>✨ {user_name} ✨</h3>", unsafe_allow_html=True)
        
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
                    <span style="font-size: 11px; color: #8A8A8F; display:block; margin-bottom: 4px;">Удача</span>
                    <span style="font-size: 18px; font-weight: bold; color: {text_color};">{luck}</span>
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
                </td>
                <td colspan="2" style="padding: 8px 4px; font-size: 12px; text-align: center; background-color: {accent_bg};">
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
    
    # Кнопка копіювання результату
    st.copy_to_clipboard(f"Результат розрахунку для {user_name if user_name else 'Гість'} ({date_str}): {code_line}")
    st.success("📋 Результат скопійовано! Можна вставити в Telegram чи нотатки.")
