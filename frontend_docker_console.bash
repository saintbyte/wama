
docker run --rm -it --name frontend  -v $PWD/src:/code -w /code -e "PORT=3000" -p 8080:3000  frontend:latest /bin/bash
