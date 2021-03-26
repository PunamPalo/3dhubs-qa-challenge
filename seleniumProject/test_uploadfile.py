import time

from selenium import webdriver
import pytest

@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Chrome(executable_path='drivers/chromedriver 2')
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield
    driver.close()
    driver.quit()

def test_uploadfile(test_setup):
    driver.get("https://www.3dhubs.com/manufacture/")
    driver.find_element_by_xpath('//*[@id="file-btn"]').send_keys('/Users/punampalo/PycharmProjects/pythonProject/datas/1-1x-3d_printing_sample_part-original.step')
    driver.find_element_by_id('email').send_keys('punampalo2@gmail.com')
    driver.find_element_by_xpath('//*[@id="emailWallForm"]/div[1]/mat-dialog-actions/button').click()
    time.sleep(5)

    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/mat-dialog-container/h3d-new-feature-walkthrough-dialog/div/button/i')


