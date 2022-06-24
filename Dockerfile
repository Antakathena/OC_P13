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
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000", "--noreload"]

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

# retirer de gitignore et dockerignore les scripts
