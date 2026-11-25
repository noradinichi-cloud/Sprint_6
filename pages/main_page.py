import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    @allure.step("Закрыть баннер с куками")
    def accept_cookies(self):
        self.click_on_element(MainPageLocators.COOKIE_BUTTON)

    @allure.step("Нажать на верхнюю кнопку 'Заказать'")
    def click_top_order_button(self):
        self.click_on_element(MainPageLocators.ORDER_BUTTON_TOP)

    @allure.step("Проскроллить и нажать на нижнюю кнопку 'Заказать'")
    def click_bottom_order_button(self):
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_BOTTOM)
        self.click_on_element(MainPageLocators.ORDER_BUTTON_BOTTOM)

    @allure.step("Нажать на логотип 'Самокат'")
    def click_scooter_logo(self):
        self.click_on_element(MainPageLocators.SCOOTER_LOGO)

    @allure.step("Нажать на логотип 'Яндекс'")
    def click_yandex_logo(self):
        self.click_on_element(MainPageLocators.YANDEX_LOGO)

    @allure.step("Проскроллить к вопросу №{question_index} и раскрыть его")
    def click_faq_question(self, question_index):
        method, locator = MainPageLocators.FAQ_QUESTION
        formatted_locator = (method, locator.format(question_index))
        self.scroll_to_element(formatted_locator)
        self.click_with_js(formatted_locator)

    @allure.step("Получить текст ответа на вопрос №{question_index}")
    def get_faq_answer_text(self, question_index):
        method, locator = MainPageLocators.FAQ_ANSWER
        formatted_locator = (method, locator.format(question_index))
        return self.get_text_on_element(formatted_locator)

