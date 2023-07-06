# Programa para Eliminar cuentas de correo gmail by Scr1im
#
# Realizado en python3 version 3.11
# Requiere las siguientes librerias para poder ejecutarse:
# pip install -U selenium, pip install pandas y pip install webdriver-manager
# Tener presente la actaulización del navegador Chrome
# Utiliza un CSV con la lista de los correos a eliminar
#

import pandas as pd 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.chrome.service import Service # Descomentariar en caso de error linea 57
#from webdriver_manager.chrome import ChromeDriverManager # Descomentariar en caso de error linea 57

userUc = "Account" # Ingresar el usuario
passUc = "Pass" # Ingresar la contraseña
urlAdmin = 'https://admin.google.com/' # URL admin de google
findUser = cleanUser = elementEnable = ifAccountDelete = False # Variables para habilitar condicionales
userGmail = "Admin@admin.com" # Ingresar el correo administrador de google o cuenta con permisos de eliminación
pathAccountDel = "//*[@id='yDmH0d']/div[5]/div/div[2]/div[3]/div[1]" # Eliminar cuenta en el registro del navegador
pathChrome = 'C:\chromium\chromedriver.exe' # Ruta del ejecutable webdriver en caso de descargar el web driver con linea 56 no es necesario tener el .exe
pathCSV = r"C:\Users\jssuarez\Documents\Correos\correosEliminar.csv" # Ruta del archivo CSV con lista de usuarios a eliminar
pathSup = "/html/body/div[7]/div[2]/header/div[2]/div[2]/div[2]/form/button[2]" # Path para eliminar registro de busqueda 
pathUser = "/html/body/div[7]/div[2]/header/div[2]/div[2]/div[2]/form/div/div/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div[2]/div[2]/span/b" # Condicional para usuarios
pathDelete = "/html/body/div[7]/c-wiz/div/div[1]/div/div/div[2]/div/div[2]/div/div[1]/div/div/span/c-wiz/div/div[3]/span/div/div/div[4]/div/span/span/div/div[2]"
loggoutUrl = 'https://accounts.google.com/Logout?hl=es&continue=https%3A%2F%2Fadmin.google.com%2Fac%2Fhome%3Fhl%3Des&timeStmp=1688489886&secTok=.AG5fkS_rXIAMRf8GPbHqdwArkeZJ5_OKMQ&ec=GAdA7wI&hl=es'

def elementClickFunction(elementEnable, pathClick): # Funcion para habilitar el clickeo
	while not elementEnable:
		try:
			driver.find_element("xpath",pathClick).click()
			elementEnable = True
		except WebDriverException:
			elementEnable = False
	elementEnable = False
	
def logginFunction(ifAccountDelete): # Funcion para iniciar sesíón en google
	if ifAccountDelete:
		driver.get(urlAdmin);
		WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath","//div[@jsname = 'o7vT9b']"))).click()
		WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath","//div[@jsname = 'V1ur5d']"))).click()
		driver.find_element("xpath",pathAccountDel).click()
	driver.get(urlAdmin);
	driver.find_element(By.CSS_SELECTOR, "input[type='email']").send_keys(userGmail);
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath","//*[@id='identifierNext']/div/button"))).click()
	WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "j_username"))).send_keys(userUc)
	WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "j_password"))).send_keys(passUc)
	driver.find_element("xpath","//*[contains(text(), 'Enviar')]").click()
	driver.find_element("xpath","//span[@jsname = 'V67aGc']").click()

df = pd.read_csv(pathCSV); # path CSV para eliminar cuentas
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) # Descomentariar en caso de error linea 57
driver = webdriver.Chrome(pathChrome); # Comentariar en caso de error en la linea y descomentariar lineas 56, 17 y 16
driver.implicitly_wait(10);
driver.maximize_window();
logginFunction(False)

for i in range(0, len(df), 1):
	findAccountDelete = driver.find_element("xpath","//input[@jsname = 'dSO9oc']")
	findAccountDelete.send_keys(df.values[i])
	findUser = driver.find_elements(By.CLASS_NAME, "irxKNb") # Condiciones para eliminar usuario
	cleanUser = driver.find_elements("xpath", pathUser # Condiciones para eliminar usuario
	if findUser:
		elementClickFunction(elementEnable, pathSup)
	elif cleanUser:
		if cleanUser[0].text == df.values[i]:
			driver.find_element(By.CLASS_NAME, "x6llVc").click()
			elementClickFunction(elementEnable, pathDelete)
			WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath","//div[@jsname = 'wIRS7d']"))).click()
			WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath","//div[@jsname = 'Ipsvze']"))).click()
			WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath","//div[@jsname = 'GXeE0e']"))).click()
			WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath","//div[@jsname = 'ZWJ7Md']"))).click()
			WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath","//div[@jsname = 'oZO05']"))).click()
			elementClickFunction(elementEnable, "//*[contains(text(), 'Aceptar')]")
			if (driver.current_url != "https://admin.google.com/ac/users/"): # En caso de no eliminar cuenta realiza una segunda verificación
				elementClickFunction(elementEnable, "//*[contains(text(), 'Aceptar')]")
			print(str(i)+" - "+df.values[i])
		if driver.find_elements(By.XPATH, "//button[@class = 'gb_Le gb_Ne']"): # WARNING Tener presente que el path del botton para borrar la busqueda cambia
			elementClickFunction(elementEnable, pathSup)
		if i % 200 == 0 and i != 0: # Cada 200 cuentas eliminadas vuelve a iniciar sesion para evitar timeout de google
			driver.get(loggoutUrl);
			logginFunction(True)
	else:
		elementClickFunction(elementEnable, pathSup)
driver.close()
exit()
