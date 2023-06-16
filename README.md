# Prueba técnica de Backend
## Instalación, creación y ejecución de entorno virtual:
- `$ pip install virtualenv`
- `$python -m venv venv`
- `$venv\Script\activate`
## Instalaciones requeridas en entorno virtual:
- En archivo /backend/requirements-python.txt se encuentra una lista de las librerías utilizadas, las cuales pueden instalarse con `$pip install -r requirements.txt`. Se utilizó el framework Flask.
## Creación del proyecto en React e instalaciones necesarias
- `$npm create-react-app frontend`
- `$ npm install react-router-dom`
- `$ npm install react-hook-form`
## Base de datos
Se utilizó PostgreSQL, las querys de creación de tablas se encuentran en el archivo 'db_querys.txt', mientras que el modelo entidad-relación se encuentra en la imagen 'modelo e-r.png'. Las credenciales pueden encontrarse en 'db_credenciales.txt'.
## Funcionamiento backend
Es posible probar los endpoints con plataformas API como Postman.
### Inicio aplicación
Al ejecutar la aplicación (/backend/app.py), se insertan valores base, que son los estados de las tareas ("pendiente", "en progreso" y "completada") y también un usuario inicial. Al estar los estados asociados a las tareas en tablas separadas, se consideran las id de los estados:
- 1: pendiente
- 2: en progreso
- 3: completada

La aplicación corre en la ruta http://localhost:8080/, por ejemplo para ver los usuarios la ruta será http://localhost:8080/api/usuarios (método GET).

Se consideraron 5 módulos en el backend acorde a los requerimientos:
- Login
- Usuarios
- Tareas
- Proyectos
- Tareas de usuarios

En las rutas que utilicen "id" o "tabla_id", reemplazar por el número de id. 
### Módulo login
- Iniciar sesión (ruta: /api/login, método POST), body con formate {""correo": "correo@ejemplo.com", "contraseña": "contraseña"}
- Cerrar sesión (ruta: /api/logout, método POST), *esta función requiere que la aplicación esté corriendo en React, para poder obtener el token de la sesión
### Módulo usuarios
- Ver todos los usuarios (ruta: /api/usuarios, método GET)
- Ver usuario específico (ruta: /api/usuarios/id, método GET) (ejemplo: /api/usuarios/1)
- Crear nuevo usuario (ruta: /api/usuarios, método POST), body con formato {"correo": "correo@ejemplo.com", "contraseña": "contraseña"}
- Borrar usuario (ruta: /api/usuarios/id, método DELETE)
  
### Módulo de tareas
- Ver todas las tareas (ruta: /api/tareas, método GET)
- Ver tarea específica (ruta: /api/tareas/id, método GET)
- Crear nueva tarea (ruta /api/tareas, método POST), body con formato {"titulo": "tarea de ejemplo", "descripcion": "descripcion de la tarea", "fecha_venc": "15-06-2023", "estado_id": 2, "proyecto_id": 1}
- Eliminar tarea (ruta: /api/tareas/id, método DELETE)
- Actualizar tarea (ruta: /api/tareas/id, método PUT), body con formato {"titulo": "tarea de ejemplo actualizada", "descripcion": "descripcion de la tarea actualizada", "fecha_venc": "15-06-2023", "estado_id": 3, "proyecto_id": 1}
- Marcar tarea como completada (ruta: /api/tareas/id_ok, método PUT)

### Módulo de proyectos
- Ver todos los proyectos (ruta: /api/proyectos, método GET)
- Ver proyecto específico (ruta: /api/proyectos/id, método GET)
- Crear nuevo proyecto (ruta: /api/proyectos, método POST), body con formato {"titulo": proyecto de ejemplo", "descripcion": "descripcion del proyecto"}
- Eliminar proyecto (ruta: /api/proyectos/id, método DELETE)
- Actualizar proyecto (ruta: /api/proyectos/id, método PUT), body con formato {"titulo": proyecto de ejemplo actualizado", "descripcion": "descripcion del proyecto actualizado"}
- Obtener tareas del proyecto (ruta: /api/id_tareas, método GET)

### Módulo de tareas de usuarios
- Ver todas las asignaciones de tareas de los usuarios (ruta: /api/usuarios_tareas, método GET)
- Ver las tareas de un usuario específico (ruta: /api/usuarios_tareas/usuario_id)
- Ver las tareas asignadas/pendientes de un usuario específico (ruta: /api/usuarios_tareas/usuario_id_asignadas)
- Crear una asignación de tarea a un usuario (ruta: /api/usuarios_tareas, método POST), body con formato {"usuario_id":1, "tarea_id": 1}
- Eliminar asignación de tarea a un usuario (ruta: /api/usuarios_tareas/id, método DELETE)

### Ejemplo (utilizando Postman)
- Login con usuario principal

  <img src="https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/6d36aa61-d53b-4ea8-8507-c7e5bc776307" height="500">

- Obtener usuarios

  <img src="https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/452c1847-da04-4ba6-927f-94bd3410b800" height="500">

- Ver usuario específico

  <img src="https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/92e4bded-c1ae-43d1-9640-2a8c38407488" height="500">

- Crear nuevo usuario

  <img src="https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/9feaf227-f257-4e1d-8083-5cb57ef04007" height="500">

- Eliminar usuario

  <img src="https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/6aa566fa-2aad-4d0b-b4f2-50778b8d2be5" height="500">

- Obtener proyectos

  <img src="https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/35f7d908-556e-4b8b-b013-56cfaae7a694" height="500">

- Crear nuevo proyecto

  <img src="https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/71bdc526-8bca-4d89-8992-6db4358706e5" height="500">

- Actualizar proyecto

  <img src="https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/4fce9337-ec25-4eb4-bfe4-69dcf48d1feb" height="500">

- Eliminar proyecto

  <img src="https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/51fb4669-4f18-45ed-ae28-5ab548e95f7c" height="500">

- Crear nueva tarea

  <img src="https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/9cff0484-5ef0-40c8-beee-9cb63f5677fe" height="500">

- Crear otra tarea más 

  <img src="https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/441515d6-9566-4e52-866f-1770a8f88c48" height="500">

- Actualizar tarea

  <img src="https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/cc8f0307-5739-4692-aab9-284775b53348" height="500">

- Marcar tarea como completada

  <img src="https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/a58b6fff-6736-4be0-ad41-026059873264" height="500">

- Obtener tareas

  <img src="https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/c8ffafe6-05fd-47e2-a1db-68a2cf0c485a" height="500">

- Obtener tareas del proyecto creado

  <img src="https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/d0362671-401b-4ec5-a4ea-9287c97e33a4" height="500">

- Asignar tarea a usuario

  <img src="https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/e7721f23-e4d7-4724-9fbc-5f2f38553a48" height="500">

- Asignar otra tarea a usuario

  <img src="https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/9085597a-e071-429d-a83a-5217cf249571" height="500">

- Obtener usuarios y tareas

  <img src="https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/d512a5b8-375a-4336-a9a9-5b5a90f6d674" height="500">

- Obtener usuarios con tareas asignadas (solo las pendientes o en proceso)

  <img src="https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/ce0fc7f0-ae88-4471-9977-b08e4a9b57f8" height="500">

- Eliminar proyecto creado

  <img src="https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/720b8959-145f-45ef-88c5-cea5fbbb8665" height="500">


