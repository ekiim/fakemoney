
Para iniciar a trabajar con el repositorio, hay que hacer un fork con github, clonar su repositorio y solicitar un pull request cuando terminen de realizar sus cambios.

  - ¿Cómo trabajar con **Fork**? En la parte superior derecha del repositorio principal se encuentra un botón **Fork** que hay que presionar.
  - Para continúar, asegúrese de estar autenticado en la plataforma **GitHub**.
  - Una vez creado el **Fork**, nos dirijimos a **Mis repositorios** ubicados en perfil y damos click en el repositorio.
  - Existe un botón en la parte superior derecha de color verde, hacemos click para desglozar las opciones y copiamos el link para crear el repositorio con **HTTPS**.
  - Dentro de una terminal de **git-bash** ejecutaremos la siguiente línea de comando para clonar el repositorio:
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

