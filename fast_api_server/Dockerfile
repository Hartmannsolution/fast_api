FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

# ARG USER=vscode
# ARG USER_UID=1000
# ARG USER_GID=$USER_UID

COPY ./requirements.txt /tmp/requirements.txt
WORKDIR /tmp
RUN pip install -r requirements.txt


COPY ./app /app
# RUN adduser --disabled-password $USER \
#         && echo "$USER ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/$USER \
#         && chmod 0440 /etc/sudoers.d/$USER

# USER $USER
# WORKDIR $HOME
# This is used for running the terminal in vscode as user: vscode
# RUN groupadd --gid $USER_GID $USERNAME \
    # && useradd -s /bin/bash --uid $USER_UID --gid $USER_GID -m $USERNAME
    # [Optional] Add sudo support for the non-root user
    # && sudo add-apt-repository main \
    # && apt-get install -y sudo \
    # && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME\
    # && chmod 0440 /etc/sudoers.d/$USERNAME

# enable sudo
# RUN set -ex && apk --no-cache add sudo
# USER vscode