=PROCEDIMIENTO PARA CREAR UN DOCUMENTO .MD =

Antes de iniciar con este procedimiento debemos saber que es un **archivo .md** .

- ¿Qué es un ** archivo .md**? Es un documento de texto simple que no contiene ningún otro elemento. En él, pueden introducirse símbolos en el texto para definir el formato de ciertas secciones. Por ejemplo, puedes poner en negrita una palabra o sección colocando dos asteriscos antes y después de esta, básicamente es un archivo de texto.

1. Primer paso es verificar que no está clonado el proyecto a partir del repositorio propio y no el del _profesor_. Para verificar esto debes ejecutar el siguiente comando dentro de la carpeta donde tienes el proyecto clonado y escribir el comando:

```
git remote -v
```
Una vez echo esto, aparecerá algo parecido a esto en la terminal:

```
origin  https://github.com/Santiix28/fakemoney.git (fetch)
origin  https://github.com/Santiix28/fakemoney.git (push)
profe   https://github.com/ekiim/fakemoney.git (fetch)
profe   https://github.com/ekiim/fakemoney.git (push)

```
Si tu link es el link de tu repositorio, o sea que tiene tu nombre está bien, pero si tiene el link del profesor que sería algo así:
```
origin https://github.com/ekiim/fakemoney.git (fetch)
```
Entonces si lo tienes clonado desde el link del profesor debes eliminarlo y clonarlo desde el tuyo siguiendo estos pasos, pero si lo tienes bien puedes saltarte al siguiente punto.

1.1 Ahora para _eliminar_ y arreglar debes ejecutar el siguiente comando estando **fuera de la carpeta del proyecto**.
```
rm -rf fakemoney/
```
Ya está eliminado el repositorio ahora te vas a tu perfil de **github**, abres el link de **fakemoney**, en el _botón_ que dice **code** haces click se abrirá una _ventanita_ , te aseguraras que el link que te arroja es el de _HTTPS_. lo copias para ejecutar el siguiente comando: 
```
git clone https://github.com/Santiix28/fakemoney.git <--- (recuerda que este link es el mio, aqui deberia de estar el tuyo)
```
**NOTA**
Recuerda **si elimaste y clonaste el repositorio , debes volver a ejecutar los siguientes comandos dentro de la carpeta del proyecto**:
```
git remote add profe https://github.com/ekiim/fakemoney.git
```

```
git pull profe main
```

2. Segundo paso ya teniendo el repositorio tuyo y no del _profesor_, ahora si se puede crear un **archivo md**.
- Debes localizar la carpeta ** fakemoney** de tu repositorio dentro de tu _equipo_, ya sea en consola de `git-bash` o desde tu _navegador_ _de_ _archivos_ .
- Dentro de esta _carpeta_ buscas la carpeta **docs** y despues la carpeta llamada **wiki**.
- Dentro de _wiki_ creas un archivo llamado con el tema que explicaras.
- Agrega el texto que quieras con el editor de texto de tu preferencia**(Notepad++, nano, vim)**.
- Guardas tus cambios y regresas a la terminal de `git-bash`.
- Verificas que este tu archivo con un comando `ls` dentro de la carpeta **wiki**.

3. Ya por último queda subirlo, con el siguiente comando:
```
git push 
```
Recuerda tener en cuenta donde está localizado tu _archivo_, necesitaras la ruta de no estar dentro de la carpeta o repositorio.
```
git add Crear-un-md.md <-- (este es el archivo que yo cree y estoy dentro de la carpeta wiki por eso no especifico ruta)
```
Posteriormente ejecutamos el siguiente comando:
```
git commit
```
Nos abrirá un editor de texto en **VIM** donde especificaremos que es lo que está haciendo este cambio y cerramos.

**NOTA**
Para cambiar de editor de texto(De VIM a NANO en git-bash) usamos el siguiente comando:
```
 git config --global core.editor "nano"
```
Volvemos a ejecutar el siguiente comando:
```
git push
```
Regresamos a _github_ a nuestro repositorio y verificamos que tengamos el siguiente mensaje:
```
"This branch is 1 commit ahead of ekiim:main"
```
- Le damos a la izquierda de este mensaje y le damos click en **"pull request"**.
- Después dentro buscamos el _botón_ de **"Create pull request"**.
- Llénanos la forma borrando las 3 líneas que están debajo de **Descripción**, una vez llenada hacemos _click_ en **"Create pull request"** y listo.