#이 명령어가 실행되면 Dockerhub에서 해당 이미지를 pull한다.
FROM nikolaik/python-nodejs:python3.10-nodejs14

#mkdir 명령어를 실행한다.
RUN mkdir /code

#동작 디렉토리를 /code로 옮긴다.
WORKDIR /code

#requirement.txt를 code 아래로 옮긴다.
ADD ./requirements.txt /code/requirements.txt 

#requirement.txt를 읽어서 필요한 패키지를 다운받는다
RUN pip install -r /code/requirements.txt 

#python과 nginx를 연결해주는 interface
RUN pip install gunicorn 

#현재 디렉토리를 /code에 복사해서 넣겠다
ADD . /code
# bash script 권한 설정
RUN ["chmod", "+x", "start.sh"]
# bash script 실행, 이 스크립트는 다음 챕터에서 만들겠다
ENTRYPOINT ["sh","./start.sh"]