# Prueba técnica de Backend
## Instalación, creación y ejecución de entorno virtual:
- `$ pip install virtualenv`
- `$python -m venv venv`
- `$venv\Script\activate`
## Instalaciones requeridas en entorno virtual:
- En archivo /backend/requirements-python.txt se encuentra una lista de las librerías utilizadas, las cuales pueden instalarse con `$pip install -r requirements.txt`. Se utilizó el framework Flask.
## Creación del proyecto en React e instalaciones necesarias
- Es necesario tener NodeJS instalado.
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
- Crear nuevo usuario (ruta: /api/usuarios, método POST), body con formato {"correo": "correo@ejemplo.com", "contraseña": "contraseña"}. La contraseña se encripta con el algoritmo bcrypt, almacenandose así en la  base de datos. 
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
![1-login-admin](https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/5428a312-8739-41b0-9e7d-876055459614)
![2-get-usuarios](https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/336e27a8-4f1f-4a6a-9f8f-12ba8fe44b63)
![3-get-usuario](https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/8917d749-f382-4354-aa57-37c10bcd0261)
![4-create-usuario](https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/2ca1524b-5b8a-4521-b297-4471e2a4690f)
![4-delete-usuario](https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/343ef02f-d0d4-4dbb-acc6-5468b414320f)
![5-get-proyectos](https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/f94c8322-6ee9-4097-98de-c533ab5980a4)
![6-create-proyecto](https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/c495a01d-dc3d-4116-b1da-9bbec870f34e)
![7-update-proyecto](https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/a37be5ab-ecae-48c5-ab4f-c6e9f1db258b)
![8-delete-proyecto](https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/df1b99cf-0a04-400f-9f70-48625feab7d2)
![9-create-tarea](https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/06fa05e4-50a7-43d2-8e85-7aa9faa16bb3)
![10-create-tarea-2](https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/3ce9b14f-3c7b-406d-acaa-36aa5ed46fc3)
![11-update-tarea](https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/8aa0b56b-3551-49cd-8d7b-d99102d9e14f)
![12-update-tarea-completa](https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/cef0d0bb-aea1-4944-998a-14a496891698)
![13-get-tareas](https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/67ddd07d-afc5-4e12-81ed-fb64a067318d)
![14-get-proyectos-tareas](https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/3c7d1989-9453-4c31-815e-3f096e69c37d)
![15-create-usuarios-tareas](https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/44bcb172-ae66-4c9a-9ce5-bf510b9268be)
![16-create-usuarios-tareas-2](https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/def7b967-4b37-4469-8344-f2c8e4af87e3)
![17-get-usuarios-tareas](https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/81e689e9-cc8a-47be-8050-4f7b0905e27e)
![18-get-usuarios-tareas-asignadas](https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/d06f1bb2-5480-4fdf-bcc0-27b8628f0a33)
![19-delete-proyecto-fin](https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/d972a9be-342c-4870-814e-342e8ac1ec61)


## Funcionamiento frontend 
Se realizaron las siguientes vistas:
- Vista de Login 
- Vista de Home, rutas:
  - Gestión de usuarios y tareas (permite ver, agregar, eliminar usuarios, asignarles tareas y eliminar sus tareas).
  - Gestión de tareas (permite ver, agregar, editar, eliminar y marcar completadas las tareas).
  - Ver mis tareas (muestra en pantalla una tabla con la lista de tareas que no se han terminado del usuario que ingresó.
  - Gestión de proyectos (permite agregar, editar, eliminar y ver los detalles y tareas de cada proyecto)  

Las llamadas a la api se realizan desde /utils/api.js, comunicando así el frontend y el backend.

### Capturas (frontend)

- Login
<img src="https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/0494a60d-f982-4e2c-ade0-36b60a318c98" height="350">

- Ver proyectos
<img src="https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/b1ab7739-ab21-40af-a5d6-4a2d6319ef49" height="350">

- Ver usuarios
<img src="https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/b7707b44-5b3d-4b56-96d3-ec21d67e1397" height="350">

- Ver tareas de usuario
<img src="https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/c679ffe3-0562-4cda-adff-a5616b31bb6c" height="350">

- Crear tarea
<img src="https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/e65794fc-8cce-44ff-81bf-920d19e33c0d" height="350">

- Ver tareas asignadas
<img src="https://github.com/virtualjoker00/prueba_tecnica_backend/assets/108155631/e0a5759e-0662-4447-9f90-6838857300d3" height="350">

