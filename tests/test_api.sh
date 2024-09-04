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
    echo "Login successful."
    echo "Access token: $access_token"
else
    echo "Failed to obtain access token."
    exit 1
fi

# Projects requests
sh $SCRIPT_DIR/test_project_api.sh -b $BASE_URL -t $access_token

# Clean-up - deleting entities created during the test
sh $SCRIPT_DIR/test_cleanup.sh -b $BASE_URL -t $access_token
