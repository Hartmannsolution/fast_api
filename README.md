# restful api with Fast API
source: https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker#quick-start
source: https://codeburst.io/implement-a-production-ready-rest-service-using-fastapi-13f284562c75

## Development
Change `main.py`
From same folder run: `uvicorn main:app --reload`
This will provide hot reload of webserver when changes are made to main.py

## Docker
`docker-compose up --build` will start a webserver on `localhost:8001` and documentation on `localhost:8001/docs`

## VS Code
Extension to install: Remote-Containers
Then in bottom left corner press green icon. (ctrl+shift+p -> Remote-Containers: attach to running container) choose "fast_api_server" from the list of running containers

open a terminal in vs code (it will open as root in the container). enter: `uvicorn main:app --reload` -> ctrl+click on the server link. A browser will open to show the api server

Make changes to main.py and see how the server is reloaded and changes takes effect in browser.

- Inside the devcontainer.json file add: `"remoteUser key": "vscode",` in order to be logged in as vscode instead of root in the terminal (This means that ownership of new files will not be root and thereby locked for other users.)
