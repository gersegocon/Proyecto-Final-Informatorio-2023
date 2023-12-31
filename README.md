Integrantes:
- *Segovia Contrera, Germán*
- *Iturri, Luciano*
- *Toloza, Marcos*

Dirección página web:
-_https://viajazos.pythonanywhere.com/_


Pasos para correr proyecto:
- En carpeta deseada: *git clone https://github.com/gersegocon/Proyecto-Final-Informatorio-2023*
- Crear entorno virtual: *python -m venv "EntornoVirtual"*
- Activar entorno virtual: Entrar a la carpeta del entorno, en este caso: EntornoVirtual\Scripts\activate
- Con el entorno activado, ir a la carpeta del proyecto ...Proyecto-Final-Informatorio-2023\blog
- Instalar los requisitos: *pip install -r requeriments.txt*
- Entrar al archivo ...Proyecto-Final-Informatorio-2023\blog\blog\settings\local.py, configurar nombre de usuario y contraseña de la base de datos de acuerdo a su configuración
- Crear la base de datos correspondientes en MySQL Worckbench
- Volver a la linea de codigos y ejecutar: *python manage.py makemigrations*
- Luego: *python manage.py migrate*
- Finalmente: *python manage.py runserver*
  
