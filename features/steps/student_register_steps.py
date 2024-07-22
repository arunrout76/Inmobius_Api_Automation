from behave import *
import requests
from logs import logs_config
from utility import helper

log = logs_config.get_logs()


@given('I send a POST request to "{url}"')
def std_register_url(context, url):
    try:
        context.url = url
    except Exception as e:
        log.error(e)


@given('passing headers for organic registration')
def std_regd_headers(context):
    try:
        context.header={}
        for row in context.table:
            context.header[row['key']] = row['value']
    except Exception as e:
        log.error(e)

@given('passing payload for organic new registration')
def new_registration_payloads(context):
    context.payloads = {}
    for row in context.table:
        context.payloads[row['key']] = helper.convert_value(row['value'])



@given('passing payload for organic exist registration')
def std_regd_payloads(context):
    try:
        context.payloads = {}
        for row in context.table:
            context.payloads[row['key']] = helper.convert_value(row['value'])
    except Exception as e:
        log.error(e)



@given('passing payload for organic registration using exist mail')
def exist_mail_payloads(context):
    context.payloads = {}
    for row in context.table:
        context.payloads[row['key']] = helper.convert_value(row['value'])


@given('passing payload for organic registration using exist Phone Number')
def exist_phone_payload(context):
    context.payloads = {}
    for row in context.table:
        context.payloads[row['key']] = helper.convert_value(row['value'])





@when('I send request as POST method for organic registration')
def type_request(context):
    try:
        context.response = requests.post(context.url, json=context.payloads, headers= context.header)
    except Exception as e:
        log.error(e)

@then('The response status code of organic registration should be "{status_code}"')
def validate_status(context, status_code):
    try:
        log.info(f"printed status_code{status_code}")
        log.info(f"Actual Status Code {context.response.status_code}")
        assert context.response.status_code == int(status_code)
    except Exception as e:
        log.error(e)
        raise

@then('Validate message for organic registration should "{message}"')
def register_message_response(context, message):
    try:
        msg_json = context.response.json()
        actual_msg = msg_json.get('detail','')
        log.info(actual_msg)
        assert actual_msg == message
    except Exception as e:
        log.error(e)
        raise

