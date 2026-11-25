import allure
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):
    @allure.step("Заполнить первую страницу формы: 'Для кого самокат'")
    def fill_user_info(self, user_data):
        self.send_keys_to_input(OrderPageLocators.NAME_INPUT, user_data["name"])
        self.send_keys_to_input(OrderPageLocators.SURNAME_INPUT, user_data["surname"])
        self.send_keys_to_input(OrderPageLocators.ADDRESS_INPUT, user_data["address"])

        # Выбор станции метро из выпадающего списка
        self.click_on_element(OrderPageLocators.METRO_INPUT)
        self.send_keys_to_input(OrderPageLocators.METRO_INPUT, user_data["metro"])
        method, locator = OrderPageLocators.METRO_STATION_OPTION
        self.click_on_element((method, locator.format(user_data["metro"])))

        self.send_keys_to_input(OrderPageLocators.PHONE_INPUT, user_data["phone"])
        self.click_on_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполнить вторую страницу формы: 'Про аренду'")
    def fill_rent_info(self, user_data):
        # Ввод даты и нажатие Enter, чтобы закрыть календарь
        date_input = self.wait_for_element(OrderPageLocators.DATE_INPUT)
        date_input.send_keys(user_data["date"])
        date_input.send_keys(Keys.ENTER)

        # Выбор срока аренды
        self.click_on_element(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        method, locator = OrderPageLocators.RENTAL_PERIOD_OPTION
        self.click_on_element((method, locator.format(user_data["period"])))

        # Выбор цвета самоката
        if user_data["color"] == "black":
            self.click_on_element(OrderPageLocators.COLOR_BLACK_CHECKBOX)
        elif user_data["color"] == "grey":
            self.click_on_element(OrderPageLocators.COLOR_GREY_CHECKBOX)

        self.send_keys_to_input(OrderPageLocators.COMMENT_INPUT, user_data["comment"])
        self.click_on_element(OrderPageLocators.ORDER_SUBMIT_BUTTON)

    @allure.step("Подтвердить оформление заказа в модальном окне")
    def confirm_order(self):
        self.click_on_element(OrderPageLocators.CONFIRM_YES_BUTTON)

    @allure.step("Проверить отображение окна об успешном создании заказа")
    def is_order_success_displayed(self):
        return self.wait_for_element(OrderPageLocators.ORDER_SUCCESS_MODAL).is_displayed()
