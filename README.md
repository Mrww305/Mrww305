# Simple CLI Chatbot

This is a command-line chatbot designed to act as a social media query handler, with a basic focus on car maintenance topics. It requires a Google API key to be provided at runtime for its (placeholder) core chat functionalities.

**Note:** The actual integration with a specific Google Chat API is currently a placeholder. You will need to replace the placeholder function with actual API calls using the appropriate Google client library.

## Prerequisites

- Python 3.x
- Pip (Python package installer)

## Setup

1.  **Clone the repository (if you haven't already):**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: `requirements.txt` currently includes `google-api-python-client` as a general placeholder. You might need to adjust this based on the specific Google API you choose to integrate.)*

## Running the Chatbot

To run the chatbot, you need to provide your Google API key using the `--api-key` command-line argument:

```bash
python chatbot.py --api-key YOUR_API_KEY_HERE
```

Replace `YOUR_API_KEY_HERE` with your actual Google API key.

Once running, you can type your queries into the console. Type `exit` to quit the chatbot.

## Functionality

-   Accepts a Google API key at runtime (not stored).
-   Simulates interaction with a Google Chat API (current implementation is a placeholder).
-   Includes very basic keyword spotting for car maintenance related queries to provide slightly tailored (placeholder) responses.
-   Basic error handling for API key input and simulated API calls.

## Future Development

-   Integrate with a specific Google Chat/NLP API (e.g., Dialogflow, Vertex AI, Google Cloud Natural Language API).
-   Expand car maintenance query understanding beyond simple keywords.
-   Implement more robust error handling for specific API responses.
-   Develop more sophisticated conversation management.
