FROM python3.12-slim
WORKDIR /app
COPY . /app
RUN pip install --upgrade pip \
    pip install -r requirements