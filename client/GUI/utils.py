import json

with open('../questionary_data.json', mode='r', encoding='utf-8') as f:
# with open('microservices/client/questionary_data.json', mode='r') as f:
    QUESTIONARY = json.load(f)['questions']
