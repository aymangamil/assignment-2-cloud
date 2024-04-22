FROM python 
WORKDIR /py
COPY . /py
CMD ["python3", "py.py"]