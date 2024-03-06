###################
# Base image: lfe #
###################

FROM python as lfe

WORKDIR /app

COPY ./requirements.txt /app

RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED=1

EXPOSE 3000

###############
# Debug Image #
###############

FROM lfe as lfe-debug

COPY ./requirements-dev.txt /app

RUN pip install -r requirements-dev.txt

EXPOSE 5678

ENTRYPOINT [ "python", "-Xfrozen_modules=off", "-m", "debugpy", "--listen", "0.0.0.0:5678", "LFE/manage.py", "runserver", "0.0.0.0:3000" ]


#################
# Release Image #
#################

FROM lfe as lfe-release

ENTRYPOINT ["python", "LFE/manage.py", "runserver", "0.0.0.0:3000"]
