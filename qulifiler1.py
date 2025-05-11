import requests

url = "https://bfhldevapigw.healthrx.co.in/hiring/generateWebhook/PYTHON"

# Request body with your details
data = {
    "name": "Devshrut Daftary",
    "regNo": "933",  # Replace with your registration number
    "email": "devshrutdaftary231088@acropolis.in"
}

# Make the POST request to generate the webhook
response = requests.post(url, json=data)

# Print response to check the webhook and access token
if response.status_code == 200:
    response_data = response.json()
    webhook_url = response_data.get("webhook")
    access_token = response_data.get("accessToken")
    print(f"Webhook URL: {webhook_url}")
    print(f"Access Token: {access_token}")
else:
    print(f"Error: {response.status_code}")
    print(f"Response: {response.text}")