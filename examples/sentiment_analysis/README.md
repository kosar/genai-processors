# Real-time Sentiment Analysis Example

This example demonstrates how to use `genai` processors to perform real-time sentiment analysis on a stream of social media data.

## Running the Example

1.  **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

2.  **Start the backend:**

    ```bash
    python backend/main.py
    ```

3.  **Open the frontend:**

    Open the `frontend/index.html` file in your web browser.

## How it Works

The backend uses a `PublicDatasetReader` processor to read data from a CSV file containing social media posts. The data is then passed to a `sentiment_analyzer` processor, which determines the sentiment of each post. The results are sent to the frontend using WebSockets, where they are displayed in real-time.

## Project Structure

*   `backend/`: Contains the Python code for the backend.
*   `frontend/`: Contains the HTML, CSS, and JavaScript for the frontend.
*   `data/`: Contains the dataset used in the example.
