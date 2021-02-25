 
> Este documento es una obra en proceso.
> Correcciones son bienvenidas


Este proyecto es un banco para dinero falso, en el cual registraremos
usuarios, y cada usuario tendrá acceso a al menos una cuenta bancaria,
estas cuentas bancarias tendrán dos tipos _personal_ y de _negocio_.

El almacenamiento de registros consultables y archivos estáticos, se llevara
por medio del modulo de Python `server.storage` (dicho archivo esta bajo
construcción), el modulo debe realizar el manejo de archivos separador por
_colecciones_, donde cada colección es un subdirectorio partiendo del 
directorio raíz para el almacenamiento (Dicho directorio raíz para el 
almacenamiento se encuentra definido por medio de una variable de ambiente
nombrada `STORAGE_DIR`.

> **Ejemplo:**
> 
> Si `STORAGE_DIR` contiene el valor `/tmp/fakemoney/storage`, y se desea
> acceder a un archivo nombrado `imagen_a.jpg`, perteneciente a la 
> colección `account_pictures`, entonces el archivo que deseamos se
> encuentra en `/tmp/fakemoney/storage/account_pictures/imagen_a.jpg`.


> **Nota:** Las variables de ambiente se definen de manera local utilizando
> un archivo `.env`, dicho archivo debe ser definido apartar de `example.env`,
> copiándolo, y editando los valores acorde el ambiente que desee configurar.

Tomando como punto de partida el almacenamiento de colecciones, definimos
las siguientes colecciones:

 - `users`
 - `accounts`
 - `account_statements`
 - `account_pictures`
 - `transactions`

Las colecciones que sirvan el propósito de almacenar archivos de datos referentes
a usuarios, transacciones, o cuentas, deberán contener exclusivamente archivos en formato
`json`, con un nombre significativo al contenido de ellos, donde los valores de referencia
serán depredados por guion bajo (`_`), y el primer valor de referencia sera una marca de tiempo
haciendo referencia al momento de creación de los archivos, y deberán contener la extinción
del archivo `.json` en caso de ser parte de una colección que almacene archivos `json` exclusivamente

 - Usuarios: `{timestamp}-{base64_email}-{phone}.json`
 - Cuentas: `{timestamp}-{account_id}.json`
 - Estados de Cuenta: `{timestamp}-{account_id}.json`
 - Transacciones: `{timestamp}-{from_account_id}-{to_account_id}.json`
 - Imágenes de las cuentas: `{asset_md5hash}.jpg`

> Issues Relacionados con estos aspectos.
> - [Manejo de Usuarios](GH-64)
>

Para el registro y manejo de usuarios, deberemos crear y consultar archivos con la siguiente
estructura.

```json
{
    "email": "user@example.com",
    "phone": "+526649999999",
    "password_md5": "{md5_for_password}",
    "picture": {
        "url": "https://{somedomain}/route/to/picture",
        "filename": "nombre_del_archivo.jpg"
    },
    "personal_data": {
        "first": "José",
        "middle": "José",
        "lastname_1": "Sosa",
        "lastname_2": "Ortiz",
        "birthdate": "1948-02-17"
    },
    "accounts": ["account_id", "account_id"],
    "comments": [
        {"timestamp": 1613952000, "comment": "Cadena de texto en Markdown"},
        {"timestamp": 1613952100, "comment": "Cadena de texto en Markdown"},
    ],
    "admin_comments": [
        {"timestamp": 1613952000, "type": "complaint", "comment": "Cadena de texto en Markdown"},
        {"timestamp": 1613952100, "type": "support", "comment": "Cadena de texto en Markdown"},
    ]
}
```

Cada usuario, al momento de su creación se le asignara un numero de cuenta, y este debe de estar
contenido bajo el atributo de `accounts`.

La estructuras deberá ser la siguiente:

```json
{
    "created_time": "2021-02-22T00:00:00-08:00",
    "id": "UUID",
    "picture": {
        "url": "https://{somedomain}/route/to/picture",
        "filename": "nombre_del_archivo.jpg"
    },
    "owner": "users base64_email",
    "users": [
        "users base64_email",
        "users base64_email",
    ],
    "blocked": false
}
```

Parece ser simple la estructura de las cuentas, pero toda la _magia_ para llevar acabo la contabilidad de la
moneda sera por medio de consultas a el ultimo estado de cuenta conocido todas las transacciones subsecuentes
al momento de creación del ultimo estado de cuenta.

Una transacción se estructura de la siguiente manera:

```json
{
    "general": {
        "from": "account_id",
        "to": "account_id",
        "amount": 10000,
        "human_reference": "Descripcion de la transaccion",
        "id": "UUID",
        "status": "fail"
    },
    "concept": {
        "items": [ ],
        "deposit": { }
    },
    "account_from": {
        "account": "account_id",
        "user": "{authorizing_user_base64email}",
        "user_session_token": "{user_session_token}",
        "last_transaction": {
            "$ref": "transactions/{transaction_file_name}"
        },
        "last_balance": 11000,
        "new_balance": 1000
    },
    "account_to": {
        "account": "account_id",
        "user": "{authorizing_user_base64email}",
        "last_transaction": {
            "$ref": "transactions/{transaction_file_name}"
        },
        "last_balance": 10000,
        "new_balance": 20000
    }
}
```

Debido a que las transacciones cargan con una referencia a la ultima transacción del usuario, podemos fácilmente
verificar el saldo de la cuenta por una simple inspección de las referencias de las transacciones que tenemos
almacenadas en nuestro historial local. 

Supongamos que un usuario decide borrar todo el historial de transacciones de su cliente web, entonces para
hacer una validación del saldo, el usuario deberá consultar su estado de cuenta, y sin necesidad de conocer mas
que la ultima transacción en su historial puede continuar realizando pagos y recibiendo pagos debido a que 
la referencia en su siguiente pago sera a la ultima transacción realizada en su cuenta, y de esta manera, si
nuestra _cadena_ de transacciones sobre la cuenta es valida, podemos asegurar que el saldo es valido.


El estado de cuenta es la entidad mas simple sin embargo requiere ser calculada a partir de las transacciones
conocidas de la cuenta en cuestión, su estructura es de la siguiente forma:

```json
{
    "account_id": "{account_id}",
    "created_time": "2021-02-22T00:00:00-08:00",
    "created_timestamp": 1613952000,
    "balance": 111000,
    "transactions": [
        {"$ref": "transactions/{transaction_file}"},
        {"$ref": "transactions/{transaction_file}"},
        {"$ref": "transactions/{transaction_file}"},
    ]
}
```

### Mecanismo de consultas de un estados de cuenta

Al momento de creación de un usuario se le asigna una cuenta inicial del tipo personal.

Al momento de creación de una cuenta se le asigna un estado de cuenta inicial con un balance inicial
y sin transacciones en la lista de transacciones.

Debido a la estructura de las transacciones por el hecho de que las transacciones cargan con una referencia a 
la transacción anterior realizada en la cuenta, un cliente del banco (Aplicación que consume el `API` del banco), 
no requiere forzosamente refrescar su estado de cuenta por medio de una consulta al servidor, si
su cadena de transacciones es valida.

Para el calculo de un estado de cuenta, necesitamos

 - Conocer las transacciones efectuadas en la cuenta, posteriores a la fecha de creación del ultimo estado de cuenta conocido (o las transacciones existentes no incluidas en la lista de transacciones), las cuales denominamos _nuevas_.
 - Verificar que la cadena de transacciones _nuevas_ sea valida y compatible con la cadena previamente existente.
 - Realizar un calculo sobre las transacciones _nuevas_ para así crear un nuevo registro de estado de cuenta.


Si el usuario realiza una consulta de su estado de cuenta deberá realizar una petición al `API`, y esté deberá
regresar el ultimo estado de cuenta en caso de no existir nuevas transacciones apartar del momento de creación
del estado de cuenta y en caso de existir nuevas transacciones deberá crear el nuevo estado de cuenta, almacenarlo
y responder al usuario con dicho estado de cuenta.


## Interacciones del usuario con el sistema

> La especificación de rutas `HTTP` esta pendiente, sera publicada en formato [_swagger_](https://editor.swagger.io/?_ga=2.171413088.198606485.1613980871-657578984.1613980871)


![Registro de usuarios](https://github.com/ekiim/fakemoney/blob/main/docs/wiki/assets/sequence-user-signup.svg)

---

![Autenticación de Usuarios](https://github.com/ekiim/fakemoney/blob/main/docs/wiki/assets/sequence-user-login.svg)

---

![Consulta de estado de cuenta](https://github.com/ekiim/fakemoney/blob/main/docs/wiki/assets/sequence-account-statement.svg)

---

![Transacción Usuario a Usuario](https://github.com/ekiim/fakemoney/blob/main/docs/wiki/assets/sequence-transaction.svg)
