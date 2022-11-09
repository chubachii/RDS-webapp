# https://docs.nvidia.com/deeplearning/frameworks/tensorflow-release-notes/rel_22-03.html#rel_22-03
# Ubuntu : 20.04
# CUDA   : 11.6.1
# cuDNN  : 8.3.3.40
# Python : 3.8
# Tensorflow : 1.15.5

FROM nvcr.io/nvidia/tensorflow:22.03-tf1-py3

# 標準出力のバッファリングを無効化
ENV PYTHONUNBUFFERED 1 

# コマンド実行
RUN apt-get update && apt-get upgrade -y
RUN apt-get install python3-tk -y

# dockerfiles/requirements.txt をコピー
COPY ../requirements.txt .
RUN pip install -r requirements.txt