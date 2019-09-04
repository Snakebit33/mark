from page_objects import PageObject, PageElement
from Details import *


class LoginPage(PageObject):
    username = PageElement(id_= Details.Lusername)
    password = PageElement(id_= Details.Lpassword)
    login = PageElement(id_= Details.Login)
    Sighin = PageElement(link_text= Details.Sighin)
    Signin2 = PageElement(link_text= Details.Sighin2)

class watchlist(PageObject):
    Watchlist = PageElement(xpath= Details.Watchlist)
    Movie = PageElement(xpath= Details.Movie)
    Wbutton = PageElement(id_ = Details.Wbutton)
    list = PageElement(link_text= Details.list)

    def Sort(a):
        driver.get(Details.website)
        assert "IMDb" in driver.title
        Drop = Select(driver.find_element_by_name(Details.Sort))
        Drop.select_by_value(Details.URvalue)
        driver.find_element_by_xpath(a).click()