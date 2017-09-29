import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

RDSS_BASE_URL = "https://rdss.nca.gov.tw/MND_NCA/welcome.do"
RDSS_BATCH_URL = "https://rdss.nca.gov.tw/MND_NCA/qsp/applyBatchAction.do"
USERNAME = ''
PASSWORD = ''
BATCH = ''

driver = webdriver.Firefox()


def login_rdss():
    driver.get(RDSS_BASE_URL)

    username = driver.find_element_by_id('username')
    password = driver.find_element_by_id('password')

    username.send_keys(USERNAME)
    password.send_keys(PASSWORD)

    driver.find_element_by_name('loginImg').click()


def apply_batch_action():
    driver.get(RDSS_BATCH_URL)

    select = Select(driver.find_element_by_id('adjustBatchList'))
    select_options_value = [option.get_attribute('value')
                            for option in select.options]

    if BATCH in select_options_value:
        select.select_by_value(BATCH)
        driver.find_element_by_id('apply').click()

        password = driver.find_element_by_id('password_tmp')
        password.send_keys(PASSWORD)

        driver.find_element_by_id('yes').click()

        time.sleep(5)

        driver.close()
        driver.quit()

        import sys
        sys.exit()

    print("No quota, retry...")


def main():
    login_rdss()

    while True:
        apply_batch_action()
        time.sleep(5)


if __name__ == '__main__':
    main()
