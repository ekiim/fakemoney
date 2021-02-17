¡Bienvenido a `FakeMoney`!

Para iniciar desarrollo o configuración sobre este proyecto, requiere instalar 

 - `python3.8` (o superior) - [ver](https://www.python.org/downloads/release/python-391/) y [Notas para Windows](https://docs.python.org/3/using/windows.html)
 - Python `Pipenv` - `pip install pipenv`
 - `git` - [ver](https://git-scm.com/download/win)
 - `docker` - [ver](https://docs.docker.com/docker-for-windows/wsl/)
 - `make` - _usar en linux, o WSL_.


Una vez instalado Doctor puede clonar el repositorio con git, compilar la imagen de Docker, y ejecutarla.

```
git clone git@github.com:ekiim/fakemoney.git
make build
make run # Para detener use `make stop`
```

Si se va a trabajar utilizando Windows, se recomienda utilizar `WSL`.

