#versão python do UVa Online Judge
FROM python:3.5.1 

WORKDIR /src

COPY . .
RUN apt install bash -y

ENTRYPOINT /bin/bash