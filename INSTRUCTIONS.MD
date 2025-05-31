# Web Processor Tool Instructions

This tool fetches a webpage, searches for predefined keywords, and extracts all links from it.

## Prerequisites

Before running the script, you need to have Python 3 installed on your system.
You also need to install the following Python libraries:

*   `requests`
*   `beautifulsoup4`

You can install them using pip:

```bash
pip install requests beautifulsoup4
```

## Running the Script

To run the tool, navigate to the directory containing the `web_processor.py` script in your terminal or command prompt and use the following command:

```bash
python web_processor.py <URL_TO_PROCESS>
```

Replace `<URL_TO_PROCESS>` with the actual URL of the webpage you want to analyze.

**Example:**

```bash
python web_processor.py https://www.example.com
```

## Output

The script will print the following information to the console:

*   A message indicating which URL is being processed.
*   Any predefined keywords found on the page.
*   A list of all unique absolute URLs found on the page.
*   Error messages if the URL cannot be fetched or processed.

## Keywords

The script currently searches for the following keywords (case-insensitive):
- polyester
- textile
- synthetic fabric
- 100% polyester

This list is defined internally in the `web_processor.py` script.
