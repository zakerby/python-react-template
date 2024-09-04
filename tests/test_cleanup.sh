#!/bin/bash

# Usage: ./test_cleanup.sh -b BASE_URL

# Parse the command line arguments
while getopts "t:b:" opt; do
    case $opt in
    b)
        BASE_URL=$OPTARG
        ;;
    t)
        ACCESS_TOKEN=$OPTARG
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

# Clean-up - deleting entities created during the test
echo "Cleaning up..."
delete_user_response=$(curl -s \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $ACCESS_TOKEN" \
    -X DELETE $BASE_URL/user)

echo $delete_user_response

# Check the response status
delete_user_response_status=$(echo $delete_user_response | jq -r '.status // empty')

if [ -z "$delete_user_response_status" ]; then
    echo "Request failed with status $delete_user_response_status."
    exit 1
else 
    echo "Request successful."
fi

