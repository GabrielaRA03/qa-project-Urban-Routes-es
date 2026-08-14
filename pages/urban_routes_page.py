from selenium.webdriver import Keys #simula tab
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from helpers.retrieve_code import retrieve_phone_code
from data import data

#localizadores y métodos
class UrbanRoutesPage:
    from_field = (By.ID, "from")
    to_field = (By.ID, "to")
    request_taxi_button = (By.CSS_SELECTOR,".button.round")
    comfort_icon = (By.XPATH, "//div[@class='tcard-title' and text()='Comfort']")

    phone_button = (By.CLASS_NAME,"np-button")
    phone_field = (By.ID,"phone")
    next_button_phone = (By.XPATH, "//button[@class='button full' and text()='Siguiente']")
    phone_code_field = (By.ID,"code")
    phone_confirm_button = (By.XPATH, "//button[@class='button full' and text()='Confirmar']")
    phone_number=(By.CLASS_NAME,'np-text')

    payment_method = (By.CSS_SELECTOR, ".pp-button.filled")
    add_card = (By.XPATH, "//div[@class='pp-row disabled'][.//div[@class='pp-title' and text()='Agregar tarjeta']]")
        #(By.XPATH,"//div[contains(@class,'section')][.//div[@class='head' and text()='Agregar tarjeta']]//button[@type='submit']")
    card_number_field = (By.CSS_SELECTOR,"input#number")
    card_code_field = (By.CSS_SELECTOR, ".card-code-input #code")
    add_card_submit = (By.XPATH, "//button[@class='button full' and text()='Agregar']")
    close_payment_method=(By.XPATH,"//div[@class='payment-picker open']//button[@class='close-button section-close']")
        #(By.CSS_SELECTOR, "//div[contains(@class, 'section') and contains(@class, 'active')]/button[contains(@class, 'close-button')]")
    card_added = (By.XPATH,"//div[@class='pp-title' and text()='Tarjeta']")

    field_comment = (By.ID, "comment")

    blanket_switch  = (By.XPATH,"//div[@class='r-sw-label' and text()='Manta y pañuelos']/following-sibling::div//span[@class='slider round']")
    blanket_switch_active = (By.XPATH,"//div[@class='r-sw-label' and text()='Manta y pañuelos']/following-sibling::div//input[@type='checkbox']")

    icecream_counter = (By.XPATH,"//div[@class='r-counter-label' and text()='Helado']/following-sibling::div//div[@class='counter-plus']")
    icecream_counter_value = (By.XPATH,"//div[@class='r-counter-label' and text()='Helado']/following-sibling::div//div[@class='counter-value']")

    button2_order_taxi =(By.XPATH,"//span[@class='smart-button-main' and text()='Pedir un taxi']")
    modal_search_taxi= (By.CLASS_NAME, "order-header-title")

    cancel_order= ( By.XPATH, "//button[@class='order-button'][.//img[@alt='close']]")


    def __init__(self, driver):
        self.driver = driver
        self.wait=WebDriverWait(driver, 10)

    def set_from(self, from_address):
        self.wait.until(
            EC.presence_of_element_located(self.from_field)
        ).send_keys(from_address)
        #self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.wait.until(
            EC.presence_of_element_located(self.to_field)
        ).send_keys(to_address)

    def get_from(self):
       return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    def get_request_taxi_button(self):
       return self.wait.until(
           EC.element_to_be_clickable(self.request_taxi_button)
       )
    def click_request_taxi_button(self):
        self.get_request_taxi_button().click()


    def get_comfort_icon(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.comfort_icon)
        )
    def click_comfort_icon(self):
        self.get_comfort_icon().click()


    def get_phone_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.phone_button))
    def click_phone_button(self):
        self.get_phone_button().click()
    def set_phone(self,phone_number):
        self.wait.until(EC.element_to_be_clickable(self.phone_field)
                        ).send_keys(phone_number)
    def get_next_button_phone(self):
        return self.wait.until(EC.element_to_be_clickable(self.next_button_phone))
    def click_next_button_phone(self):
        self.get_next_button_phone().click()
    def set_phone_code_field(self):
        phone_code= retrieve_phone_code(self.driver)
        return self.wait.until(EC.element_to_be_clickable(self.phone_code_field)
            ).send_keys(phone_code)
    def get_phone_confirm_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.phone_confirm_button))
    def click_phone_confirm_button(self):
        self.get_phone_confirm_button().click()
    def get_phone(self):
        return self.wait.until(EC.visibility_of_element_located(self.phone_number)
            ).text

    def get_payment_method(self):
        return self.wait.until(EC.element_to_be_clickable(self.payment_method))
    def click_payment_method(self):
        self.driver.find_element(*self.payment_method).click()
    def get_add_card(self):
        return self.wait.until(EC.element_to_be_clickable(self.add_card))
    def click_add_card(self):
        self.driver.find_element(*self.add_card).click()
    def set_card_number(self,card_number, card_code):
        self.wait.until(EC.element_to_be_clickable(self.card_number_field)
                               ).send_keys(card_number)
        self.wait.until(EC.element_to_be_clickable(self.card_code_field)
                               ).send_keys(card_code,Keys.TAB)
    def get_add_card_submit(self):
        return self.wait.until(EC.element_to_be_clickable(self.add_card_submit))
    def click_add_card_submit(self):
        self.driver.find_element(*self.add_card_submit).click()
    def get_card_added(self):
        return self.wait.until(EC.presence_of_element_located(self.card_added)
                               ).text

    def get_field_comment(self):
        return self.wait.until(EC.element_to_be_clickable(self.field_comment))
    def set_field_comment(self,field_comment):
        self.wait.until(EC.element_to_be_clickable(self.field_comment)
                        ).send_keys(data.message_for_driver)
    def get_comment(self):
        return self.wait.until(EC.element_to_be_clickable(self.field_comment)
                               ).get_property('value')

    def get_blanket_switch(self):
        return self.wait.until(EC.element_to_be_clickable(self.blanket_switch))
    def click_blanket_switch(self):
        self.driver.find_element(*self.blanket_switch).click()
    def get_blanket_switch_active(self):
        return self.wait.until(EC.presence_of_element_located(self.blanket_switch_active)
                               ).is_selected()

    def get_ice_cream_counter(self):
        return self.wait.until(EC.element_to_be_clickable(self.icecream_counter))
    def click_twice_ice_cream(self):
        counter = self.driver.find_element(*self.icecream_counter)
        counter.click()
        counter.click()
    def get_icecream_counter_value(self):
        return self.wait.until(EC.presence_of_element_located(self.icecream_counter_value)
                               ).text

    def get_button2_order_taxi(self):
        return self.wait.until(EC.element_to_be_clickable(self.button2_order_taxi))
    def click_button2_order_taxi(self):
        self.driver.find_element(*self.button2_order_taxi).click()
    def get_modal_search_taxi(self):
        return self.wait.until(EC.visibility_of_element_located(self.modal_search_taxi))
    def get_cancel_order(self):
        return self.wait.until(EC.element_to_be_clickable(self.cancel_order))
    def click_cancel_order(self):
        self.get_cancel_order().click()

    def get_info_modal_taxi(self):
        WebDriverWait(self.driver, 60).until(EC.text_to_be_present_in_element(
            self.modal_search_taxi,"El conductor llegará en"))
        return self.driver.find_element(*self.modal_search_taxi).text


