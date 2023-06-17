# Prueba técnica: Sistema de Gestión de Tareas
## Instalación, creación y ejecución de entorno virtual:
- `$ pip install virtualenv`
- `$ python -m venv venv`
- `$ venv\Script\activate`
## Instalaciones requeridas en entorno virtual:
- En archivo /backend/requirements-python.txt se encuentra una lista de las librerías utilizadas, las cuales pueden instalarse con `$ pip install -r requirements.txt`. Se utilizó el framework Flask.
## Creación del proyecto en React e instalaciones necesarias
- Es necesario tener NodeJS instalado.
- `$ npx create-react-app frontend`
- `$ npm install react-router-dom`
- `$ npm install react-hook-form`
## Ejecución del proyecto
Se pueden utilizar dos ventanas de la terminal, y se utilizan los comandos en sus rutas correspondientes (/backend y /frontend):
- `$ python app.py`
- `$ npm start`
## Base de datos
Se utilizó PostgreSQL, las queries de creación de tablas se encuentran en el archivo 'db_querys.txt'. Las credenciales pueden encontrarse en 'db_credenciales.txt'. 

Las tablas de la base de datos son las siguientes:
- Usuario (id, correo, contraseña)
- Tarea (id, titulo, descripcion, fecha_venc, estado_id, proyecto_id)
- Proyecto (id, titulo, descripcion)
- Usuario_tarea (id, usuario_id, tarea_id)

Y adicionalmente se creó la tabla LogoutToken, para almacenar los token de las sesiones activas.
- LogoutToken (id, token)

Este es el modelo entidad-relación resultante de la base de datos diseñada:

 <img src="https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/2c304d2f-c3bb-405d-b356-bc9a76a83101" height="500">

## Funcionamiento backend
Es posible probar los endpoints con plataformas API como Postman.

Para conectar con la base de datos, se utiliza la librería SQLAlchemy. Se utiliza CORS para permitir la comunicación entre el backend y el frontend.

La aplicación corre en la ruta http://localhost:8080/, por ejemplo para ver los usuarios la ruta será http://localhost:8080/api/usuarios (método GET).

Para la generación de tokens, se utilizó la libería de Python PyJWT, los cuales se guardan en la base de datos y para las sesiones desde el frontend, se guardan en el almacenamiento local.

Se trabajó además con la librería dotenv, para utilizar variables de entorno (en este caso, la llave secreta para codificar los tokens).

### Inicio aplicación
Al ejecutar la aplicación (/backend/app.py), se insertan valores base de forma automática, que son los estados de las tareas ("pendiente", "en progreso" y "completada") y también un usuario inicial administrador. Al estar los estados asociados a las tareas en tablas separadas, se consideran las id de los estados:
- 1: pendiente
- 2: en progreso
- 3: completada

Se consideraron 5 módulos en el backend acorde a los requerimientos:
- Login
- Usuarios
- Tareas
- Proyectos
- Tareas de usuarios

En las rutas que utilicen "id" o "tabla_id", reemplazar por el número de id. 

