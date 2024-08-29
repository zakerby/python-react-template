#!/bin/bash

# Parse the command line arguments
while getopts "t:b:" opt; do
  case $opt in
    t)
      access_token=$OPTARG
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

# Get projects
echo "Getting projects"
get_projects_response=$(curl -H "Authorization: Bearer $access_token" -X GET http://localhost:8080/api/v1/projects/)
echo $get_projects_response

# Create project

# Delete project