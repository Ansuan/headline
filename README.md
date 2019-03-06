# Flash Heroku headline
## Requisitos
gunicorn

feedparser

Flask
## Configuración
Generar un archivo llamado ***requirements.txt*** en el que contendra los paquetes de software y su versión que seran instalado desde Heroku con PiP
```txt
gunicorn==19.9.0
feedparser==5.2.1
Flask==1.0.2
```
Tambien puedes hacer uso del comando ***pip freeze > requirements.txt*** con el que te generar tal archivo con todos los paquetes de software instalados en el equipo

A continuación, generar un archivo llamado ***Procfile*** en el que contendra el comando con el que se ejecutara el proyecto.
```txt
web: gunicorn headlines:app
```

## Heroku
