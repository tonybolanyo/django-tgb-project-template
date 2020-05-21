# ---- Python base ----
FROM python:3.7-slim AS base

# Needed for ERD docs generation
RUN apt-get update && apt-get install -y graphviz libgraphviz-dev pkg-config

# ---- Dependencias del sistema
FROM base AS system-base

###########################################################################
# non-root user: tgb
###########################################################################
###########################################################################
# User Aliases
###########################################################################
USER root
# Add a non-root user to prevent files being created with root permissions on host machine.
ARG PUID=1000
ENV PUID ${PUID}
ARG PGID=1000
ENV PGID ${PGID}

# Add user as non-root. If everithing runs as root user
# you can edit files outside docker container (i.e., in host machine)
RUN groupadd -g ${PGID} tgb && \
  useradd -u ${PUID} -g tgb -m tgb && \
  usermod -p "*" tgb -s /bin/bash

COPY ./src /app/
COPY ./docker/start.sh /start.sh
COPY ./docker/wait_for_postgres.sh /wait_for_postgres.sh
RUN chmod +x /start.sh && chmod +x /wait_for_postgres.sh && mkdir /logs

# ---- Python requirements
FROM system-base AS dependencies

RUN mkdir -p /app/requirements

COPY ./requirements/base.txt /app/requirements/
COPY ./requirements/docs.txt /app/requirements/
COPY ./requirements/dev.txt /app/requirements/
COPY ./requirements/test.txt /app/requirements/
COPY ./requirements/audit.txt /app/requirements/

RUN pip install --upgrade pip \
 && pip install -r /app/requirements/dev.txt

# ---- Release target
FROM system-base as release

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


COPY --from=dependencies /root/.cache /root/.cache
COPY --from=dependencies /app/requirements/base.txt /app/requirements/
COPY ./requirements/prod.txt /app/requirements/
RUN pip install -r /app/requirements/prod.txt && rm -rf /root/.cache

RUN chown -R tgb:tgb /app
WORKDIR /app

# ---- Development version
FROM dependencies AS develop

COPY --from=dependencies /root/.cache /root/.cache
COPY --from=dependencies /app/requirements/base.txt /app/requirements/
COPY ./requirements/dev.txt /app/requirements/
RUN pip install -r /app/requirements/dev.txt && rm -rf /root/.cache

COPY ./docker/run_tests.sh /app/

RUN chown -R tgb:tgb /app
WORKDIR /app/src
