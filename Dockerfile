FROM python:3.10-slim-bullseye
ENV PYTHONUNBUFFERED=1
#ENV PATH="/scripts:${PATH}"

COPY ./requirements.txt /oc_lettings_project/requirements.txt
RUN set -ex \
    && pip install --upgrade pip\
    && pip install --no-cache-dir -r /oc_lettings_project/requirements.txt
WORKDIR /oc_lettings_project
ADD . .
#CMD ["entrypoint.sh"]
CMD gunicorn oc_lettings_site.wsgi:application -b 0.0.0.0:$PORT -b 0.0.0.0:8000
