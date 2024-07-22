from behave import *
import requests
from logs import logs_config
import json


log = logs_config.get_logs()

@given('I send a GET request to "{url}"')
def send_url(context, url):
    try:
        context.url = url
    except Exception as e:
        log.error(e)

@given('passing headers')
def pass_headers(context):
    try:
        context.header= {}
        for row in context.table:
            context.header[row['key']] = row['value']
        log.info(f"Headers: {context.header}")
    except Exception as e:
        log.error(e)

@given('passing payload')
def pass_payload(context):
    try:
        context.payloads = {}
        for row in context.table:
            context.payloads[row['key']] = row['value']
        log.info(f"payload :{context.payloads}")
    except Exception as e:
        log.error(e)


@given('Passing Incorrect Payload')
def pass_payload(context):
    try:
        context.payloads = {}
        for row in context.table:
            context.payloads[row['key']] = row['value']
        log.info(f"incorrect payload: {context.payloads}")
    except Exception as e:
        log.error(e)


@when('I send request as POST method')
def send_request(context):
    try:
        context.response = requests.post(context.url, json=context.payloads, headers=context.header)
    except Exception as e:
        log.error(e)        

@then('The response status code should be {status_code}')
def validate_response(context, status_code):
    log.info(f"Status_code: {context.response.status_code}")
    assert context.response.status_code == int(status_code)


@then('Validate admission_id "{actual_id}"')
def validate_admission_id(context,actual_id):
    json_response = context.response.json()
    log.info(f"Json Response: {json_response}")
    getting_id = json_response['user']['admission_id']
    log.info(f"getting_id: {getting_id}")
    assert getting_id == actual_id

@then('In Reponse get a message as "{message}"')
def incorrect_credential_message(context, message):
    incorrect_cred = context.response.json()
    actual_message = incorrect_cred.get('detail','')
    log.info(f"Message for Incorrect Password: {actual_message}")
    assert actual_message == message





