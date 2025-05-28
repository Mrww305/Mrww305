from flask import Flask, render_template
from github_api_client import get_most_starred_repositories, get_latest_updated_repositories

app = Flask(__name__)

@app.route('/')
def index():
    starred_repos = get_most_starred_repositories(count=100)
    latest_repos = get_latest_updated_repositories(count=100)
    return render_template('index.html', starred_repos=starred_repos, latest_repos=latest_repos)

if __name__ == '__main__':
    app.run(debug=True)
