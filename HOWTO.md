# HOWTO: Use GenAI Processors in a Web Application with a Local Ollama Model

This guide will walk you through the process of integrating the GenAI Processors library into a web application, using a locally hosted model with Ollama. This approach allows you to build powerful AI-powered web services that are not dependent on cloud-based AI platforms.

## What You'll Build

You will build a web application that allows users to interact with a local large language model. The application will have a simple interface where users can enter a prompt and receive a response from the model. The web application will be powered by a FastAPI backend that uses the GenAI Processors library to communicate with the local model.

This project serves as a starting point for building more complex applications that leverage the power of the GenAI Processors library. You can extend this project to create applications such as:

*   **A chatbot that can answer questions about your documents.**
*   **A content generation tool that can write articles, emails, and social media posts.**
*   **A code generation assistant that can help you write code faster.**

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

## Mock Press Release

**FOR IMMEDIATE RELEASE**

**New Web App Unleashes the Power of Local AI for Everyone**

[City, State] – [Date] – A new web application launched today promises to revolutionize the way people interact with artificial intelligence. The app, built on the powerful GenAI Processors library and open-source models, allows anyone to run a large language model on their own computer, free from the constraints of cloud-based platforms.

“We believe that AI should be accessible to everyone,” said the app’s creator. “By leveraging the GenAI Processors library and open models, we’ve created a tool that is not only powerful and flexible but also private and secure. Your data never leaves your computer.”

The new web app can be used for a wide range of applications, from writing and content creation to coding and data analysis. Its modular design, a core feature of the GenAI Processors library, allows for easy customization and extension, making it a valuable tool for developers and researchers.

“This is a game-changer,” said one early user. “The ability to run a powerful AI model locally, without having to pay for expensive cloud services, is incredible. I can’t wait to see what people build with this.”

The web app is available now and can be downloaded from the project’s website.

## Technical Prompt for a Coding Assistant

You are an expert software engineer tasked with building a web application that leverages the GenAI Processors library and a locally hosted large language model. The goal is to create a robust and scalable web service that can be easily integrated with a modern web front-end.

Here’s a breakdown of the task:

1.  **Set up the backend:**
    *   Create a FastAPI application that will serve as the backend for the web service.
    *   Implement an endpoint that accepts a prompt from the user.
    *   Use the GenAI Processors library to create a processor that interacts with a locally hosted Ollama model (e.g., `gemma:2b`).
    *   The processor should take the user’s prompt as input and return the model’s response as a stream of text.
    *   The endpoint should stream the response back to the client as it is generated.

2.  **Develop the front-end:**
    *   Create a simple and intuitive user interface using HTML, CSS, and JavaScript.
    *   The interface should include a text area for the user to enter their prompt and a button to submit it.
    *   The response from the model should be displayed in a clear and readable format.
    *   The front-end should be able to handle streaming responses from the backend, updating the UI in real-time as the response is generated.

3.  **Deployment:**
    *   Containerize the application using Docker.
    *   Provide instructions for deploying the application to a cloud platform such as Vercel, Google Cloud, or AWS.

Your solution should be well-documented, with clear instructions on how to set up and run the application. The code should be clean, efficient, and easy to maintain. You should also consider potential challenges, such as handling long-running requests and managing the state of the application.

## Guidance for Cloud Architects

As a cloud architect, your goal is to design a scalable, resilient, and cost-effective infrastructure for deploying applications built with the GenAI Processors library. Here's a guide to help you make informed decisions when building out a plan for your platform.

### Understanding GenAI Processors

The GenAI Processors library is designed to be lightweight and flexible, allowing developers to build complex AI pipelines by chaining together modular processors. The core of the library is the `Processor` class, which operates on asynchronous streams of `ProcessorPart` objects. This architecture has several implications for deployment:

*   **Statelessness:** Processors are generally stateless, meaning they don't retain any information between requests. This makes them easy to scale horizontally.
*   **Asynchronous Nature:** The library is built on `asyncio`, making it well-suited for I/O-bound tasks and real-time applications.
*   **Local Model Dependency:** The example application uses a locally hosted Ollama model. In a production environment, you will need to decide whether to continue using a local model or switch to a managed AI service.

### Deployment Patterns

Here are a few deployment patterns to consider, depending on your specific requirements:

*   **Serverless:** For applications with intermittent traffic, a serverless approach (e.g., AWS Lambda, Google Cloud Functions) can be a cost-effective option. You can package the FastAPI application and its dependencies into a container image and deploy it as a serverless function.
*   **Container Orchestration:** For applications with high traffic or long-running requests, a container orchestration platform (e.g., Kubernetes, Amazon ECS) is a better choice. This will allow you to scale the application horizontally and manage the containers effectively.
*   **Managed AI Services:** If you prefer not to manage your own AI models, you can use a managed AI service (e.g., Google AI Platform, Amazon SageMaker). The GenAI Processors library can be easily adapted to work with these services by creating a custom processor that calls the service's API.

### Best Practices

Here are some best practices to follow when deploying a GenAI Processors application on your platform:

*   **Infrastructure as Code (IaC):** Use a tool like Terraform or AWS CloudFormation to define your infrastructure as code. This will make it easier to manage and reproduce your environment.
*   **CI/CD:** Set up a CI/CD pipeline to automate the process of building, testing, and deploying your application.
*   **Monitoring and Logging:** Use a monitoring and logging service to track the performance of your application and identify any issues.
*   **Security:** Follow security best practices to protect your application and data. This includes using a firewall, encrypting data in transit and at rest, and managing access to your resources.

By following these guidelines, you can design a robust and scalable infrastructure for your GenAI Processors application that will meet the needs of your users and your business.
