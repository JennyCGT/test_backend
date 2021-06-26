# chat-backend

-- step1 : build python-django 
docker-compose build
-- step2: build with db
docker-compose up -d

docker-compose up --build 
-- step3: run migrations
docker-compose exec django python manage.py migrate --noinput
-- step4: create superuser
docker-compose exec django python manage.py createsuperuser
-- step5: collect statics files
docker-compose exec django python manage.py collectstatic

-- step6: enter docker
docker exec -ti django bash
docker exec -ti so /bin/sh   

Remover contenedores
docker ps -q | xargs docker rm -f docker rm -fv $(docker ps -aq)
Apagar 

--ver todos los contenedores
docker ps -a
-- borrar contenedor
docker rm nombre/id docker

--correr un contenedor en Dockerfile, estar en la carpeta del dockerfile 
docker build -t nombre cualquiera . 

--abrir el puerto de un contenedor
docker run -d --name nombre contenedor -p 80:80 nombre-imagen:latest

docker images -f dangling=true docker images -f dangling=true -q | xargs docker rmi


--build image
docker build -t jrtec/django-video-inspections .
--run docker container
docker run -p 5000:9080 <image id>

pgadmin4.db