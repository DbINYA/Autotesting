import time
from selenium import webdriver
from selenium.webdriver.common.by import By


URL = "https://lambdatest.github.io/sample-todo-app/"
first_test = "5 of 5 remaining"
swap_el = "First Item"

driver = webdriver.Edge(options=webdriver.EdgeOptions())
driver.get(URL)

txt = driver.find_element(By.CLASS_NAME, "ng-binding").text
# 1 test
assert txt == first_test, "1st test is failed"


elements = list(map(lambda x: x.text, \
                    driver.find_elements(By.CLASS_NAME, "done-false")))

for i in range(len(elements)):
    if elements[i] == swap_el:
        position = i + 1
        try:
            driver.find_element(By.NAME, f"li{position}").click()
            swap_el = elements[position]
        except:
            pass
            time.sleep(1)
            driver.find_element(By.ID, \
                                "sampletodotext").send_keys("New element")
            time.sleep(1)
            driver.find_element(By.CLASS_NAME, "btn-primary").click()
            time.sleep(1)
            driver.find_element(By.NAME, f"li{position + 1}").click()
    time.sleep(1)
