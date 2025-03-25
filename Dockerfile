FROM python:3.12.7-slim-bullseye as base
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    VIRTUAL_ENV=/auth/venv

WORKDIR /auth/app

COPY ./poetry.lock ./pyproject.toml ./

RUN python -m pip install --no-cache-dir "poetry==1.8.3" \
    && python -m venv --copies "${VIRTUAL_ENV}" \
    && . "${VIRTUAL_ENV}/bin/activate" \
    && poetry install --without dev --no-root

FROM python:3.12.7-slim-bullseye as final

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    VIRTUAL_ENV=/auth/venv

WORKDIR /auth/app

COPY --from=base ${VIRTUAL_ENV} ${VIRTUAL_ENV}

COPY . .

RUN chmod u+x ./app-entrypoint.sh

ENV PATH="${VIRTUAL_ENV}/bin:$PATH"

ENTRYPOINT ["sh", "/auth/app/app-entrypoint.sh"]
