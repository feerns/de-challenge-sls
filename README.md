# de-challenge-sls

### Description
This repository contains a FastAPI API for the AI + Data Engineer Challenge by Shadow Light Studios.
The API has one single endpoint that returns an anlytics result for two KIPs: CAC and ROAS.

The used DataWarehouse is BigQuery and the NoSQL database is CloudSQL.
The ETL process is orchestrated with N8N.

### Installation
Requires Python 3.12+.

#### Installation and run FastAPI with UV
1. Follow the steps in the [official documentation](https://docs.astral.sh/uv/getting-started/installation/).
2. Clone this repository.
3. Navigate to the project directory.
4. Run `uv run fastapi  dev` to install the dependencies and start the development server.
5. The API will be available at `http://localhost:8000`.
6. You can access the API documentation at `http://localhost:8000/docs`.

#### Installation and run FastAPI  with python and pip
1. Clone this repository.
2. Navigate to the project directory.
3. Create a virtual environment with `python -m venv venv`.
4. Activate the virtual environment
5. Run `pip install -r requirements.txt` to install the dependencies.
6. Run `fastapi run main.py --reload` to start the development server.
7. The API will be available at `http://localhost:8000`.
8. You can access the API documentation at `http://localhost:8000/docs`.

#### Trigger the ETL process
1. Clone the repo
2. Create and activate a virtual environment
3. Install the dependencies with one of the options above
4. run the script in n8n_connector/trigger_workflow.py