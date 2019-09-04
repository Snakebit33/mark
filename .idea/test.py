import unittest
import time
import re
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeDriverManager
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from Objects import *
from Details import *


class test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        #self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        #self.driver = webdriver.Edge(EdgeDriverManager().install())


    def testcase4(self):
        driver = self.driver
        driver.get(Details.website)
        assert "IMDb" in driver.title

        Drop = Select(driver.find_element_by_name(Details.Sort))
        Drop.select_by_value(Details.URvalue)
        driver.find_element_by_xpath(Details.Movie1).click()
        time.sleep(2)
        Rating1 = driver.find_element_by_xpath(Details.Number).text

        driver.get(Details.website)
        Drop = Select(driver.find_element_by_name(Details.Sort))
        Drop.select_by_value(Details.URvalue)
        driver.find_element_by_xpath(Details.Movie2).click()
        time.sleep(2)
        Rating2 = driver.find_element_by_xpath(Details.Number).text

        driver.get(Details.website)
        Drop = Select(driver.find_element_by_name(Details.Sort))
        Drop.select_by_value(Details.URvalue)
        driver.find_element_by_xpath(Details.Movie3).click()
        time.sleep(2)
        Rating3 = driver.find_element_by_xpath(Details.Number).text

        int_rating1 = int(Rating1.replace(',','').replace(' ',''))
        int_rating2 = int(Rating2.replace(',','').replace(' ',''))
        int_rating3 = int(Rating3.replace(',','').replace(' ',''))
        assert int_rating1 > int_rating2
        assert int_rating2 > int_rating3



    def testcase8(self):
        driver = self.driver
        driver.get(Details.website)
        assert "IMDb" in driver.title
        page=LoginPage(driver)
        page.Sighin.click()
        page.Signin2.click()
        page.username = Details.username
        page.password = Details.password
        page.login.click()
        time.sleep(3)

        page2=watchlist(driver)
        if page2.Watchlist.get_attribute("title")==Details.title:
            page2.Watchlist.click()
            time.sleep(3)
            assert page2.Watchlist.get_attribute("title")==Details.title2

        page2.Watchlist.click()
        time.sleep(3)
        assert page2.Watchlist.get_attribute("title")==Details.title

        text = page2.Movie.text
        page2.Wbutton.click()
        time.sleep(3)
        assert driver.find_element_by_link_text(text).is_displayed()

        page2.list.click()
        time.sleep(3)
        page2.Watchlist.click()
        time.sleep(3)
        assert page2.Watchlist.get_attribute("title")==Details.title2

        page2.Wbutton.click()
        time.sleep(3)
        try:
            assert not driver.find_element_by_link_text(text).is_displayed()
        except NoSuchElementException:
            pass

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()