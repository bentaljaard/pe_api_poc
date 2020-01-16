FROM python:3

ADD ie_customer_management /opt/ie_customer_management
COPY requirements.txt /tmp/requirements.txt

RUN pip3 install -r /tmp/requirements.txt
EXPOSE 5000
CMD [ "python3", "/opt/ie_customer_management/__init__.py" ]
