import time
from data import data
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from pages.urban_routes_page import UrbanRoutesPage

#pruebas en esta clase
class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        options = Options()
        options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(service=Service(),options=options)
        cls.driver.get(data.urban_routes_url)
        cls.routes_page=UrbanRoutesPage(cls.driver)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        assert self.routes_page.get_from() == address_from
        assert self.routes_page.get_to() == address_to

    #2.seleccionar tarifa comfort
    def test_select_comfort_tariff(self):
        self.driver.get(data.urban_routes_url)
        self.routes_page.set_route(data.address_from, data.address_to)
        self.routes_page.click_request_taxi_button()
        self.routes_page.click_comfort_icon()
        comfort_tariff = self.routes_page.get_comfort_icon().text
        assert comfort_tariff == "Comfort"

    #3.ingresar numero telefonico
    def test_set_phone(self):
        self.driver.get(data.urban_routes_url)
        self.routes_page.set_route(data.address_from, data.address_to)
        self.routes_page.click_request_taxi_button()
        self.routes_page.click_phone_button()
        self.routes_page.set_phone(data.phone_number)
        self.routes_page.click_next_button_phone()
        self.routes_page.set_phone_code_field()
        self.routes_page.click_phone_confirm_button()
        assert self.routes_page.get_phone()==data.phone_number

    #4.ingresar tarjeta de credito
    def test_set_payment_method(self):
        self.driver.get(data.urban_routes_url)
        self.routes_page.set_route(data.address_from, data.address_to)
        self.routes_page.click_request_taxi_button()
        self.routes_page.click_payment_method()
        self.routes_page.click_add_card()
        self.routes_page.set_card_number(data.card_number,data.card_code)
        self.routes_page.click_add_card_submit()
        assert self.routes_page.get_card_added()== "Tarjeta"

     #5.mensaje conductor
    def test_set_comment(self):
        self.driver.get(data.urban_routes_url)
        self.routes_page.set_route(data.address_from, data.address_to)
        self.routes_page.click_request_taxi_button()
        self.routes_page.set_field_comment(data.message_for_driver)
        message = self.routes_page.get_comment()
        assert message == data.message_for_driver

    #6.pedir manta y pañuelos
    def test_order_blanket_handkerchiefs(self):
        self.driver.get(data.urban_routes_url)
        self.routes_page.set_route(data.address_from, data.address_to)
        self.routes_page.click_request_taxi_button()
        self.routes_page.click_comfort_icon()
        self.routes_page.click_blanket_switch()
        assert self.routes_page.get_blanket_switch_active () is True

    #7.pedir 2 helados
    def test_order_two_icecreams(self):
        self.driver.get(data.urban_routes_url)
        self.routes_page.set_route(data.address_from, data.address_to)
        self.routes_page.click_request_taxi_button()
        self.routes_page.click_comfort_icon()
        self.routes_page.click_twice_ice_cream()
        assert self.routes_page.get_icecream_counter_value() == "2"

    #8.modal buscar un taxi
    def test_modal_search_taxi(self):
        self.driver.get(data.urban_routes_url)
        self.routes_page.set_route(data.address_from, data.address_to)
        self.routes_page.click_request_taxi_button()
        self.routes_page.click_phone_button()
        self.routes_page.set_phone(data.phone_number)
        self.routes_page.click_next_button_phone()
        self.routes_page.set_phone_code_field()
        self.routes_page.click_phone_confirm_button()
        self.routes_page.click_button2_order_taxi()
        assert self.routes_page.get_modal_search_taxi().is_displayed()
        self.routes_page.click_cancel_order()

    #9. Información del conductor, extra.
    def test_driver_info(self):
        self.driver.get(data.urban_routes_url)
        self.routes_page.set_route(data.address_from, data.address_to)
        self.routes_page.click_request_taxi_button()
        self.routes_page.click_phone_button()
        self.routes_page.set_phone(data.phone_number)
        self.routes_page.click_next_button_phone()
        self.routes_page.set_phone_code_field()
        self.routes_page.click_phone_confirm_button()
        self.routes_page.set_field_comment(data.message_for_driver)
        self.routes_page.click_button2_order_taxi()
        assert "El conductor llegará en" in self.routes_page.get_info_modal_taxi()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
