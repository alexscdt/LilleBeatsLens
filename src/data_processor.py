from fetch_data import fetch_data

def process(apiKey: str, apiUrl: str) -> str:
    responses = fetch_data(apiKey, apiUrl)

    if responses.status_code == 200:
        data = responses.json().get('response', {})
        print(data)

        return "Processed data"
    else:
        print(f"Error: {responses.status_code}")
        return "Error"

