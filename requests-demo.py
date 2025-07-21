import requests
import json
import random
import string
from dotenv import load_dotenv
import os

# Load token from .env if available
load_dotenv()
auth_token = os.getenv("AUTH_TOKEN") or '2c80e9f0bc9d735b4c308b8c58d693f85a986b3c050dc9a2831886d8040ef315'
base_url = "https://gorest.co.in"


def generate_random_email():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"{username}@auto.com"


def get_request():
    url = base_url + '/public/v2/users'
    headers = {
        'Authorization': f'Bearer {auth_token}',
        'Content-Type': 'application/json'
    }

    response = requests.get(url, headers=headers)
    print(f"GET Status Code: {response.status_code}")
    if response.status_code == 200:
        json_str = json.dumps(response.json(), indent=4)
        print('✅ JSON GET response:\n', json_str)
    else:
        print("❌ Failed to fetch users\n", response.text)


def post_request():
    url = base_url + '/public/v2/users'
    email = generate_random_email()
    print(f"Generated email: {email}")

    headers = {
        'Authorization': f'Bearer {auth_token}',
        'Content-Type': 'application/json'
    }

    data = {
        'name': 'RK Automation',
        'email': email,
        'gender': 'male',
        'status': 'active'
    }

    response = requests.post(url, json=data, headers=headers)
    print(f"POST Status Code: {response.status_code}")
    print(f"POST Response Body:\n{response.text}")

    assert response.status_code == 201, "❌ Failed to create user"
    json_data = response.json()
    print('✅ JSON POST response:\n', json.dumps(json_data, indent=4))
    return json_data['id']


def put_request(user_id):
    url = f"{base_url}/public/v2/users/{user_id}"
    print(f"PUT URL: {url}")

    headers = {
        'Authorization': f'Bearer {auth_token}',
        'Content-Type': 'application/json'
    }

    data = {
        'name': 'RK Automation Labs',
        'email': generate_random_email(),
        'gender': 'male',
        'status': 'active'
    }

    response = requests.put(url, json=data, headers=headers)
    print(f"PUT Status Code: {response.status_code}")
    print(f"PUT Response Body:\n{response.text}")

    assert response.status_code == 200, "❌ Failed to update user"
    json_data = response.json()
    print('✅ JSON PUT response:\n', json.dumps(json_data, indent=4))


def delete_request(user_id):
    url = f"{base_url}/public/v2/users/{user_id}"
    print(f"DELETE URL: {url}")

    headers = {
        'Authorization': f'Bearer {auth_token}',
        'Content-Type': 'application/json'
    }

    response = requests.delete(url, headers=headers)
    print(f"DELETE Status Code: {response.status_code}")

    assert response.status_code == 204, "❌ Failed to delete user"
    print("✅ User deleted successfully")


# === Run Full Lifecycle ===
if __name__ == "__main__":
    print("🚀 Creating user...")
    user_id = post_request()

    print("\n✏️ Updating user...")
    put_request(user_id)

    print("\n🧹 Deleting user...")
    delete_request(user_id)

    print("\n📋 Listing users...")
    get_request()