### Módulo login
- Iniciar sesión (ruta: /api/login, método POST), body con formato {""correo": "correo@ejemplo.com", "contraseña": "contraseña"}
- Cerrar sesión (ruta: /api/logout, método POST), *esta función requiere que la aplicación esté ejecutandose en React, dado a que los tokens de las sesiones se guardan en el almacenamiento local*

### Módulo usuarios
- Ver todos los usuarios (ruta: /api/usuarios, método GET)
- Ver usuario específico (ruta: /api/usuarios/id, método GET) (ejemplo: /api/usuarios/1)
- Crear nuevo usuario (ruta: /api/usuarios, método POST), body con formato {"correo": "correo@ejemplo.com", "contraseña": "contraseña"}. La contraseña se encripta con el algoritmo bcrypt, almacenandose así en la  base de datos. 
- Borrar usuario (ruta: /api/usuarios/id, método DELETE). Esta acción también elimina todas las asociaciones con tareas del usuario. 
  
### Módulo de tareas
- Ver todas las tareas (ruta: /api/tareas, método GET)
- Ver tarea específica (ruta: /api/tareas/id, método GET)
- Crear nueva tarea (ruta /api/tareas, método POST), body con formato {"titulo": "tarea de ejemplo", "descripcion": "descripcion de la tarea", "fecha_venc": "15-06-2023", "estado_id": 2, "proyecto_id": 1}
- Eliminar tarea (ruta: /api/tareas/id, método DELETE). Esta acción también elimina todas las asociaciones con usuarios de la tarea.
- Actualizar tarea (ruta: /api/tareas/id, método PUT), body con formato {"titulo": "tarea de ejemplo actualizada", "descripcion": "descripcion de la tarea actualizada", "fecha_venc": "15-06-2023", "estado_id": 3, "proyecto_id": 1}
- Marcar tarea como completada (ruta: /api/tareas/id_ok, método PUT)

### Módulo de proyectos
- Ver todos los proyectos (ruta: /api/proyectos, método GET)
- Ver proyecto específico (ruta: /api/proyectos/id, método GET)
- Crear nuevo proyecto (ruta: /api/proyectos, método POST), body con formato {"titulo": proyecto de ejemplo", "descripcion": "descripcion del proyecto"}
- Eliminar proyecto (ruta: /api/proyectos/id, método DELETE). Esta acción también elimina todas las tareas asociadas al proyecto, y sus asociaciones con usuarios.
- Actualizar proyecto (ruta: /api/proyectos/id, método PUT), body con formato {"titulo": proyecto de ejemplo actualizado", "descripcion": "descripcion del proyecto actualizado"}
- Obtener tareas del proyecto (ruta: /api/id_tareas, método GET)

### Módulo de tareas de usuarios
- Ver todas las asignaciones de tareas de los usuarios (ruta: /api/usuarios_tareas, método GET)
- Ver las tareas de un usuario específico (ruta: /api/usuarios_tareas/usuario_id)
- Ver las tareas asignadas/pendientes de un usuario específico (ruta: /api/usuarios_tareas/usuario_id_asignadas)
- Crear una asignación de tarea a un usuario (ruta: /api/usuarios_tareas, método POST), body con formato {"usuario_id":1, "tarea_id": 1}
- Eliminar asignación de tarea a un usuario (ruta: /api/usuarios_tareas/id, método DELETE)

## Funcionamiento frontend 
Se realizaron las siguientes vistas:
- Vista de Login 
- Vista de Home, rutas:
  - Gestión de usuarios y tareas (permite ver, agregar, eliminar usuarios, asignarles tareas y eliminar sus tareas).
  - Gestión de tareas (permite ver, agregar, editar, eliminar y marcar completadas las tareas).
  - Ver mis tareas (muestra en pantalla una tabla con la lista de tareas que no se han terminado del usuario que ingresó.
  - Gestión de proyectos (permite agregar, editar, eliminar y ver los detalles y tareas de cada proyecto)  

Las llamadas a la api se realizan desde /utils/api.js, comunicando así el frontend y el backend. Mientras que los módulos se encuentran en /components.

La aplicación verifica que el usuario haya iniciado sesión antes de redirigirlo a los módulos, esto se realiza revisando si existe su token de usuario en el almacenamiento local. Cuando el usuario cierra sesión, este token se elimina.

## Consideraciones adicionales
- El primer usuario en ser creado tiene rol de administrador. Este usuario no puede ser eliminado, y de eliminarse en la base de datos, se creará de nuevo al iniciar la aplicación.
- Un usuario que no tiene rol de administrador no puede eliminarse a sí mismo ni a otros usuarios. Pero sí puede asignar y eliminar tareas a otros usuarios. *Esto está controlado desde el frontend, dado a que se almacena el id del usuario que ingresó en el sistema* 

## Anexo 

### Ejemplo de funcionamiento del backend (utilizando Postman)
- Login con usuario principal

  <img src="https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/5428a312-8739-41b0-9e7d-876055459614" height="400">

- Obtener usuarios

  <img src="https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/336e27a8-4f1f-4a6a-9f8f-12ba8fe44b63" height="400">

- Ver usuario específico

  <img src="https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/8917d749-f382-4354-aa57-37c10bcd0261" height="400">

- Crear nuevo usuario

  <img src="https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/2ca1524b-5b8a-4521-b297-4471e2a4690f" height="400">

- Eliminar usuario

  <img src="https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/343ef02f-d0d4-4dbb-acc6-5468b414320f" height="400">

- Obtener proyectos

  <img src="https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/f94c8322-6ee9-4097-98de-c533ab5980a4" height="400">

- Crear nuevo proyecto

  <img src="https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/c495a01d-dc3d-4116-b1da-9bbec870f34e" height="400">

- Actualizar proyecto

  <img src="https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/a37be5ab-ecae-48c5-ab4f-c6e9f1db258b" height="400">

- Eliminar proyecto

  <img src="https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/df1b99cf-0a04-400f-9f70-48625feab7d2" height="400">

- Crear nueva tarea

  <img src="https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/06fa05e4-50a7-43d2-8e85-7aa9faa16bb3" height="400">

- Crear otra tarea más 

  <img src="https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/3ce9b14f-3c7b-406d-acaa-36aa5ed46fc3" height="400">

- Actualizar tarea

  <img src="https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/8aa0b56b-3551-49cd-8d7b-d99102d9e14f" height="400">

- Marcar tarea como completada

  <img src="https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/7edb10ad-0351-475c-b9fd-2f52ad79a32d" height="400">

- Obtener tareas

  <img src="https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/f53f3bfa-3563-42bf-8138-b0892b479d2d" height="400">

- Obtener proyectos y tareas

  <img src="https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/504e5e25-dca1-4112-8de0-1aaa53980b3f" height="400">

- Crear asignación de tarea a usuario

  <img src="https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/dad09dde-651f-4031-9494-c686a92889b6" height="400">

- Crear otra asignación de tarea a usuario

  <img src="https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/cae03caf-133f-4e46-9554-d9173e04d3ee" height="400">

- Obtener usuarios y tareas

  <img src="https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/0cefe046-845c-4847-8629-4b31ba9bbb7c" height="400">

- Obtener tareas asignadas al usuario (pendientes y en progreso)

  <img src="https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/46e47b5d-1fbc-496f-b36c-d71f163a5a8a" height="400">

- Eliminar proyecto creado

  <img src="https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/2b863271-f17c-47cf-92b8-f27b5b8eeb01" height="400">



### Capturas (frontend)

- Inicio de sesión

  <img src="https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/6e8e6226-e8ad-43c6-b491-fa750322e5a2" height="350">

- Ver proyectos

  <img src="https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/dde4de75-3205-445c-9ee6-f99f9093fa2f" height="350">
  
- Ver tareas

 <img src="https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/35b29be8-25c2-459e-a6ad-259914e78901" height="350">

- Ver tareas asignadas

  <img src="https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/012aa54f-30d0-44ab-a4a1-1be56d69c274" height="350">

- Ver tareas de usuario

  <img src="https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/732e1acb-3795-4122-be53-c1966c3a8e7d" height="350">

- Ver usuarios

  <img src="https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/7fb851d5-9612-4bb2-a1c9-a4abf589f9d4" height="350">

