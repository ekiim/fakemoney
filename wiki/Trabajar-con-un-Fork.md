
Para iniciar a trabajar con el repositorio, hay que hacer un fork con github, clonar su repositorio y solicitar un pull request cuando terminen de realizar sus cambios.


  - Para crear un fork hay que presionar el boton que dice **Fork** ubicado en la parte superior derecha del repositorio principal.
  - Hay que asegurarse de estar autenticado en la plataforma de **github**.
  - Una vez creado el fork ,hay que ubicar el boton que dice **clone** y obtener el link para crear el repositorio con **https**.
  - Para clonar un repositorio hay que abrir una terminal de **git-bash** , ejecutar la siguiente linea:
  - `git clone {URL}`

**NOTA**
Es importante estar dentro del repositorio fakemoney para correr los comandos o rutas!

Para mantener sus _branch_ al día con el proyecto principal es útil ejecutar las siguientes líneas en la terminal de git. 

Esta línea les permitirá observar los cambios que se realicen en el branch principal.
```
git remote add profe https://github.com/ekiim/fakemoney.git
```

Después deberán hacer para obtener los cambios mas recientes en la rama principal. 

```
git pull profe main
```

---

Cuando tengas listos los cambios, y desees actualizar tu sitio de github, realizar un `push`

```
git push
```

Asi sus cambios se veran reflejados en su pagina de github, `https://github.com/{nombre de usuario}/fakemoney`



