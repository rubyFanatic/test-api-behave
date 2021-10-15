Feature: Search API REST call 

  Scenario: Users should be able to make GET requests successfully and get desired data as response
    Given Search API
    When I make an http get request
    Then must get a reponse with status code 200 and a valid json response data

  Scenario: Upon user passing bad data request, api should respond with right message 
    Given Search API Request
    When I make a bad http get request
    Then must get a reponse with status code 404 and a valid title