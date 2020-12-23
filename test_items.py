import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_find_button_add_to_basket(browser):
    browser.get(link)
    time.sleep(3)
    button = browser.find_element_by_class_name("btn-add-to-basket")

    assert button, 'button not found'
