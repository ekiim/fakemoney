En esta pequeña guia, les voy a comentar como instalar Pipenv en Windows de 64 bits.
Antes de comenzar, estos son los requisitos inciales para ejecutar esta mini guia:
 -PC con una distribucion de Windows Oficial (Windows 10).
 -El archivo ejecutable de Python 3.8 o superior, por aca les dejo el link:
  (https://www.python.org/downloads/release/python-391/)
 -Se trabajara con una terminal PowerShell de Windows (Admin).

A continuacion, habra el link de Python para descargar el instalador de Python, 
de preferencia descargue el archivo ejecutable para 64 bits. 

Una vez echo esto, ejecute el instalador de Python, y le abrira la ventana de
instalacion de Python.
 
**NOTA_IMPORTANTE**
{Al momento de que se habra la ventana del wizard de instalacion, en la esquina
  inferior izquierda, habra un casilla que dice asi: "Desea agregar python al PATH
  automaticamente?" Tiene que seleccionar esa casilla, de lo contrario, tendremos 
  problemas para instalar  Pipenv}

Solo es cuestion de unos minutos en lo que se lleva a cabo la instalacion. Una vez
instalado podemos verificar que version de Python instalamos con el siguiente
comando: 
 py --version

Ahora instalaremos Pipenv por medio de "pip". Pip en python no es mas que un administrador
de paquetes. En este punto no hay que preocuparse, si descargo Python desde el link proporcionado
pip ya esta instalado por default.

Actualizaremos la version actual de pip con el siguiente conmando: 
 
 py -m pip install -U pip

Una vez actualizado pip, abrimos una terminal PowerShell de Windows (Tecla Windows + R, despues PowerShell)
y corremos el siguiente comando:

 pip install --user pipenv

Y automaticamente la instalacion de pipenv comenzara. Una vez echo esto habras
completado la instalacion de Pipenv y Python al mismo tiempo.
