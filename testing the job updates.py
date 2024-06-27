import requests
import hashlib
import schedule
import time
from datetime import datetime

# List of URLs to monitor
urls = [
    x,
    x,
    
]

# Dictionary to store the previous content hashes
previous_hashes = {}

def get_page_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def hash_content(content):
    return hashlib.md5(content.encode('utf-8')).hexdigest()

def check_for_changes():
    for url in urls:
        content = get_page_content(url)
        if content:
            current_hash = hash_content(content)
            if url in previous_hashes:
                if previous_hashes[url] != current_hash:
                    print(f"Change detected at {url} on {datetime.now()}")
                else:
                    print(f"No change at {url} on {datetime.now()}")
            previous_hashes[url] = current_hash

# Schedule the check_for_changes function to run every day at 9:02 a.m.
schedule.every().day.at("09:02").do(check_for_changes)

print("Monitoring started. Press Ctrl+C to stop.")

# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)
