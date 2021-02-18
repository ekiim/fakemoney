
Para iniciar a trabajar con el repositorio, hay que hacer un fork con github, clonar su repositorio y solicitar un pull request cuando terminen de realizar sus cambios.

  - Para crear un fork hay que presionar el boton que dice **Fork** ubicado en la parte superior derecha del repositorio principal.
  - Hay que asegurarse de estar autenticado en la plataforma de **github**.
  - Una vez creado el fork ,hay que ubicar el boton que dice **clone** y obtener el link para crear el repositorio con **https**.
  - Para clonar un repositorio hay que abrir una terminal de **git-bash** , ejecutar la siguiente linea:
  - `git clone {URL}`

**NOTA**:
!Es importante estar dentro del repositorio fakemoney para correr los comandos o rutas!

Para mantener sus _branch_ al día con el proyecto principal es útil ejecutar las siguientes líneas en la terminal de git. 

Esta línea les permitirá observar los cambios que se realicen en el branch principal.
```
git remote add profe https://github.com/ekiim/fakemoney.git
```

Después lo que deberán hacer para obtener los cambios mas recientes en la rama principal.

```
git pull profe main
```

---

Cuando tengas listos los cambios, y desees actualizar tu sitio de github, realizar un `push`

```
git push
```

Asi sus cambios se veran reflejados en su pagina de github, `https://github.com/{nombre de usuario}/fakemoney`


### Cambiar de editor de texto a NANO.

Nano es un editor de texto visual para la terminal.

Si deseas cambiar de editor de texto para los mensajes de `commit`, y utilizar NANO como editor de texto principal (para git).

Uno puede ejecutar la siguiente linea.

```
git config --global core.editor "nano"
```

### Evitar conflictos contra la rama principal.

Si presento confictos con la rama principal una manera de resolverlos es hacer un `git rebase`.

Para configurar que los `git pull` por default se comporten como un `rebase`, hay que ejecutar la siguiente linea.

```
git config --global pull.rebase true
```

De aqui en adelante uno puede ejecutar 

```
git pull profe main
```

Para traer a su rama actual los cambios que se presentan en la rama principal `ekiim:main`.

Cuando se tenga un conflicto entrarán en modo `rebase`, donde tendrán que editar los archivos para conciliar los cambios, y borraran lo no deseado.

Una vez concluida la fase de conciliación de cambios ejecutamos `git add` para informarle a `git` de esto, y ejecutamos un `git rebase --continue`.

