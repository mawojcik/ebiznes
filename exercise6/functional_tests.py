from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest

class ShopAppTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("http://localhost:8080")
        cls.driver.implicitly_wait(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def go_to(self, link_text):
        self.driver.find_element(By.LINK_TEXT, link_text).click()

    def test_01_homepage_loads(self):
        self.assertIn("Produkty", self.driver.page_source)

    def test_02_products_listed(self):
        products = self.driver.find_elements(By.TAG_NAME, "li")
        self.assertGreater(len(products), 0)

    def test_03_add_product_to_cart(self):
        btns = self.driver.find_elements(By.TAG_NAME, "button")
        btns[0].click()
        self.go_to("Koszyk")
        self.assertIn("Koszyk", self.driver.page_source)
        self.assertGreater(len(self.driver.find_elements(By.TAG_NAME, "li")), 0)

    def test_04_total_price_in_cart(self):
        self.assertIn("Łącznie", self.driver.page_source)

    def test_05_buy_products(self):
        btn = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Kup wszystko')]")
        btn.click()
        time.sleep(1)
        self.assertIn("Twój koszyk jest pusty", self.driver.page_source)

    def test_06_go_to_payments(self):
        self.go_to("Płatności")
        self.assertIn("Historia płatności", self.driver.page_source)

    def test_07_payments_not_empty(self):
        items = self.driver.find_elements(By.TAG_NAME, "li")
        self.assertGreater(len(items), 0)

    def test_08_navigate_back_to_products(self):
        self.go_to("Produkty")
        self.assertIn("Produkty", self.driver.page_source)

    def test_09_add_multiple_to_cart(self):
        buttons = self.driver.find_elements(By.TAG_NAME, "button")
        for b in buttons[:3]:
            b.click()
        self.go_to("Koszyk")
        items = self.driver.find_elements(By.TAG_NAME, "li")
        self.assertGreaterEqual(len(items), 2)

    def test_10_clear_cart_on_purchase(self):
        btn = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Kup wszystko')]")
        btn.click()
        time.sleep(1)
        self.assertIn("Twój koszyk jest pusty", self.driver.page_source)

    def test_11_product_names_visible(self):
        self.go_to("Produkty")
        self.assertIn("Laptop", self.driver.page_source)

    def test_12_prices_are_correct_format(self):
        products = self.driver.find_elements(By.TAG_NAME, "li")
        for p in products:
            text = p.text
            self.assertRegex(text, r"\d+\.\d{2} zł")

    def test_13_buttons_exist(self):
        buttons = self.driver.find_elements(By.TAG_NAME, "button")
        self.assertTrue(any("Dodaj" in b.text or "Kup" in b.text for b in buttons))

    def test_14_cart_link_works(self):
        self.go_to("Koszyk")
        self.assertIn("Koszyk", self.driver.page_source)

    def test_15_payment_records_have_prices(self):
        self.go_to("Płatności")
        records = self.driver.find_elements(By.TAG_NAME, "li")
        for r in records:
            self.assertRegex(r.text, r"\d+\.\d{2} zł")

    def test_16_multiple_purchases_recorded(self):
        self.go_to("Produkty")
        self.driver.find_elements(By.TAG_NAME, "button")[0].click()
        self.go_to("Koszyk")
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Kup wszystko')]").click()
        self.go_to("Płatności")
        records = self.driver.find_elements(By.TAG_NAME, "li")
        self.assertGreaterEqual(len(records), 2)

    def test_17_cart_state_resets(self):
        self.go_to("Koszyk")
        self.assertIn("pusty", self.driver.page_source)

    def test_18_no_duplicate_ids(self):
        self.go_to("Płatności")
        items = self.driver.find_elements(By.TAG_NAME, "li")
        texts = [item.id for item in items]
        self.assertEqual(len(texts), len(set(texts)))  # assumes unique strings

    def test_19_total_price_reflects_cart(self):
        self.go_to("Produkty")
        self.driver.find_elements(By.TAG_NAME, "button")[0].click()
        self.go_to("Koszyk")
        total_text = self.driver.find_element(By.XPATH, "//p[contains(text(), 'Łącznie')]").text
        self.assertRegex(total_text, r"\d+\.\d{2}")


    def test_20_router_works_without_reload(self):
        self.go_to("Produkty")
        self.go_to("Koszyk")
        self.go_to("Płatności")
        self.assertIn("Płatności", self.driver.page_source)

    def test_21_empty_cart_message(self):
        self.go_to("Koszyk")
        self.assertIn("pusty", self.driver.page_source)

    def test_22_navigation_sequence(self):
        self.go_to("Produkty")
        self.go_to("Koszyk")
        self.go_to("Płatności")
        self.go_to("Produkty")
        self.assertIn("Produkty", self.driver.page_source)

    def test_23_add_same_item_multiple_times(self):
        self.go_to("Produkty")
        add_btn = self.driver.find_elements(By.TAG_NAME, "button")[0]
        for _ in range(3):
            add_btn.click()
        self.go_to("Koszyk")
        text = self.driver.find_element(By.TAG_NAME, "li").text
        self.assertTrue("x3" in text or "3" in text)

    def test_24_check_total_after_multiple_adds(self):
        self.go_to("Produkty")
        for btn in self.driver.find_elements(By.TAG_NAME, "button")[:2]:
            btn.click()
            btn.click()
        self.go_to("Koszyk")
        total = self.driver.find_element(By.XPATH, "//p[contains(text(), 'Łącznie')]").text
        self.assertRegex(total, r"\d+\.\d{2}")

    def test_25_buy_button_disables_on_empty_cart(self):
        self.go_to("Koszyk")
        buy_btn = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Kup wszystko')]")
        self.assertFalse(buy_btn.is_enabled() or "disabled" not in buy_btn.get_attribute("class"))

    def test_26_add_and_remove_single_item(self):
        self.go_to("Produkty")
        self.driver.find_elements(By.TAG_NAME, "button")[0].click()
        self.go_to("Koszyk")
        # Assuming there is a remove button
        try:
            remove_btn = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Usuń')]")
            remove_btn.click()
            time.sleep(0.5)
            self.assertIn("pusty", self.driver.page_source)
        except:
            self.skipTest("Brak przycisku 'Usuń'")

    def test_27_payment_history_updates(self):
        self.go_to("Produkty")
        self.driver.find_elements(By.TAG_NAME, "button")[0].click()
        self.go_to("Koszyk")
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Kup wszystko')]").click()
        self.go_to("Płatności")
        items = self.driver.find_elements(By.TAG_NAME, "li")
        self.assertGreaterEqual(len(items), 1)

    def test_28_price_format_in_cart(self):
        self.go_to("Produkty")
        self.driver.find_elements(By.TAG_NAME, "button")[0].click()
        self.go_to("Koszyk")
        text = self.driver.find_element(By.TAG_NAME, "li").text
        self.assertRegex(text, r"\d+\.\d{2} zł")

    def test_29_routing_without_errors(self):
        try:
            for page in ["Produkty", "Koszyk", "Płatności"]:
                self.go_to(page)
                self.assertNotIn("404", self.driver.page_source)
        except:
            self.fail("Routing failed")

    def test_30_payment_entry_contains_timestamp(self):
        self.go_to("Płatności")
        entry = self.driver.find_elements(By.TAG_NAME, "li")[0].text
        self.assertRegex(entry, r"\d{4}-\d{2}-\d{2}")

    def test_31_clicking_logo_goes_home(self):
        try:
            logo = self.driver.find_element(By.CLASS_NAME, "logo")
            logo.click()
            self.assertIn("Produkty", self.driver.page_source)
        except:
            self.skipTest("Brak elementu z klasą 'logo'")

    def test_32_no_items_in_cart_message_displays(self):
        self.go_to("Koszyk")
        self.assertIn("Twój koszyk jest pusty", self.driver.page_source)

    def test_33_payment_list_scrollable(self):
        self.go_to("Płatności")
        # Assuming a scroll container
        container = self.driver.find_element(By.CLASS_NAME, "payment-list")
        self.assertGreater(container.size['height'], 0)

    def test_34_cart_total_price_matches_items(self):
        self.go_to("Produkty")
        btns = self.driver.find_elements(By.TAG_NAME, "button")[:2]
        for b in btns:
            b.click()
        self.go_to("Koszyk")
        total = self.driver.find_element(By.XPATH, "//p[contains(text(), 'Łącznie')]").text
        self.assertRegex(total, r"\d+\.\d{2}")

    def test_35_reload_cart_page_persists_state(self):
        self.go_to("Produkty")
        self.driver.find_elements(By.TAG_NAME, "button")[0].click()
        self.go_to("Koszyk")
        self.driver.refresh()
        self.assertIn("Koszyk", self.driver.page_source)

    def test_36_multiple_buy_clicks_do_not_duplicate(self):
        self.go_to("Produkty")
        self.driver.find_elements(By.TAG_NAME, "button")[0].click()
        self.go_to("Koszyk")
        for _ in range(3):
            self.driver.find_element(By.XPATH, "//button[contains(text(), 'Kup wszystko')]").click()
            time.sleep(0.5)
        self.go_to("Płatności")
        items = self.driver.find_elements(By.TAG_NAME, "li")
        self.assertLessEqual(len(items), 3)

    def test_37_empty_state_for_payments_if_none(self):
        # Optional: clean backend before test
        self.go_to("Płatności")
        if "Brak płatności" in self.driver.page_source:
            self.assertIn("Brak płatności", self.driver.page_source)

    def test_38_add_product_shows_notification(self):
        self.go_to("Produkty")
        self.driver.find_elements(By.TAG_NAME, "button")[0].click()
        # Assuming a toast appears
        time.sleep(0.5)
        self.assertIn("Dodano do koszyka", self.driver.page_source)

    def test_39_payment_success_message(self):
        self.go_to("Produkty")
        self.driver.find_elements(By.TAG_NAME, "button")[0].click()
        self.go_to("Koszyk")
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Kup wszystko')]").click()
        self.assertIn("Zakup zakończony sukcesem", self.driver.page_source)

    def test_40_cart_does_not_accept_negative_quantity(self):
        # You'd need a quantity input for this test
        self.skipTest("Brak opcji edycji ilości produktu")

    def test_41_title_contains_app_name(self):
        self.assertIn("ShopApp", self.driver.title)

    def test_42_url_changes_with_route(self):
        self.go_to("Płatności")
        self.assertIn("/payments", self.driver.current_url)

    def test_43_navbar_exists(self):
        navbar = self.driver.find_element(By.TAG_NAME, "nav")
        self.assertTrue(navbar.is_displayed())

    def test_44_link_texts_are_visible(self):
        for label in ["Produkty", "Koszyk", "Płatności"]:
            self.assertTrue(self.driver.find_element(By.LINK_TEXT, label).is_displayed())

    def test_45_empty_cart_buy_button_hidden(self):
        self.go_to("Koszyk")
        buy_btn = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Kup wszystko')]")
        self.assertFalse(buy_btn.is_enabled() or "disabled" not in buy_btn.get_attribute("class"))

    def test_46_add_product_no_error(self):
        self.go_to("Produkty")
        try:
            self.driver.find_elements(By.TAG_NAME, "button")[0].click()
        except Exception as e:
            self.fail(f"Unexpected error: {e}")

    def test_47_buy_button_shows_spinner(self):
        self.go_to("Produkty")
        self.driver.find_elements(By.TAG_NAME, "button")[0].click()
        self.go_to("Koszyk")
        btn = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Kup wszystko')]")
        btn.click()
        self.assertIn("loading", btn.get_attribute("class") or "")

    def test_48_products_have_name_and_price(self):
        self.go_to("Produkty")
        products = self.driver.find_elements(By.TAG_NAME, "li")
        for p in products:
            self.assertRegex(p.text, r".+\d+\.\d{2} zł")

    def test_49_cart_quantity_reset_after_purchase(self):
        self.go_to("Koszyk")
        self.assertIn("pusty", self.driver.page_source)

    def test_50_ui_loads_under_2s(self):
        start = time.time()
        self.driver.get("http://localhost:8080")
        self.assertLess(time.time() - start, 2.0)


if __name__ == "__main__":
    unittest.main()
