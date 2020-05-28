FROM python:latest

ADD . /celiatool

WORKDIR /celiatool

# Install native libraries, required for numpy
RUN pip --no-cache 

# Upgrade pip
RUN pip install --upgrade pip

# packages that we need
RUN pip install numpy && \
    pip install pandas && \
    pip install jupyter && \
    pip install sklearn


CMD ["main.py"]

ENTRYPOINT python3 main.py ./config.json
