import pytest
import allure
from pages.main_page import MainPage
from data import FaqData, Urls


class TestMainPage:
    @allure.title("Проверка текста ответа в выпадающем списке 'Вопросы о важном' (вопрос №{question_index})")
    @pytest.mark.parametrize("question_index, expected_answer", FaqData.EXPECTED_ANSWERS.items())
    def test_faq_question_shows_expected_answer(self, driver, question_index, expected_answer):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        main_page.click_faq_question(question_index)
        actual_answer = main_page.get_faq_answer_text(question_index)

        assert actual_answer == expected_answer

    @allure.title("Переход на главную страницу при клике на логотип 'Самокат'")
    def test_click_scooter_logo_redirects_to_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.click_top_order_button()
        main_page.click_scooter_logo()

        assert main_page.get_current_url() == Urls.MAIN_PAGE

    @allure.title("Открытие главной страницы Дзена в новой вкладке при клике на логотип 'Яндекс'")
    def test_click_yandex_logo_opens_dzen_in_new_window(self, driver):
        main_page = MainPage(driver)
        main_page.click_yandex_logo()
        main_page.switch_to_new_window()
        main_page.wait_for_url_contains(Urls.DZEN_URL)

        assert Urls.DZEN_URL in main_page.get_current_url()
