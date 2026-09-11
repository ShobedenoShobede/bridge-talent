import json
import os
import random

TEMPLATES = [
    "Hi {username}, I came across your GitHub profile and was impressed by your {stack} work. I work with US tech companies hiring remote engineers from {location}. If you're open to hearing about roles paying $4,000-$8,000/month USD, let me know.",
    "Hey {username}, your {stack} projects look strong. I'm a recruiter placing LatAm/Eastern European developers with US startups. Remote, USD pay, 0-3 hour timezone overlap. Interested in a quick chat?",
    "Hi {username}, I'm building a talent pool of {stack} engineers in {location} for US companies. Pay is $4k-$8k/month USD, fully remote. Worth a 15-minute call?"
]

def generate_outreach():
    with open("candidates.json", "r") as f:
        candidates = json.load(f)
    
    messages = []
    for c in candidates[:20]:  # Limit to 20 per run to avoid spam flags
        template = random.choice(TEMPLATES)
        msg = template.format(**c)
        messages.append({
            "to": c["username"],
            "profile": c["profile"],
            "message": msg
        })
    
    with open("outreach_queue.json", "w") as f:
        json.dump(messages, f, indent=2)
    print(f"Generated {len(messages)} outreach messages")

if __name__ == "__main__":
    generate_outreach()
