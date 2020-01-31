

class PayrollMap:
    # Locators
    payroll_menu = "//span[contains(text(),'Nóm')]"
    close_video = "//*[@id='Capa_1']"
    btn_new = "//button[contains(text(),'Nueva')]"
    group = "//*[@id='payroll_group_id']//input"
    stardate_incidence = "//input[@id='start_date_incidence']"
    endate_incidence = "//input[@id='end_date_incidence']"
    btn_sub = "//button[contains(text(),'Guardar')]"
    new_payroll = "//h2[@class='active-payrolls-subtitle']"
    btn_start = "//button[contains(text(),'Comenzar')]"
    open_emp = "//h3[contains(text(),'Empleados en la nómina')]"
    btn_continue = "//button[contains(text(),'Continuar')]"
    btn_delete = "//button[contains(text(),'Eliminar nómina')]"
    btn_confirm_del = "//button[contains(text(),'Eliminar')]"
