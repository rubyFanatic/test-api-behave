from behave import *
import requests
import json

@given('Search API Request')
def set_impl(context):
    context.url = 'https://api.dictionaryapi.dev/api/v2/entries/en/qaisnotmagic'

@when('I make a bad http get request')
def step_impl(context):
    context.res = requests.get(context.url)  

@then('must get a reponse with status code 404 and a valid title')
def step_impl(context):
    assert context.res.status_code == 404
    response_body = context.res.json()
    assert response_body["title"] == "No Definitions Found"