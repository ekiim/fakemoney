¡Bienvenido a `FakeMoney`!

Para iniciar desarrollo o configuración sobre este proyecto, requiere instalar 

 - `python3.8` (o superior) - [ver](https://www.python.org/downloads/release/python-391/) y [Notas para Windows](https://docs.python.org/3/using/windows.html)
 - Python `Pipenv` - `python -m pip install pipenv`
 - `git` - [ver](https://git-scm.com/download/win)

Para descargar el proyecto uno puede ejecutar la siguiente linea, y esto descargara el proyecto como repositorio de GIT en una carpeta nombrada como `fakemoney` en el directorio actual.

```sh
git clone git@github.com:ekiim/fakemoney.git
```

Para validar que su ambiente funciona correctamente uno puede ejecutar las siguientes dos lineas. 

```sh
pipenv install -d
pipenv run test
```

Esto instalara las dependencias del proyecto y ejecutara las pruebas automatizadas del proyecto.

Para iniciar desarrollo uno puede editar lo que corresponda, y finalmente ejecutar.

```sh
pipenv run lint
```
Esto le arrojara una lista de mensajes que hay que leer y realizar los cambios correspondientes. Estos cambios serán cambio de estilo en el código que se escribió.

Y repita el proceso de ejecutar `pipenv run lint` hasta que no arroje ningún mensaje de error.

Posteriormente organice sus cambios con `git`, subamos los cambios a su _fork_ (la rama que ustedes generaron al darle fork al proyecto), y abran un `pull request`, y verán como se ejecutara una serie de pruebas automatizadas que deberán pasar exitosamente para poder aceptar su contribución.

