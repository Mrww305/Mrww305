# GitHub Repository Viewer

## Description

This application fetches and displays the top 100 most starred and the top 100 most recently updated public repositories from GitHub. It provides a simple web interface to view these repository lists.

## Features

*   Lists the top 100 most starred GitHub repositories.
*   Lists the top 100 most recently updated GitHub repositories.
*   Simple web interface to view repository details including name, description, star count, and last updated date.
*   Repository names link directly to their GitHub pages.

## Setup and Installation

### Prerequisites

*   Python 3.x
*   `pip` (Python package installer)

### Instructions

1.  **Clone the repository (if applicable):**
    ```bash
    # git clone <repository_url> # Replace <repository_url> with the actual URL
    # cd <repository_directory>
    ```
    *(Note: Cloning is not directly applicable in the current execution environment but is standard practice.)*

2.  **Install dependencies:**
    Create a `requirements.txt` file with the following content:
    ```
    Flask
    requests
    ```
    Then, install the dependencies using pip:
    ```bash
    pip install -r requirements.txt
    ```

## Running Locally

1.  **Start the Flask development server:**
    ```bash
    python main.py
    ```
2.  **Access the application:**
    Open your web browser and navigate to `http://127.0.0.1:5000/`.

## Deployment

This Flask application can be deployed as a serverless function on various cloud platforms. Here's a general guide:

### General Concepts

*   **WSGI Handler:** Serverless environments often require a WSGI (Web Server Gateway Interface) handler to bridge the gap between the serverless platform and Flask. Tools like `serverless-wsgi` (for AWS Lambda) or similar utilities for other platforms can be used.
*   **Packaging:** Your application code (Python files, `templates` directory) and dependencies (listed in `requirements.txt`) need to be packaged, typically as a zip file, for deployment.
*   **Environment Variables:** While this application doesn't currently use environment variables for sensitive data like API keys, in a real-world scenario, you would configure these in your serverless function's settings rather than hardcoding them.

### AWS Lambda

*   **API Gateway:** Use Amazon API Gateway to create an HTTP endpoint that triggers your Lambda function.
*   **Lambda Function:**
    *   Create a new Lambda function with a Python runtime.
    *   Upload your packaged zip file.
    *   Configure the handler. If you're using `serverless-wsgi`, the handler might be `wsgi_handler.handler` or similar.
*   **Tools:** Consider using `serverless-wsgi` to adapt your Flask app or `Zappa` for a more automated deployment experience.

### Google Cloud Functions

*   **Native Support:** Google Cloud Functions natively supports Python Flask applications.
*   **Deployment:** You can deploy using the `gcloud functions deploy` command. You'll need to specify:
    *   A name for your function.
    *   The Python runtime (e.g., `python310`).
    *   The entry point (e.g., `app` if your Flask app instance is named `app` in `main.py`).
    *   The source directory or zip file.
    *   The trigger (e.g., HTTP).

### Azure Functions

*   **Python Support:** Azure Functions supports Python.
*   **Function App:** Create a Function App in Azure.
*   **Deployment:** Deploy your Flask application code. You might need to configure a `requirements.txt` and specify the entry point for your Flask app (often `main:app` or similar in the function configuration, pointing to `app` object in `main.py`). The specific way to adapt Flask might involve using Azure's Python Worker or specific libraries.

### `requirements.txt`

*   **Crucial for Dependencies:** Ensure your `requirements.txt` file is complete and up-to-date. Serverless platforms use this file to install the necessary Python packages (like Flask and Requests) in the execution environment.

This guidance provides a starting point. Refer to the specific documentation of your chosen cloud provider for detailed instructions.
