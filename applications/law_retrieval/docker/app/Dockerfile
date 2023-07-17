FROM --platform=linux/amd64 python:3.10
WORKDIR /code
COPY requirements.txt .
RUN pip3 install https://gitlab.com/trungtv/vi_spacy/-/raw/master/vi_core_news_lg/dist/vi_core_news_lg-0.0.1.tar.gz
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt
COPY src src
CMD ["uvicorn", "src.main:app","--host","0.0.0.0" ,"--port", "80"]