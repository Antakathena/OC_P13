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

