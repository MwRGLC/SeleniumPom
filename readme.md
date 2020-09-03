# SeleniumPom

Editar descripcion

## Installation

Dame los pasos necesarios para poder correrlo en mi maquina desde cero

## Stuff necesario

Yo uso PyCharm IDE porque es el que mas facil se me hizo a la hora de crear la estructura.

webdrivers chrome y firefox que es lo que esta codeado, solo tenes que cambiarle el exec_path.

Required Packages: 

#los instalas desde settings -> interpreter -> add/+ y tiene un buscador de packages/plugins

selenium
pytest
pytest-html
pytest-xdist
openpyxl
allure-pytest

#La estructura es todo lo que tiene parentesis y la creas desde el project name
#Despues podes pegar los archivos directamente con ctrl+v en los lugares que muestra abajo
#Si hay una forma de pasarte todo el project todavia no lo se hacer XD

	pageObjects(package)
		LoginPage.py
	testCases(package)
		conftest.py
		test_login.py
		test_login_ddt.py
	utilities(package)
		customLogger.py
		readProperties.py
		XLUtils.py
	TestData(directory)
		LoginData.xlsx
	Configurations(directory)
		config.ini
	Logs(directory)
	Screenshots(directory)
	Reports(directory)

## terminal commands

#test_login

pytest -s -v --html=Reports\report.html testCases/test_login.py --browser chrome

#(testCases/test_login.py es el Path from content root)

#test_login_ddt

pytest -s -v --html=Reports\report.html testCases/test_login_ddt.py --browser chrome

#(testCases/test_login_ddt.py es el Path from content root)
