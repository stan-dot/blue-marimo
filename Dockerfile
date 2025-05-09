FROM ghcr.io/marimo-team/marimo:0.13.5

# Install any additional dependencies here

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    g++ \
    git
    # rm -rf /var/lib/apt/lists/*
    # libmagic1 \

CMD ["marimo", "edit", "--no-token", "-p", "8081", "--host", "0.0.0.0"]
