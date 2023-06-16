# Prueba técnica de Backend
## Instalación y creación de entorno virtual:
`$ pip install virtualenv`
## Instalaciones requeridas en entorno virtual:
- `$ pip install flask flask_sqlalchemy flask_cors`
- `$ pip install psycopg2`
- `$ pip install bcrypt`
- `$ pip install python-dotenv`
## Instalaciones requeridas para el Frontend (React)
- `$ npm install react-router-dom`
## Base de datos
Se utilizó PostgreSQL, las querys de creación de tablas se encuentran en el archivo 'db_querys.txt', mientras que el modelo entidad-relación se encuentra en la imagen 'modelo e-r.png'
## Funcionamiento backend
Es posible probar los endpoints con plataformas API como Postman.
### Inicio aplicación
Al ejecutar la aplicación (/backend/app.py), se insertan valores base, que son los estados de las tareas ("pendiente", "en progreso" y "completada") y también un usuario inicial. Al estar los estados asociados a las tareas en tablas separadas, se consideran las id de los estados:
- 1: pendiente
- 2: en progreso
- 3: completada

La aplicación corre en la ruta http://localhost:8080/, por ejemplo para ver los usuarios la ruta será http://localhost:8080/api/usuarios (método GET).

Se consideraron 5 módulos acorde a los requerimientos:
- Login
- Usuarios
- Tareas
- Proyectos
- Tareas de usuarios

En las rutas que utilicen "id" o "tabla_id", reemplazar por el número de id. 
### Módulo login
- Iniciar sesión (ruta: /api/login, método POST), body con formate {""correo": "correo@ejemplo.com", "contraseña": "contraseña"}
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

### Módulo de tareas de usuarios
- Ver todas las asignaciones de tareas de los usuarios (ruta: /api/usuarios_tareas, método GET)
- Ver las tareas de un usuario específico (ruta: /api/usuarios_tareas/usuario_id)
- Crear una asignación de tarea a un usuario (ruta: /api/usuarios_tareas, método POST), body con formato {"usuario_id":1, "tarea_id": 1}
- Eliminar asignación de tarea a un usuario (ruta: /api/usuarios_tareas/id, método DELETE)

