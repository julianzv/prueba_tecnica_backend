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
<img src="https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/6d36aa61-d53b-4ea8-8507-c7e5bc776307" height="200">

- Obtener usuarios
<img src="https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/452c1847-da04-4ba6-927f-94bd3410b800" height="200">

- Ver usuario específico
<img src="https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/92e4bded-c1ae-43d1-9640-2a8c38407488" height="200">

- Crear nuevo usuario
<img src="https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/9feaf227-f257-4e1d-8083-5cb57ef04007" height="200">

