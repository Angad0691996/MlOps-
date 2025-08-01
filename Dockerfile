FROM nvidia/cuda:12.1.0-cudnn8-runtime-ubuntu22.04

RUN apt update && apt install -y python3 python3-pip git
COPY . /app
WORKDIR /app

RUN pip3 install -r requirements.txt

CMD ["python3", "train.py"]
