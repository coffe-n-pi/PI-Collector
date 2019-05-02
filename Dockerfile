FROM jjanzic/docker-python3-opencv

COPY ./src /src
WORKDIR src
RUN pip install pipenv && \
    pipenv install

CMD ["pipenv", "run", "python", "cap.py"]
