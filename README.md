# Proof of Concept Project with Langchain, FastAPI, and OpenAI

This project is a Proof of Concept (POC) that utilizes Langchain, FastAPI, and OpenAI to create an API that provides three different endpoints. Before running the project, make sure you have Docker installed and complete the `.env` file with your OpenAI API key.

## Configuration

1. Install Docker if you haven't already on your system.

2. Complete the `.env` file with your OpenAI API key as follows:

`OPENAI_API_KEY=YOUR_API_KEY`


## Running the Project

Once you have configured the environment, follow these steps to run the project:

1. Run the following command to create the container containing the API:

```make build```


2. After the container build is successful, you can start the API with the following command:

```make start```


3. The API will run at http://0.0.0.0:8000/.

## Available Endpoints

Once the API is up and running, you will have access to three different endpoints:

- `/openai/playground/`: This endpoint is a wrapper for OpenAI's ChatGPT. You can interact with the GPT-3.5 model through this endpoint.

- `/joke/playground/`: Send a topic to this endpoint, and you will receive a joke related to that topic.

- `/billtrust/playground/`: You can ask questions about Billtrust, and the API will use information from the "about" section of the Billtrust website to provide relevant answers.

## Accessing the Endpoints

You can access the endpoints from your web browser using the following base URL:

- Billtrust Playground: [http://0.0.0.0:8000/billtrust/playground/](http://0.0.0.0:8000/billtrust/playground/)

Make sure to modify the base URL according to the endpoint you want to use.

Enjoy exploring this POC project!
