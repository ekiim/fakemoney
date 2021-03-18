# Problemas tipicos con Git

Cuando uno trabaja con `git`, puede tener problemas.

Si tiene problemas, abra un issue del tipo ayuda, explicandolo, una vez resuleto, el problema y su solucion se documentaran, en esta pagina.

> Obra en proceso.

> (Por Accidente añadi un archivo que no quería al repositorio) 
¿Qué pasa si hemos añadido un archivo que realmente no queríamos
 añadir en el commit?

Quizás un archivo que no quieres compartir, una imagen que has guardado en la carpeta equivocada.

Si sólo lo has mandado a “stage” pero no has hecho un commit, 
simplemente hay que quitar de “stage” el archivo que queremos:

git reset /assets/img/archivo_a_eliminar.jpg
Si ya has realizado un commit, debes hacer un paso mas

git reset --soft HEAD~1
git reset /assets/img/archivo_a_eliminar.jpg
rm /assets/img/archivo_a_eliminar.jpg
git commit
Esto revertirá el commit, eliminará el archivo (en el ejemplo una imagen).


> (Por Accidente olvidé añadir un archivo al último commit)
Otro error muy común al usar git es realizar un commit 
demasiado pronto. 
Has olvidado incluir un archivo, quizás lo estabas editando
 y olvidaste guardarlo antes, o necesitas hacer 
 un pequeño cambio que tienes que incluir en el último commit.

Para eso  --amend vuelve a ser la opción que te ayude.

Añade ese archivo faltante o gurda los cambios del archivo 
que necesitas incluir y que todavía tienes en el editor 
y ejecuta estos comandos:

git add archivo_faltante.txt
git commit --amend



*Ayuda GIT
 git reflog muestra una lista de cosas que has hecho. Después permite a git hacer mágicamente un viaje en el tiempo
 hasta un punto en el pasado. 
 Hay que comentar que este es el último recurso 
 y no debería ser utilizado a la ligera. 
 Para ver esa lista ejecuta el comando:
                                        git reflog
 
 Si quieres volver a un punto del pasado de tu repositorio ejecuta 
 el siguiente comando,
 reemplazando {AQUI VA EL NUMERO} por el número al que quieras 
 que vuelva todo el repositorio, por ejemplo f2f3f4.

git reset HEAD@{f2f3f4}
 
 

*Cosas que no Debes hacer con Git

Nunca Realizar un git p$sh --f0rce. Un push force sobrescribe
toda la estructura y secuencia de commits en el repositorio central,
tirando a la basura los commits de las demás personas.

