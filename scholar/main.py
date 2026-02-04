from scholarly import scholarly
import json
import os

# Create a proxy generator
pg = ProxyGenerator()
pg.FreeProxies() # This grabs a list of free proxies to bypass the block
scholarly.use_proxy(pg)

# 1. Fetch author data
print("Connecting to Google Scholar...")
author = scholarly.search_author_id(os.environ['GOOGLE_SCHOLAR_ID'])
print(f"Found author: {author.get('name')}")

print("Fetching indices...")
scholarly.fill(author, sections=['basics', 'indices'])
print("Data retrieved successfully.")

# 2. Extract the specific numbers you want
total_citations = author.get('citedby', 0)
h_index = author.get('hindex', 0)
i10_index = author.get('i10index', 0)

# 3. Create a clean JSON for your website
stats = {
    "citations": total_citations,
    "hindex": h_index,
    "i10index": i10_index
}

os.makedirs('results', exist_ok=True)
with open('results/gs_stats.json', 'w') as f:
    json.dump(stats, f)

# 4. Create the Shields.io badge JSON for h-index specifically
hindex_badge = {
  "schemaVersion": 1,
  "label": "h-index",
  "message": str(h_index),
  "color": "orange"
}
with open('results/gs_hindex_shieldsio.json', 'w') as f:
    json.dump(hindex_badge, f)
