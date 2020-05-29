from selenium.common.exceptions import NoSuchElementException

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_find_add_to_basket(browser):
    browser.get(link)
    try:
        button = browser.find_element_by_css_selector('.btn-lg.btn-primary.btn-add-to-basket')
    except (NoSuchElementException):
        assert False, 'button is missing'
