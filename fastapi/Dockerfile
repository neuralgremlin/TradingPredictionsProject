  
FROM python:3.8

WORKDIR /app

RUN apt-get -y update  && apt-get install -y \
  python3-dev \
  apt-utils \
  python-dev \
  build-essential \
&& rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade setuptools
RUN pip install \
    cython==0.29.24 \
    numpy==1.21.1 \
    pandas==1.3.1 \
    pystan==2.19.1.1

RUN pip install convertdate==2.1.2 lunarcalendar==0.0.9 holidays==0.10.3
RUN pip install tqdm --upgrade
RUN pip install gunicorn
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN python model_setup.py
CMD gunicorn -w 3 -k uvicorn.workers.UvicornWorker main:app --bind 0.0.0.0:$PORT
