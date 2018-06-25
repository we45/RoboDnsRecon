FROM python:3.6

RUN apt update && apt install -y git

RUN git clone https://github.com/we45/dnsrecon.git
RUN pip install -r /dnsrecon/requirements.txt
RUN mkdir /dnsrecon_results
ENTRYPOINT ["/dnsrecon/dnsrecon.py"]
