#!/bin/bash

# Parse the command line arguments
while getopts "t:b:" opt; do
  case $opt in
    t)
      ACCESS_TOKEN=$OPTARG
      ;;
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

# Check parameters
if [ -z "$ACCESS_TOKEN" ]; then
  echo "Access token is required. Use -t to provide the access token."
  exit 1
fi

if [ -z "$BASE_URL" ]; then
  echo "Base URL is required. Use -b to provide the base URL."
  exit 1
fi

echo "Testing projects API..."

# Create project
echo "Creating project"
echo "curl -s -H "Authorization Bearer: $ACCESS_TOKEN" -H "Content-Type: application/json" -X POST $BASE_URL/projects -d '{"name": "test_project"}'"
create_project_response=$(curl -s -H "Authorization: Bearer $ACCESS_TOKEN" -H "Content-Type: application/json" -X POST $BASE_URL/projects -d '{"name": "test_project"}')

# Check the response status code
create_project_response_status=$(echo $create_project_response | jq -r '.status // empty')
create_project_response=$(echo $create_project_response | jq -r '.status_code // empty')

if [ -n "$create_project_response_status" ]; then
    echo "Request failed with status $create_project_response_status."
    exit 1
else
    echo "Request successful."
fi

# Get projects
echo "Getting projects"
get_projects_response=$(curl -s -H "Authorization: Bearer $ACCESS_TOKEN" -X GET $BASE_URL/projects/)
echo $get_projects_response


# Delete project