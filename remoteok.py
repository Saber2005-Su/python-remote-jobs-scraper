import requests
import csv

url = "https://remoteok.com/remote-jobs.json"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
data = response.json()

csv_filename = "all_remote_jobs.csv"

with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Position', 'Company', 'Location', 'Apply URL', 'Date', 'Tags Count'])
    
    
    for job in data:
        writer.writerow([
            job.get('position', ''),
            job.get('company', ''),
            job.get('location', ''),
            job.get('apply_url', ''),
            job.get('date', ''),
            len(job.get('tags', []))
        ])

print(f"✅ Successfully saved {len(data)} jobs to '{csv_filename}'")