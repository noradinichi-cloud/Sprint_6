import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import OrderData


class TestOrderPage:
    @allure.title("Позитивный сценарий оформления заказа самоката (точка входа: {order_button})")
    @pytest.mark.parametrize(
        "order_button, user_data",
        [
            ("top", OrderData.USER_1),
            ("bottom", OrderData.USER_2),
        ]
    )
    def test_order_scooter_positive_flow(self, driver, order_button, user_data):
        main_page = MainPage(driver)
        main_page.accept_cookies()

        if order_button == "top":
            main_page.click_top_order_button()
        elif order_button == "bottom":
            main_page.click_bottom_order_button()

        order_page = OrderPage(driver)
        order_page.fill_user_info(user_data)
        order_page.fill_rent_info(user_data)
        order_page.confirm_order()

        assert order_page.is_order_success_displayed()

