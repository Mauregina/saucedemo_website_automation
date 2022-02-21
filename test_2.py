from pages.ProductPage import ProductPage

class Test2:

    def test_execute_login(self, login_page_open):
        login_page_open.execute_login()
        product_page = ProductPage(login_page_open.driver)
        assert product_page.is_product_page(), 'Página de produtos não encontrada!'

