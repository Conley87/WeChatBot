FROM python:3.11-alpine

WORKDIR /wechatbot
ADD . .

RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

ENV REPLYMODE=
ENV SEND_API=
ENV DEBUG=true

CMD ["python","run.py"]
