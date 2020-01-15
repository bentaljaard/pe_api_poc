FROM python:3

ADD nl_customer_management /opt/nl_customer_management
COPY requirements.txt /tmp/requirements.txt

RUN pip3 install -r /tmp/requirements.txt
EXPOSE 5000
CMD [ "python3", "/opt/nl_customer_management/__init__.py" ]
