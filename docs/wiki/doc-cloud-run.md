> El siguiente documento Markdown presenta información sobre Google Cloud Run y como fue implementado en el proyecto final.
> Documento en proceso, correcciones ortográficas son bien recibidas.

¿Qué es `Google Cloud Run`?
Cloud Run es una plataforma de procesamiento administrada que te permite ejecutar contenedores sin estado que se pueden invocar a través de solicitudes web o eventos de Pub/Sub. 
Cloud Run es una plataforma sin servidores, lo que significa que quita la complejidad de la administración de infraestructura, de modo que te puedas enfocar en lo que más importa: compilar aplicaciones excelentes. Se basa en Knative.

Se puede encontrar más información en el siguiente enlace: [Documentación de Google Cloud Run](https://cloud.google.com/run/docs?hl=es-419)

Para llegar a configurar los servicios de Google Cloud Run, primero se debe de llevar a cabo la suscripcion de envio por parte de Pub/Sub.
Esto llegara a cumplir los objetivos de escribir, complitar datos y tambien tener servicios mediante notificaciones de mensaje

En nuestro caso en el proyecto de Fakemoney, se llegara a utilizar los beneficios de Cloud build para que llegue a compilar de manera muy eficiente y rapida los lenguajes que se llegue a programar
Ademas de obtener control sobre el flujo de trabajo que se llegue a implementar y asi tener una mayor facilidad al compilamiento, tener una mayor flexibilidad a las extensiones que deseamos agregar y tener tambien la seguridad y cumplimiento.
Para llegar a bloquear todo tipo de amenazas y estar reforzando las vulnerabilidades que se puedan encontrar.

`Guía de inicio rápido:` Implementa un contenedor de muestra ya compilado
A continuación se muestra cómo implementar un contenedor de muestra que ya se subió al repositorio de Container Registry en Cloud Run.

Antes de comenzar

1. Accede a tu cuenta de Google Cloud. Si eres nuevo en Google Cloud, crea una cuenta para evaluar el rendimiento de nuestros productos en situaciones reales.
2. En la página del selector de proyectos de Google Cloud Console, selecciona o crea un proyecto de Google Cloud.
3. Ir al selector de proyecto

`Implementa el contenedor de muestra:` 
Para implementar un contenedor, haz lo siguiente:

1. Ir a Cloud Run
2. Hacer clic en Crear servicio para ver el formulario Create service (Crear servicio):

En el `formulario`, debes hacer lo siguiente:

1.	Selecciona Cloud Run (fully managed) (completamente administrado) como la plataforma de desarrollo.
2.	Selecciona la región donde quieres que se ubique el servicio.
3.	Especifica el nombre que deseas asignarle al servicio.
4.	Haz clic en Siguiente para ir a la página Configurar la primera revisión del servicio.
5.	Selecciona Implementar una revisión desde una imagen de contenedor existente.
6.	Usa us-docker.pkg.dev/cloudrun/container/hello como la imagen de contenedor.
7.	Haz clic en Siguiente para ir a la página Configurar cómo se activa este servicio.
8.	Selecciona Allow unauthenticated invocations (Permitir invocaciones no autenticadas) para poder abrir el resultado en el navegador web.
9.	Haz clic en Crear para implementar la imagen en Cloud Run y espera a que termine la implementación.
10.	Haz clic en el vínculo de la URL que se muestra para ejecutar el contenedor implementado.

Felicitaciones. Acabas de implementar un contenedor en Cloud Run que responde a las solicitudes web entrantes. De forma automática, Cloud Run escala horizontalmente tu contenedor para manejar las solicitudes recibidas y, luego, reduce la escala cuando la demanda disminuye.


