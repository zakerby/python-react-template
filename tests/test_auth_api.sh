#!/bin/bash

# Usage: ./test_auth_api.sh -b BASE_URL

# Parse the command line arguments
while getopts "b:" opt; do
  case $opt in
    b)
      BASE_URL=$OPTARG
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      exit 1
      ;;
    :)
      echo "Option -$OPTARG requires an argument." >&2
      exit 1
      ;;
  esac
done

# Check if BASE_URL is provided
if [ -z "$BASE_URL" ]; then
  echo "Base URL is required. Use -b to provide the base URL."
  exit 1
fi

# Generate a random username
username="user_$(date +%s)"
username_email="user_$(date +%s)@azk.com"
password="password"

register_response=$(curl -s -o /dev/null -w "%{http_code}" -H "Content-Type: application/json" \
     -d "{\"username\": \"$username\", \"password\": \"$password\", \"confirm_password\": \"$password\", \"email\": \"$username_email\"}" \
     -X POST $BASE_URL/auth/register)

if [ "$register_response" -ne 200 ]; then
    echo "Request failed with status code $register_response."
    exit 1
fi

login_response=$(curl -s -H "Content-Type: application/json" \
     -d "{\"username\": \"$username\", \"password\": \"$password\"}" \
     -X POST $BASE_URL/auth/login)

# Check if the login_response contains the access_token field
login_access_token=$(echo $login_response | jq -r '.access_token // empty')

if [ -n "$login_access_token" ]; then
    echo $login_access_token
else
    echo "Request failed or access_token not found in the response."
    exit 1
fi