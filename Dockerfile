FROM fedora:39

WORKDIR /app

RUN dnf update -y && dnf install -y \
    python3 \
    python3-pip \
    gcc \
    python3-devel \
    libgomp \
    && dnf clean all

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt
RUN python3 setup.py build_ext --inplace

EXPOSE 8000

CMD ["python3"]
