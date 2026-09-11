import os
import requests
import json
from datetime import datetime

# --- SEARCH QUERIES (targeting LatAm + Eastern Europe) ---
LOCATIONS = [
    "Buenos Aires", "Mexico City", "Bogota", "Santiago", "Lima", "Sao Paulo",
    "Warsaw", "Bucharest", "Kyiv", "Sofia", "Budapest", "Prague"
]

STACKS = ["Python", "JavaScript", "React", "Node.js", "TypeScript", "Go"]

def search_github_devs():
    """Search GitHub for developers in target regions with target stacks."""
    headers = {"Accept": "application/vnd.github.v3+json"}
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"token {token}"
    
    candidates = []
    for loc in LOCATIONS:
        for stack in STACKS:
            query = f"location:{loc} language:{stack}"
            url = f"https://api.github.com/search/users?q={query}&per_page=5"
            try:
                r = requests.get(url, headers=headers, timeout=15)
                if r.status_code == 200:
                    for user in r.json().get("items", []):
                        candidates.append({
                            "username": user["login"],
                            "location": loc,
                            "stack": stack,
                            "profile": user["html_url"],
                            "discovered": datetime.now().isoformat()
                        })
            except Exception as e:
                print(f"Error searching {loc}/{stack}: {e}")
    
    return candidates

def save_candidates(candidates):
    """Save to a JSON file for the outreach agent to pick up."""
    with open("candidates.json", "w") as f:
        json.dump(candidates, f, indent=2)
    print(f"Saved {len(candidates)} candidates")

if __name__ == "__main__":
    devs = search_github_devs()
    save_candidates(devs)
