from behave import *
import requests
import json

@given('search api')
def set_impl(context):
    context.url = 'https://api.dictionaryapi.dev/api/v2/entries/en/qa'

@when('I make an http get request')
def step_impl(context):
    context.res = requests.get(context.url)  

@then('must get a reponse with status code 200 and a valid json response data')
def step_impl(context):
    assert context.res.status_code == 200
    response_body = context.res.json()
    assert response_body[0]["word"] == "QA"
    assert isinstance(response_body[0]["phonetics"], list)
    assert response_body[0]["meanings"][0]["partOfSpeech"] == "abbreviation"
    assert response_body[0]["meanings"][0]["definitions"][0]["definition"] == "quality assurance."