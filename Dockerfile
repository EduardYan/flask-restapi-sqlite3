FROM alpine:3.15

# installing
RUN apk add python3 \
    && apk add py3-pip \
    && pip install --upgrade pip \
    && apk add sqlite

WORKDIR /myrestapi

COPY . /myrestapi

RUN pip install -r requirements.txt

# varialbe for work
ENV SQLITE_PATH="/myrestapi/database/books.db"

# running
CMD ["python3", "index.py"]