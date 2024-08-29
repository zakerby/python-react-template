#!/bin/bash

# Bash script to test the API
# Usage: ./test_api.sh

# Set the base URL
BASE_URL="http://localhost:8080/api/v1"

# Get the folder of the script
SCRIPT_DIR=$(dirname "$0")
SCRIPT_DIR=$(realpath "$SCRIPT_DIR")

# Get the access token by calling the register_and_login.sh script
access_token=$(sh $SCRIPT_DIR/test_auth_api.sh -b $BASE_URL)

if [ -n "$access_token" ]; then
    echo "Access token: $access_token"
    # Continue with the rest of the script
else
    echo "Failed to obtain access token."
    exit 1
fi

# Projects requests
echo "Testing projects API..."
sh "$SCRIPT_DIR/test_project_api.sh" -t $access_token -b $BASE_URL

# Clean-up - deleting entities created during the test
echo "Cleaning up..."
delete_user_response=$(curl -s -o /dev/null -w "%{http_code}" \
                     -H "Authorization: Bearer $access_token" \
                     -X DELETE http://localhost:8080/api/v1/user)
if [ "$delete_user_response" -eq 200 ]; then
    echo "User deleted successfully."
else
    echo "Failed to delete user."
    exit 1
fi