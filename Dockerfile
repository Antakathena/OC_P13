FROM python:3.10-slim-bullseye
ENV PYTHONUNBUFFERED=1
ENV PATH="/scripts:${PATH}"

COPY ./requirements.txt /oc_lettings_project/requirements.txt
RUN set -ex \
    && pip install --upgrade pip\
    && pip install --no-cache-dir -r /oc_lettings_project/requirements.txt
WORKDIR /oc_lettings_project
ADD . .
CMD ["entrypoint.sh"]

# add LABEL com.circleci.preserve-entrypoint=true? < https://circleci.com/docs/2.0/custom-images

#EXPOSE 8000
#RUN python manage.py collectstatic --noinput # ça ne passe pas comme ça
#RUN ls -a
#
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000", "--noreload"]

##CMD [ "gunicorn", "--bind", ":8000", "--workers", "3", "oc_lettings_site.wsgi:application" ]



#ENV PATH="/scripts:${PATH}"

## install requirements and updates, then delete the unnecessary files to lighten the container :
#COPY ./requirements.txt /requirements.txt
#RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers
#RUN pip install -r /requirements.txt
#RUN apk del .tmp
#
## create the file for the app inside the container and copy the needed files in it from . :
#RUN mkdir /app
#WORKDIR /app
#ADD . .
##COPY ./Python-OC-Lettings-FR /app ?
##COPY ./app /app
##COPY ./scripts /scripts
#
## give authorisations to the scripts
#RUN chmod +x /scripts/*
#
## ensure we have the possibility to add media and statics later :
#RUN mkdir -p /vol/web/media
#RUN mkdir -p /vol/web/static
#
##if we'd like a user with less priveledges for security reasons :
#RUN adduser -D user
#RUN chown -R user:user /vol
#RUN chmod -R 755 /vol/web
#USER user
#
#CMD ["entrypoint.sh"]
 # nb : en utilisant un script séparé on peut faire tourner collectstatic sans soucis
 # https://www.reddit.com/r/django/comments/gj96uq/dockercompose_collect_static/

# Ajouter au requirements.txt: uWSGI>=2.0.18,<2.1
# retirer de gitignore et dockerignore les scripts
