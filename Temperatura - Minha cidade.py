from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from webdriver_manager.firefox import GeckoDriverManager  
from selenium.webdriver.firefox.service import Service  
instalador_do_sistema = Service(GeckoDriverManager().install())  
navegador = webdriver.Firefox(service=instalador_do_sistema)

navegador.get('https://www.accuweather.com') 
time.sleep(3)
navegador.find_element('xpath', '/html/body/div[2]/div[2]/div[1]/div[2]/div[2]/button[2]/p').click()
navegador.find_element('xpath', '/html/body/div/div[1]/div[3]/div/div[1]/div[1]/form/input').send_keys('Porto, Porto')
navegador.find_element('xpath', '/html/body/div/div[1]/div[3]/div/div[1]/div[1]/form/input').send_keys(Keys.ENTER)
time.sleep(2)

temperatura = navegador.find_element('xpath', "/html/body/div/div[5]/div[1]/div[1]/a[1]").text[17:22].title()
sen_termica = navegador.find_element('xpath', "/html/body/div/div[5]/div[1]/div[1]/a[1]").text[32:36].title()

print("A temperatura agora é de:" +temperatura+ ", com sensação térmica de " +sen_termica+ ".")
navegador.close()