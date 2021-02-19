Para iniciar a crear un md que es basicamente un archivo de texto.

1 - Primero se debe verificar que no se tenga clonado el proyecto a partir del repositorio propio y no el del profesor. Para verificar esto debes ejecutar el siguiente comando dentro de la carpeta donde tienes el proyecto clonado

```
git remote -v
```
aparecera algo parecido a esto en la terminal 

```
origin  https://github.com/Santiix28/fakemoney.git (fetch)
origin  https://github.com/Santiix28/fakemoney.git (push)
profe   https://github.com/ekiim/fakemoney.git (fetch)
profe   https://github.com/ekiim/fakemoney.git (push)

```
Si tu link es el link de tu repositorio, o sea que tiene tu nombre esta bien, pero si tiene el link del profesor que seria algo asi 
```
origin https://github.com/ekiim/fakemoney.git (fetch)
```
Entonces si lo tienes clonado desde el link del profesor debes eliminarlo y clonarlo desde el tuyo siguiendo estos pasos, pero si lo tienes bien puedes saltarte al siguiente punto.

1.1 Ahora para eliminar y arreglar debes ejecutar el siguiente comando estando fuera de la carpeta del proyecto.
```
rm -rf fakemoney/
```
ya esta eliminado el repositorio ahora te vas a tu perfil de git hub, abres el link de fakemoney, en el boton que dice code haces click se abrira una ventanita y te aseguraras que el link que te arroja es el de HTTPS. lo copias para ejecutar el siguiente comando que seria 
```
git clone https://github.com/Santiix28/fakemoney.git <--- (recuerda que este link es el mio, aqui deberia de estar el tuyo)
```
**NOTA**
Recuerda que si elimaste y clonaste el repositorio al tuyo debes volver a ejecutar los siguientes comandos dentro de la carpeta del proyecto
```
git remote add profe https://github.com/ekiim/fakemoney.git
```

```
git pull profe main
```

2 - Segundo paso ya teniendo el repositorio tuyo y no del profesor, ahora si se puede crear un archivo md, que es muy sencillo.
  - solo debes localizar la carpeta de tu repositorio dentro de tu maquina, ya sea en consola de git-bash o desde tu navegador de arrchivos.
  - Ya dentro de esta carpeta entras a la otra carpeta llamada wiki.
  - Dentro de wiki creas un archivo llamado como sea el tema que explicaras
  - Agrega el texto que quieras con el editor de texto de tu preferencia.
  - Guardas tus cambios y te regresas a la terminal de git-bash
  - Ahora verificas que este tu archivo con un ls dentro de la carpeta wiki

3 - ya por ultimo queda subirlo, que seria con el siguiente comando.
```
git push 
```
depues el comando, recuerda tener en cuenta donde esta localizado tu archivo ya que necesitaras la ruta de no estar dentro de la carpeta o repositorio.
```
git add Crear-un-md.md <-- (este es el archivo que yo cree y estoy dentro de la carpeta wiki por eso no especifico ruta)
```
despues ejecutamos el siguiente comando
```
git commit
```
nos abirira un editor de texto donde especificaremos que es lo que esta haciendo este cambio, guardamos ya especificando y cerramos.

volvemos a ejecutar el siguiente comando
```
git push
```
ahora regresamos a github a nuestro reprositorio y verificamos que que tengamos el siguiente mensaje 
"This branch is 1 commit ahead of ekiim:main"
le damos a la izquierda de este mensaje y le damos click en "pull request"
y despues dentro buscamos el boton de "Create pull request"
y llenanos la forma borrando las 3 lineas que estan debajo de Descripcion, y una vez llenada hacemos click en "Create pull request"
y listo.