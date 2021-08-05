#versão python do UVa Online Judge
FROM python:3.5.1 

WORKDIR /src
RUN apt install bash -y

COPY . .
ENTRYPOINT /bin/bash