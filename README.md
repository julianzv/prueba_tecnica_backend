# Prueba técnica de backend
## Instalación y creación de entorno virtual:
`$ pip install virtualenv`
## Instalaciones requeridas en entorno virtual:
- `$ pip install flask flask_sqlalchemy flask_cors`
- `$ pip install psycopg2`
- `$ pip install bcrypt`
- `$ pip install python-dotenv`
- 
## Base de datos
Se utilizó PostgreSQL, las querys de creación de tablas se encuentran en el archivo 'db_querys.txt', mientras que el modelo entidad-relación se encuentra en la imagen 'modelo e-r.png'
## Funcionamiento
Es posible probar los endpoints con plataformas API como Postman.
### Inicio aplicación
Al ejecutar la aplicación (/backend/app.py), se insertan valores base, que son los estados de las tareas ("pendiente", "en progreso" y "completada") y también un usuario inicial. 

Se consideraron 4 módulos acorde a los requerimientos:
- Usuarios
- Tareas
- Proyectos
- Usuarios_tareas (para asignar/revisar las tareas de cada usuario)
### Módulo usuarios
- Ver todos los usuarios (ruta: /api/usuarios, método GET)
- Ver usuario específico (ruta: /api/usuarios/<id>, método GET) (ejemplo: /api/usuarios/1)
- Crear nuevo usuario (ruta: /api/usuarios, método POST), body con formato {"correo": "correo@ejemplo.com", "contraseña": "contraseña"}



