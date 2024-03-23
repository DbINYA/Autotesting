import time
from selenium import webdriver
from selenium.webdriver.common.by import By


URL = "https://lambdatest.github.io/sample-todo-app/"
first_test = "5 of 5 remaining"
swap_el = "First Item"
new_el = "New element"

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
            last_el = list(map(lambda x: x.text, \
                    driver.find_elements(By.CLASS_NAME, "done-true")))[-1]
            assert swap_el == last_el, "Not marked"
            print(last_el)
            swap_el = elements[position]
        except:
            time.sleep(1)
            driver.find_element(By.ID, \
                                "sampletodotext").send_keys(new_el)
            time.sleep(1)
            driver.find_element(By.CLASS_NAME, "btn-primary").click()
            time.sleep(1)
            driver.find_element(By.NAME, f"li{position + 1}").click()
    time.sleep(1)

    
last_el = list(map(lambda x: x.text, \
                    driver.find_elements(By.CLASS_NAME, "done-true")))[-1]
assert last_el == new_el, "Not marked"
