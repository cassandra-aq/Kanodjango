# Base image
FROM python:3.12-slim AS base

WORKDIR /opt/app

COPY . /opt/app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONPATH /opt/app:$PYTHONPATH
ENV DJANGO_SETTINGS_MODULE=kanodjango.settings
ENV TERM=xterm-256color

# Create default user
ARG USER_NAME=docker_user
ARG USER_UID=1000
ARG USER_GID=1000

RUN apt-get update \
  && apt-get install -y gettext build-essential --no-install-recommends \
  && rm -rf /var/lib/apt/lists/* /usr/share/doc /usr/share/man && \
  groupadd ${USER_NAME} --non-unique --gid ${USER_GID} && \
  useradd ${USER_NAME} --non-unique --uid ${USER_UID} --gid ${USER_GID} --shell /bin/bash && \
  chown -R ${USER_UID}:${USER_GID} .

# Development stage
FROM base AS development

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

CMD ["python", "/opt/app/manage.py", "runserver", "0.0.0.0:8000"]

# Production stage
FROM base AS production

RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    python3 manage.py collectstatic --noinput

CMD ["python", "/opt/app/manage.py", "runserver", "0.0.0.0:8000"]
