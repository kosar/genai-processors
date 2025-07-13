# HOWTO: Use GenAI Processors in a Web Application with a Local Ollama Model

This guide will walk you through the process of integrating the GenAI Processors library into a web application, using a locally hosted model with Ollama. This approach allows you to build powerful AI-powered web services that are not dependent on cloud-based AI platforms.

## Prerequisites

Before you begin, make sure you have the following installed:

*   Python 3.10+
*   Docker
*   Node.js and npm (or your preferred package manager)

## Step 1: Set Up a Local Ollama Server

Ollama is a tool for running large language models locally. We will use it to serve a local model that our web application can interact with.

1.  **Install Ollama:** Follow the instructions on the [Ollama website](https://ollama.ai/) to install it on your system.

2.  **Pull a model:** Once Ollama is installed, you can pull a model from the Ollama library. For this guide, we will use the `gemma:2b` model:

    ```bash
    ollama pull gemma:2b
    ```

3.  **Run the Ollama server:** Start the Ollama server in a separate terminal window:

    ```bash
    ollama serve
    ```

    The server will be available at `http://localhost:11434`.

## Step 2: Create a Web Service with FastAPI

Next, we will create a web service using FastAPI that encapsulates the GenAI Processors library. This service will expose an endpoint that our web application can call to interact with the local model.

1.  **Install dependencies:**

    ```bash
    pip install fastapi uvicorn genai-processors
    ```

2.  **Create the FastAPI application:** Create a file named `main.py` with the following code:

    ```python
    from fastapi import FastAPI
    from pydantic import BaseModel
    from genai_processors import processor
    from genai_processors.core.ollama_model import OllamaModel
    from genai_processors.content_api import ProcessorPart
    from typing import AsyncIterable

    app = FastAPI()

    class PromptRequest(BaseModel):
        prompt: str

    @processor
    async def ollama_processor(prompt: str) -> AsyncIterable[ProcessorPart]:
        model = OllamaModel(model="gemma:2b")
        async for part in model.call(prompt):
            yield part

    @app.post("/generate")
    async def generate(request: PromptRequest):
        response = ""
        async for part in ollama_processor(request.prompt):
            response += part.text
        return {"response": response}
    ```

3.  **Run the web service:**

    ```bash
    uvicorn main:app --reload
    ```

    The service will be available at `http://localhost:8000`.

## Step 3: Create a Web Application

Now, we will create a simple web application that interacts with our web service. For this guide, we will use a simple HTML page with JavaScript.

1.  **Create the HTML file:** Create a file named `index.html` with the following code:

    ```html
    <!DOCTYPE html>
    <html>
    <head>
        <title>GenAI Web App</title>
    </head>
    <body>
        <h1>GenAI Web App</h1>
        <textarea id="prompt" rows="4" cols="50"></textarea>
        <br>
        <button onclick="generate()">Generate</button>
        <hr>
        <h2>Response:</h2>
        <p id="response"></p>

        <script>
            async function generate() {
                const prompt = document.getElementById("prompt").value;
                const responseElement = document.getElementById("response");

                const response = await fetch("http://localhost:8000/generate", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify({ prompt }),
                });

                const data = await response.json();
                responseElement.innerText = data.response;
            }
        </script>
    </body>
    </html>
    ```

2.  **Serve the HTML file:** You can serve this file using a simple HTTP server. If you have Python installed, you can use the following command:

    ```bash
    python -m http.server
    ```

    Open your web browser and navigate to `http://localhost:8000`.

## Conclusion

You have now successfully integrated the GenAI Processors library into a web application, using a locally hosted model with Ollama. This setup provides a powerful and flexible way to build AI-powered web services that are both private and cost-effective. You can now build on top of this foundation to create more complex and sophisticated applications.
