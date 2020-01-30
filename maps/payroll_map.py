

class PayrollMap:
    # Locators
    payroll_menu = "//span[contains(text(),'Nóm')]"
    close_video = "//*[@id='Capa_1']"
    btn_new = "//button[contains(text(),'Nueva')]"
    group = "//*[@id='payroll_group_id']//input"
    startdate = "//*[@id='start_date']//input"
    stardate_incidence = "//*[@id='start_date_incidence']//input"
    endate_incidence = "//*[@id='end_date_incidence']//input"
    # input_startate = "//*[@id='start_date']//input[value='01/06/2019']"
    # year = "//span[@class='react-datepicker__year-read-view--down-arrow']"
    # select_year = "//span[@class='react-datepicker__year-read-view--selected-year']//contains(text(),'2019')"
    # prev_month = "//button[@class='react-datepicker__navigation react-datepicker__navigation--previous']"
    btn_sub = "//button[contains(text(),'Guardar')]"
