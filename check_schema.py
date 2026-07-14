import json

with open('data.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

models = {}

for item in data:
    model_name = item['model']
    if model_name not in models:
        models[model_name] = set()
    for key in item['fields'].keys():
        models[model_name].add(key)

for model, keys in models.items():
    print(f"\n--- {model} ---")
    for key in sorted(keys):
        print(f"  - {key}")
