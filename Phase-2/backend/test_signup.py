#!/usr/bin/env python3
"""Test signup endpoint directly"""
import requests
import json

# Test data
data = {
    "email": "test@example.com",
    "password": "test1234",
    "name": "Test User"
}

print("Testing signup endpoint...")
print(f"URL: http://localhost:8000/api/auth/signup")
print(f"Data: {json.dumps(data, indent=2)}")
print("-" * 50)

try:
    response = requests.post(
        "http://localhost:8000/api/auth/signup",
        json=data,
        headers={"Content-Type": "application/json"}
    )

    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")

    if response.status_code == 201:
        print("\n✅ SUCCESS! User created successfully!")
        result = response.json()
        print(f"Token: {result['token'][:50]}...")
        print(f"User: {result['user']}")
    else:
        print(f"\n❌ FAILED with status {response.status_code}")

except Exception as e:
    print(f"\n❌ ERROR: {e}")
