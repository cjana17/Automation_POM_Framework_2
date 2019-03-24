from selenium import webdriver
import requests

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("https://google.com")

elements=driver.find_elements_by_tag_name("a")
print(type(elements))
print(len(elements))
broken_link=[]
correct_link=[]

for i in elements:
    r=requests.head(i.get_attribute("href"))

    if r.status_code != 200:
        broken_link.append(i.get_attribute("href"))
    else:
        correct_link.append(i.get_attribute("href"))

print("BL",broken_link)
print("WL",correct_link)

