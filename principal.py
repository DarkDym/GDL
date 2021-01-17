#Biblioteca para manipulação dos arquivos .csv com as informações dos professores
import csv
#Biblioteca para manipulação de pastas e objetos do sistema
import glob
#Biblioteca para manipulação e utilização do tempo do sistema
import time
#Biblioteca para manipulação das funções do sistema operacional
import os
import sys
#Biblioteca para manipulação dos arquivos salvos
import json

#Biblioteca de manipulação das páginas web
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#Exceções da biblioteca Selenium
from selenium.common.exceptions import TimeoutException

#Caminhos para as as pastas que contêm os arquivos necessários para o funcionamento do sistema
PATH_DRIVER = "C://Users//Dymytry//Desktop//GDL//chromedriver.exe"
PATH_CSV = "C://Users//Dymytry//Desktop//GDL//PROFESSORES//"
PATH_SAVE = "C://Users//Dymytry//Desktop//GDL//Lattes"

class GetDataLattes:

    #Função que abre e manipula as informações dos arquivos .csv dos professores
    # def get_datacsv():
    #     for arq in glob.glob(os.path.join(PATH_CSV,"*.csv")):
    #         with open(arq,encoding="utf8") as open_csv:
    #             read_csv = csv.reader(open_csv,delimiter=",")
    #             for row in read_csv:

    #Função que abre a página web com a plataforma Lattes e busca as informações necessárias
    def web_init():
        flag_op = 0
        driver = webdriver.Chrome(executable_path=PATH_DRIVER)
        driver.get("http://buscatextual.cnpq.br/buscatextual/busca.do")

        id_textbox = "textoBusca"
        id_checkbox = "buscarDemais"
        # id_btnsearch = "botaoBuscaFiltros"

        in_textbox = driver.find_element_by_id(id_textbox)
        in_checkbox = driver.find_element_by_id(id_checkbox)
        # in_btnsearch = driver.find_element_by_id(id_btnsearch)

        in_checkbox.click()
        #BUSCAR NO CSV E INSERIR NO SITE MAIS DE UMA VEZ
        for arq in glob.glob(os.path.join(PATH_CSV,"*.csv")):
            arq_aux = os.path.basename(arq)
            arq_aux = arq_aux.replace(".csv","")
            with open(arq,encoding="utf8") as open_csv:
                read_csv = csv.reader(open_csv,delimiter=",")
                for row in read_csv:
                    if flag_op != 1:
                        flag_op += 1
                    else:

                        in_textbox.send_keys(row[0])
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
                        id_pp = "/html/body/div[1]/div[3]/div/div/div/div[10]/a/h1"
                        in_pp = driver.find_element_by_xpath(id_pp)

                        # id_tit = "/html/body/div[1]/div[3]/div/div/div/div/a"
                        id_tit = "title-wrapper"
                        in_tit = driver.find_elements_by_class_name(id_tit)
                        
                        indice = 2
                        sv_pp = 0
                        sv_pe = 0
                        sv_p = []
                        for teste in in_tit:
                            if 'Projetos de pesquisa' in teste.text:
                                sv_pp = 1
                                sv_p.append(indice)
                                print("VALOR DO INDICE GUARDADO SV_PP--> "+str(indice))
                                # print("Valor do H1 no div -> "+str(teste.text) + " no indice de valor --> "+str(indice))
                            elif 'Projetos de extensão' in teste.text:
                                sv_pe = 1
                                sv_p.append(indice)
                                print("VALOR DO INDICE GUARDADO SV_PE--> "+str(indice))
                                # print("Valor do H1 no div -> "+str(teste.text) + " no indice de valor --> "+str(indice))
                            indice+=1
                        # print(eero)
                        try:
                            element = WebDriverWait(driver,500).until(EC.presence_of_element_located((By.XPATH,id_pp)))
                        except TimeoutException:
                            print(ERRO)
                        else:
                            if sv_pp != 0:
                                id_div_pp = "/html/body/div[1]/div[3]/div/div/div/div["+str(sv_p[0])+"]/div"
                                in_div_pp = driver.find_elements_by_xpath(id_div_pp)
                                print("VAMOS VER O QUE VEIO NESSA BOSTA")
                                print(len(in_div_pp))
                                aux_teste = 0
                                for treco in in_div_pp:
                                    teste = treco.text
                                    aux_teste = teste.split('\n')
                                    print(aux_teste)

                                limpa = []
                                    # flag_sit = 0
                                for x in range(0,len(aux_teste)):
                                    if aux_teste[x] == '':
                                        print("APAGUEI ISSO --> " +str(aux_teste[x]))
                                    else:
                                        if ' - Atual' in aux_teste[x]:
                                            limpa.append(aux_teste[x])
                                            limpa.append(aux_teste[x+1])
                                                # flag_sit == 0
                                        elif 'Projeto certificado' in aux_teste[x]:
                                            print("AQUI ESSA CONDIÇÃO NÃO PODE OCORRER")
                                        elif 'Descrição: ' in aux_teste[x]:
                                            limpa.append(aux_teste[x])
                                        elif 'Situação: ' in aux_teste[x]:
                                                # if flag_sit == 0:                                            
                                            limpa.append(aux_teste[x])
                                                    # flag_sit = 1
                                        elif '201' in aux_teste[x]:
                                            limpa.append(aux_teste[x])
                                            limpa.append(aux_teste[x+1])
                                                # flag_sit == 0
                                        elif '202' in aux_teste[x]:
                                            limpa.append(aux_teste[x])
                                            limpa.append(aux_teste[x+1])
                                                # flag_sit == 0
                                        elif '200' in aux_teste[x]:
                                            limpa.append(aux_teste[x])
                                            limpa.append(aux_teste[x+1])
                                                # flag_sit == 0
                                        elif '199' in aux_teste[x]:
                                            limpa.append(aux_teste[x])
                                            limpa.append(aux_teste[x+1])
                                                # flag_sit == 0
                                        else:
                                            print("PERDI ISSO AQUI --> "+str(aux_teste[x]))
                                print(limpa)
                                print(len(limpa))

                            if sv_pe != 0:
                                if sv_pp == 0:
                                    id_titulo_pe = "/html/body/div[1]/div[3]/div/div/div/div["+str(sv_p[0])+"]/a/h1"
                                else:
                                    id_titulo_pe = "/html/body/div[1]/div[3]/div/div/div/div["+str(sv_p[1])+"]/a/h1"
                                in_titulo_pe = driver.find_element_by_xpath(id_titulo_pe)
                                flag_pe = 0
                                if in_titulo_pe.text == "Projetos de extensão":
                                    flag_pe = 1
                                    if sv_pp == 0:
                                        id_div_pe = "/html/body/div[1]/div[3]/div/div/div/div["+str(sv_p[0])+"]/div"
                                    else:
                                        id_div_pe = "/html/body/div[1]/div[3]/div/div/div/div["+str(sv_p[1])+"]/div"
                                    in_div_pe = driver.find_elements_by_xpath(id_div_pe)
                                    print("VAMOS VER O QUE VEIO NESSA BOSTA")
                                    print(len(in_div_pe))
                                    aux_teste2 = 0
                                    for treco in in_div_pe:
                                        teste = treco.text
                                        aux_teste2 = teste.split('\n')
                                        print(aux_teste2)
                                    
                                    limpa2 = []
                                    for x in range(0,len(aux_teste2)):
                                        if aux_teste2[x] == '':
                                            print("APAGUEI ISSO --> " +str(aux_teste2[x]))
                                        else:
                                            if ' - Atual' in aux_teste2[x]:
                                                limpa2.append(aux_teste2[x])
                                                limpa2.append(aux_teste2[x+1])
                                            elif 'Projeto certificado' in aux_teste2[x]:
                                                print("AQUI ESSA CONDIÇÃO NÃO PODE OCORRER")    
                                            elif 'Descrição: ' in aux_teste2[x]:
                                                limpa2.append(aux_teste2[x])
                                            elif 'Situação: ' in aux_teste2[x]:
                                                limpa2.append(aux_teste2[x])
                                            elif '201' in aux_teste2[x]:
                                                if len(aux_teste2[x]) <= 12: 
                                                    limpa2.append(aux_teste2[x])
                                                    print("INDICE -> "+str(x))
                                                    print("Valor de X-> "+str(aux_teste2[x]))
                                                    print("Valor de X+1-> "+str(aux_teste2[x+1]))
                                                    limpa2.append(aux_teste2[x+1])
                                            elif '202' in aux_teste2[x]:
                                                limpa2.append(aux_teste2[x])
                                                limpa2.append(aux_teste2[x+1])
                                                
                                            elif '200' in aux_teste2[x]:
                                                limpa2.append(aux_teste2[x])
                                                limpa2.append(aux_teste2[x+1])
                                                
                                            elif '199' in aux_teste2[x]:
                                                limpa2.append(aux_teste2[x])
                                                limpa2.append(aux_teste2[x+1])
                                                
                                            else:
                                                print("PERDI ISSO AQUI --> "+str(aux_teste2[x]))
                                    print(limpa2)
                                    print(len(limpa2))
                            
                            info_json = []
                            info_json2 = []
                            name_json = []
                            # name_json.append({"NOME":row[0]})
                            # if sv_pp != 0:
                            for x in range(0,len(limpa)):
                                if 'Situação:' in limpa[x]:
                                    if len(limpa[x]) < 50:
                                        if 'Descrição:' in limpa[x-1]:
                                            print("OK")
                                        else:
                                            limpa.insert(x,"Descrição:")
                                    # if x+1 < len(limpa):
                                    #     print(x)
                                    #     if 'Situação:' in limpa[x+1]:
                                    #         print(limpa[x])
                                    #         print(limpa[x+1])
                                    #         limpa.pop(x+1)
                                    
                                    
                            print("TA AQUI ESSA COISA: "+str(limpa))
                            # if sv_pe != 0:
                            if flag_pe == 1:
                                last_len = len(limpa2)
                                for x in range(0,len(limpa2)):
                                    if 'Situação:' in limpa2[x]:
                                        if len(limpa2[x]) < 50:
                                            if 'Descrição:' in limpa2[x-1]:
                                                print("OK INDICE DE X --> "+str(x))
                                            else:
                                                print("INDICE DE X --> "+str(x))
                                                print("TAMANHO DO LIMPA ANTES --> "+str(len(limpa2)))
                                                limpa2.insert(x,"Descrição:")    
                                                print("TAMANHO DO LIMPA DEPOIS --> "+str(len(limpa2)))
                                                print("VALOR NO MOMENTO DA ADIÇAO -->"+str(limpa2[x]))
                                if last_len < len(limpa2):
                                    for x in range(0,len(limpa2)):
                                        if 'Situação:' in limpa2[x]:
                                            if len(limpa2[x]) < 50:
                                                if 'Descrição:' in limpa2[x-1]:
                                                    print("OK INDICE DE X --> "+str(x))
                                                else:
                                                    print("INDICE DE X --> "+str(x))
                                                    print("TAMANHO DO LIMPA ANTES --> "+str(len(limpa2)))
                                                    limpa2.insert(x,"Descrição:")    
                                                    print("TAMANHO DO LIMPA DEPOIS --> "+str(len(limpa2)))
                                                    print("VALOR NO MOMENTO DA ADIÇAO -->"+str(limpa2[x]))

                            with open(PATH_SAVE+"/"+str(arq_aux)+"/"+row[0]+".json",'w',encoding='utf8') as save_csv:
                                # if sv_pp != 0:
                                for x in range(0,len(limpa),4):
                                    #print(x)/html/body/div[1]/div[3]/div/div/div/div[10]
                                    if 'Descrição:' in limpa[x+2]:
                                        print("VALOR DO TITULO: " + str(limpa[x+1]))
                                        info_json.append({"ANO":str(limpa[x]),"TITULO":str(limpa[x+1]),"SITUACAO":str(limpa[x+3])})
                                    else:
                                        info_json.append({"ANO":str(limpa[x]),"TITULO":str(limpa[x+1]),"SITUACAO":str(limpa[x+2])})
                                if flag_pe == 1:
                                    print("TA AQUI ESSA PORCARIA --> "+str(limpa2))
                                    for x in range(0,len(limpa2),4):
                                        print(x)
                                        if 'Descrição:' in limpa2[x+2]:
                                            print("VALOR DO TITULO: " + str(limpa2[x+1]))
                                            info_json2.append({"ANO":str(limpa2[x]),"TITULO":str(limpa2[x+1]),"SITUACAO":str(limpa2[x+3])})
                                        else:
                                            info_json2.append({"ANO":str(limpa2[x]),"TITULO":str(limpa2[x+1]),"SITUACAO":str(limpa2[x+2])})
                                    name_json.append({"NOME":row[0],"PROJPESQ":info_json,"PROJEXT":info_json2})
                                else:
                                    name_json.append({"NOME":row[0],"PROJPESQ":info_json})
                                json.dump(name_json,save_csv,indent=4,ensure_ascii=False)
                            save_csv.close()

                            #Fechar nova guia
                            driver.close()
                            flag_pe = 0
                            driver.switch_to_window(GUID_origin)
                            id_close = "/html/body/form/div/div[1]/div/div/div/div[2]/div/a[3]"
                            in_close = driver.find_element_by_xpath(id_close)
                            in_close.click()
                            id_bt_newsearch = "/html/body/form/div/div[4]/div/div/div/div[3]/div/div[5]/a"
                            in_bt_newsearch = driver.find_element_by_xpath(id_bt_newsearch)
                            in_bt_newsearch.click()
                            id_textbox = "textoBusca"
                            id_checkbox = "buscarDemais"                            
                            in_textbox = driver.find_element_by_id(id_textbox)
                            in_checkbox = driver.find_element_by_id(id_checkbox)
                            in_checkbox.click()

                                # if "20" in aux_teste:
                                #     print("ANO: "+str(treco.text))
                                # elif "19" in treco.text:          
                                #     print("ANO: "+str(treco.text))
                                # elif "Descrição:" in treco.text:
                                #     print(treco.text)
                                # elif "Situação:" in treco.text:
                                #     print(treco.text)
                                # else:
                                #     print("ERA PRA TER PARADO")                       
                                #     # print(treco.text)    
            flag_op = 0                

        driver.close()

tst = GetDataLattes
tst.web_init()