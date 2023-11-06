FROM ubuntu:18.04

RUN apt-get update && apt-get install -y socat libc6-i386

COPY ./pwn7 /home/pwn7
COPY ./flag /home/flag

WORKDIR /home

CMD ["socat" ,"tcp-listen:12345,reuseaddr,fork","exec:/home/pwn7"]



