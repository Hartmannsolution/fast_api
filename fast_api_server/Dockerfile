FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

ARG USER=vscode
ARG GROUP=vscode
ARG GROUP_ID=1000

COPY ./requirements.txt /tmp/requirements.txt
WORKDIR /tmp
RUN pip install -r requirements.txt

COPY ./app /app

# create a user to use for writing files inside the container with vs code.
RUN chown :$GROUP_ID /app \
&& chmod 775 /app \
&& chmod g+s /app \
&& addgroup --gid $GROUP_ID $GROUP \
&& adduser --disabled-password --gecos "" --force-badname --ingroup $GROUP $USER \
&& chown :$GROUP_ID /start.sh
# && echo "su $USER">> /start.sh

# RUN set -ex && apk --no-cache add sudo
# User must be root to run the start.sh script from the parent container.
# USER $USER

# Override CMD from parent container to run it as root "-s" for shell
# CMD ["su","&&","/start.sh"]
# CMD su root -c /start.sh
