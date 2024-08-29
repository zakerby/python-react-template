#!/bin/bash

# Bash script to test the API
# Usage: ./test_api.sh

# Set the base URL
BASE_URL="http://localhost:8080/api/v1"


# First register a new user
echo "Registering a new user"

# generate a random username
username="user_$(date +%s)"
username_email="user_$(date +%s)@azk.com"
password="password"

register_response=$(curl -s -o /dev/null -w "%{http_code}" -H "Content-Type: application/json" \
     -d "{\"username\": \"$username\", \"password\": \"$password\", \"confirm_password\": \"$password\", \"email\": \"$username_email\"}" \
     -X POST $BASE_URL/auth/register)

if [ "$register_response" -eq 200 ]; then
    echo "Register request was successful."
else
    echo "Request failed with status code $register_response."
    exit 1
fi

# Login with the new user
echo "Logging in with the new user"
login_response=$(curl -s -H "Content-Type: application/json" \
     -d "{\"username\": \"$USERNAME\", \"password\": \"$PASSWORD\"}" \
     -X POST $BASE_URL/auth/login)

# Check if the login_response contains the access_token field
access_token=$(echo $login_response | jq -r '.access_token // empty')

if [ -n "$access_token" ]; then
    echo "Request was successful. Access token: $access_token"
else
    echo "Request failed or access_token not found in the response."
    exit 1
fi



# Clean-up - deleting entities created during the test
echo "Cleaning up..."
delete_user_response=$(curl -s -H "Content-Type: application/json" \
     -d "{\"username\": \"$USERNAME\", \"password\": \"$PASSWORD\"}" \
     -X POST $BASE_URL/auth/login)