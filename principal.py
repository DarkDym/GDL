import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH_DRIVER = "C://Users//Dymytry//Desktop//GDL//chromedriver.exe"

class GetDataLattes:
    def web_init():
        driver = webdriver.Chrome(executable_path=PATH_DRIVER)
        driver.get("http://buscatextual.cnpq.br/buscatextual/busca.do")

        id_textbox = "textoBusca"
        id_checkbox = "buscarDemais"
        # id_btnsearch = "botaoBuscaFiltros"

        in_textbox = driver.find_element_by_id(id_textbox)
        in_checkbox = driver.find_element_by_id(id_checkbox)
        # in_btnsearch = driver.find_element_by_id(id_btnsearch)

        in_checkbox.click()
        in_textbox.send_keys("Alleff Dymytry Pereira de Deus")
        in_textbox.send_keys(Keys.ENTER)
        # in_btnsearch.click()

        xpath_result = "/html/body/form/div/div[4]/div/div/div/div[3]/div/div[3]"

        try:
            element = WebDriverWait(driver,1000).until(EC.presence_of_element_located((By.XPATH,xpath_result)))
        finally:
            xpath_li = "/html/body/form/div/div[4]/div/div/div/div[3]/div/div[3]/ol/li"
            in_li = driver.find_element_by_xpath(xpath_li)
            # List count_li = in_li
            # print("li: "+str(len(count_li)))
            id_name = "/html/body/form/div/div[4]/div/div/div/div[3]/div/div[3]/ol/li/b/a"
            in_name = driver.find_element_by_xpath(id_name)
            in_name.click()
        
        GUID_origin = driver.current_window_handle
        print(GUID_origin)
        print("TITULLO DA PAGINA ANTES DA TROCA: "+str(driver.title))

        try:
            element = WebDriverWait(driver,1000).until(EC.presence_of_element_located((By.ID,"idbtnabrircurriculo")))
        finally:
            id_btnop_cur = "idbtnabrircurriculo"
            in_btnop_cur = driver.find_element_by_id(id_btnop_cur)
            in_btnop_cur.click()
        # time.sleep(5)
        try:
            element = WebDriverWait(driver, 1000).until(EC.number_of_windows_to_be(2))
        finally:
            GUID_all = driver.window_handles
            for guid in GUID_all:
                print("VALOR DO GUID: "+str(guid))
                if (guid != GUID_origin):
                    driver.switch_to_window(guid)
                    break
        print("TITULLO DA PAGINA DEPOIS DA TROCA: "+str(driver.title))
        
        # try:
            # element = WebDriverWait(driver,1000).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div[3]/div/div/div/div[1]/h2")))
        # finally:
        id_namep2 = "/html/body/div[1]/div[3]/div/div/div/div[1]/h2"
        in_namep2 = driver.find_element_by_xpath(id_namep2)
        print(in_namep2.text)

        driver.close()

tst = GetDataLattes
tst.web_init()