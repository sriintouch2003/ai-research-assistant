import requests

res = requests.post(
    "http://localhost:8502/research",
    json={
        "query":"What is todays price for DMT6005LPS13?"
    }
).json()

print(res)

res = requests.get(
    "http://localhost:8502"
).json()

print(res)

res = requests.get(
    "http://localhost:8502/serper",
    json={
        "query":"What is todays price for DMT6005LPS13?"
    }
).json()

print(res)

res = requests.post(
    "http://localhost:8502/openai",
    json={
        "query": "What is todays price for BAV99?",
        "prompt": "You are an expert in Test Summarization and help in summarizing the text into simplified tone in fewer words"
    }
).json()

print(res)

#Start Unioorn using -> uvicorn app.main:app --port 8502 