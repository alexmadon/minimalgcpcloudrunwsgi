FROM python:3.7
WORKDIR /
COPY . /
# RUN pip install --trusted-host pypi.python.org -r app/requirements.txt
EXPOSE 8080
CMD ["python", "minimal_webserver.py"]
