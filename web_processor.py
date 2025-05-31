import requests
from bs4 import BeautifulSoup
import argparse
from urllib.parse import urljoin

KEYWORDS = ["polyester", "textile", "synthetic fabric", "100% polyester"]

def search_keywords(soup, keywords):
    """Searches for keywords in the parsed HTML content."""
    found_keywords = []
    if soup.body:
        body_text = soup.body.get_text(separator=' ', strip=True).lower()
        for keyword in keywords:
            if keyword.lower() in body_text:
                found_keywords.append(keyword)
    return found_keywords

def extract_links(soup, base_url):
    """Extracts all unique absolute links from the parsed HTML content."""
    links = set()  # Use a set to store unique links
    # Ensure soup object is not None and has a body before proceeding
    if soup and soup.body:
        for a_tag in soup.find_all('a', href=True): # soup.find_all is robust
            href = a_tag['href']
            absolute_url = urljoin(base_url, href)
            links.add(absolute_url)
    return list(links)

def main():
    # Setup command-line argument parsing
    parser = argparse.ArgumentParser(description="A command-line tool to fetch, search keywords in, and extract links from a web page.")
    parser.add_argument("url", help="The URL of the web page to process.")
    args = parser.parse_args()

    # Define a User-Agent header to mimic a browser request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    print(f"Processing URL: {args.url}...")

    try:
        # Make the HTTP GET request
        response = requests.get(args.url, headers=headers, timeout=10) # Added timeout
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)

        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        print(f"Successfully fetched and parsed URL: {args.url}")

        # Search for keywords
        found_keywords = search_keywords(soup, KEYWORDS)
        if found_keywords:
            print(f"\nFound predefined keywords: {', '.join(found_keywords)}")
        else:
            print("\nNo predefined keywords found on the page.")

        # Extract links
        extracted_links = extract_links(soup, args.url)
        if extracted_links:
            print("\nFound links on the page:")
            for link in extracted_links:
                print(f"- {link}")
        else:
            print("\nNo links found on the page.")

        print("\nTool functionality complete. Ready for packaging instructions.")

    except requests.exceptions.Timeout:
        print(f"Error: The request to {args.url} timed out.")
    except requests.exceptions.HTTPError as e:
        print(f"Error: HTTP error occurred while fetching {args.url}: {e}")
    except requests.exceptions.RequestException as e:
        # This catches other request-related errors like network issues
        print(f"Error: Could not fetch URL {args.url}. An error occurred: {e}")
    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
