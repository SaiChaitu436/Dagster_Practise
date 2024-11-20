# # Base Python Image
# FROM python:3.9-slim

# # Install dependencies
# RUN apt-get update && apt-get install -y \
#     build-essential \
#     libpq-dev \
#     && rm -rf /var/lib/apt/lists/*

# # Set working directory
# WORKDIR /opt/dagster

# # Copy files
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# COPY . .

# # Expose port for Dagit
# EXPOSE 3000

# # CMD ["dagit", "-w", "workspace.yaml", "-h", "0.0.0.0"]
# CMD ["dagster-webserver", "-w", "workspace.yaml", "-h", "0.0.0.0"]



# FROM python:3.9-slim

# WORKDIR /app

# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# COPY . .

# CMD ["dagster", "dev"]




# FROM python:3.10-slim//

# RUN mkdir -p /opt/dagster/dagster_home /opt/dagster/app

# RUN pip install dagster-webserver dagster-postgres dagster-aws

# # Copy your code and workspace to /opt/dagster/app
# COPY repo.py workspace.yaml /opt/dagster/app/

# ENV DAGSTER_HOME=/opt/dagster/dagster_home/

# # Copy dagster instance YAML to $DAGSTER_HOME
# COPY dagster.yaml /opt/dagster/dagster_home/

# WORKDIR /opt/dagster/app

# EXPOSE 3000

# ENTRYPOINT ["dagster-webserver", "-h", "0.0.0.0", "-p", "3000"]



FROM python:3.10-slim

WORKDIR /usr/src/app
ENV DAGSTER_HOME=/usr/src/app


RUN pip install dagster dagster-webserver dagit dagster-postgres SQLAlchemy==1.4.49 pandas pyarrow

# Copy our code and workspace to /usr/src/app
COPY dagster.yaml workspace.yaml ./
COPY my_dagster_project ./my_dagster_project
COPY pyproject.toml setup.py ./

# Install the project
RUN pip install --no-cache-dir .


EXPOSE 3000

CMD ["dagster-webserver", "-w", "workspace.yaml", "-h", "0.0.0.0", "-p", "3000"]
