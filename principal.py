import csv
from selenium import webdriver

class GetDataLattes:
    def web_init():
        driver = webdriver.Chrome(executable_path="chromedriver.exe")
        driver.get("http://buscatextual.cnpq.br/buscatextual/busca.do")
        driver.close()

tst = GetDataLattes
tst.web_init()