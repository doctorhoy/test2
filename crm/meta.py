import requests

API_BASE = "https://graph.facebook.com/v17.0"

def fetch_leads(access_token: str, leadgen_form_id: str):
    """Fetch leads for a given lead generation form."""
    url = f"{API_BASE}/{leadgen_form_id}/leads"
    params = {"access_token": access_token}
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()
    return data.get("data", [])
