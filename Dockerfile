FROM python:3.7
WORKDIR /exploradome_tangram
COPY . /exploradome_tangram
EXPOSE 5000
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["server.py"]