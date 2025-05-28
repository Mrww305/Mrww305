import requests

def get_most_starred_repositories(count=5):
    """
    Fetches the most starred repositories from GitHub.

    Args:
        count (int): The number of repositories to fetch.

    Returns:
        list: A list of dictionaries, where each dictionary contains repository details.
              Returns an empty list if an error occurs.
    """
    url = "https://api.github.com/search/repositories"
    headers = {"Accept": "application/vnd.github.v3+json"}
    params = {
        "q": "stars:>0",
        "sort": "stars",
        "order": "desc",
        "per_page": count,
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()
        repositories = []
        for item in data.get("items", []):
            repositories.append({
                "name": item.get("name"),
                "html_url": item.get("html_url"),
                "description": item.get("description"),
                "stargazers_count": item.get("stargazers_count"),
                "updated_at": item.get("updated_at"),
            })
        return repositories
    except requests.exceptions.RequestException as e:
        print(f"Error fetching most starred repositories: {e}")
        return []

def get_latest_updated_repositories(count=5):
    """
    Fetches the most recently updated repositories from GitHub.

    Args:
        count (int): The number of repositories to fetch.

    Returns:
        list: A list of dictionaries, where each dictionary contains repository details.
              Returns an empty list if an error occurs.
    """
    url = "https://api.github.com/search/repositories"
    headers = {"Accept": "application/vnd.github.v3+json"}
    # Using a recent date for "updated" query, adjust as needed
    params = {
        "q": "updated:>2023-01-01",  # Example: repositories updated after Jan 1, 2023
        "sort": "updated",
        "order": "desc",
        "per_page": count,
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()
        repositories = []
        for item in data.get("items", []):
            repositories.append({
                "name": item.get("name"),
                "html_url": item.get("html_url"),
                "description": item.get("description"),
                "stargazers_count": item.get("stargazers_count"),
                "updated_at": item.get("updated_at"),
            })
        return repositories
    except requests.exceptions.RequestException as e:
        print(f"Error fetching latest updated repositories: {e}")
        return []

if __name__ == "__main__":
    starred_repos = get_most_starred_repositories()
    if starred_repos:
        print("Most Starred Repositories:")
        for repo in starred_repos:
            print(
                f"  Name: {repo['name']}\n"
                f"  URL: {repo['html_url']}\n"
                f"  Description: {repo['description']}\n"
                f"  Stars: {repo['stargazers_count']}\n"
                f"  Updated At: {repo['updated_at']}\n"
            )

    latest_repos = get_latest_updated_repositories()
    if latest_repos:
        print("\nLatest Updated Repositories:")
        for repo in latest_repos:
            print(
                f"  Name: {repo['name']}\n"
                f"  URL: {repo['html_url']}\n"
                f"  Description: {repo['description']}\n"
                f"  Stars: {repo['stargazers_count']}\n"
                f"  Updated At: {repo['updated_at']}\n"
            )
