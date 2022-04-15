import pytest     
import requests

def call_api(param):
    """
    Executes GET request of the Github User API for specified user.

    Parameters:
        param (dict): dict must contain 'user_id' key with a valid Git user value.
    
    Returns:
        api_resp: GET request response from Github User API
    """
    
    api_url = 'https://api.github.com/users/' + param['user_id']
    api_resp = requests.get(api_url)
    return api_resp

## API Testing

## set valid user_id of your choice
test_param = {
    "user_id": '6wl'
}

## call the github user API 
api_response = call_api(test_param)

def test_api_resp_status():     
    assert api_response.status_code == 200,"Test failed: Should be 200"

def test_api_resp_headers():  
    resp_headers = api_response.headers      
    expected_headers = {'Server': 'GitHub.com', 'Content-Type': 'application/json; charset=utf-8'}     
    for key,value in expected_headers.items():
        assert resp_headers[key] == value,"Test failed: Should be"+value

def test_api_resp_body():  
    expected_resp = {'name':'Gregory Loscombe', 'id': 15330, 'location': 'Manchester', 'public_repos': 7,
    'public_gists': 11, 'followers': 12, 'following': 29} 
  
    resp_body = api_response.json() 
    for key,value in expected_resp.items():
        assert resp_body[key] == value,"Test failed: Should be"+value

