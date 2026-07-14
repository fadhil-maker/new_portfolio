import urllib.request
import json
import sys

try:
    url = 'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=https://muhammedfadhil.vercel.app/&strategy=mobile'
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    
    print("Score:", data['lighthouseResult']['categories']['performance']['score'] * 100)
    print("FCP:", data['lighthouseResult']['audits']['first-contentful-paint']['displayValue'])
    print("LCP:", data['lighthouseResult']['audits']['largest-contentful-paint']['displayValue'])
    print("\n--- WARNINGS ---")
    for audit_id, audit in data['lighthouseResult']['audits'].items():
        score = audit.get('score')
        if score is not None and score < 1:
            print(f"{audit.get('title')} (Score: {score}): {audit.get('displayValue', '')}")
except Exception as e:
    print("Error:", e)
