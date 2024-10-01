from behave import *
import requests
from logs import logs_config
from utility import helper

log = logs_config.get_logs()

BASE_URL = None
@given('Set the base URL to "{url}"')
def set_base_url(context, url):
    try:
        global BASE_URL
        BASE_URL = url
    except Exception as e:
        log.error(e)


# Create a School
@given('Sent get request "{url}"')
def std_register_url(context, url):
    try:
        context.url = BASE_URL+url
    except Exception as e:
        log.error(e)
@given('passing HEADERS for school registration')
def std_regd_headers(context):
    try:
        context.header={}
        for row in context.table:
            context.header[row['key']] = row['value']
    except Exception as e:
        log.error(e)
@given('passing PAYLOAD for school registration')
def new_registration_payloads(context):
    context.payloads = {}
    for row in context.table:
        key_parts = row['key'].split('.')  # Split the key by '.'
        if len(key_parts) > 1:  # If it's a nested key
            if key_parts[0] not in context.payloads:  # If the root key doesn't exist, create it
                context.payloads[key_parts[0]] = {}
            # Use convert_value from helper.py to convert the value
            context.payloads[key_parts[0]][key_parts[1]] = helper.convert_value(row['value'])
        else:  # If it's a simple key
            context.payloads[row['key']] = helper.convert_value(row['value'])

@when('I send request as POST method for school registration')
def type_request(context):
    try:
        context.response = requests.post(context.url, json=context.payloads, headers= context.header)
    except Exception as e:
        log.error(e)
@then('Response is "{status_code}"')
def validate_status(context, status_code):
    declare_status = False
    try:
        log.info(f"printed status_code {status_code}")
        log.info(f"Actual Status Code {context.response.status_code}")
        log.info(f"Response Message {context.response.json()}")
        if context.response.status_code == int(status_code):
            declare_status = True
    except Exception as e:
        log.error(e)
    assert declare_status is True
        

# Onboard School
@given('onbaord school request url "{url}"')
def school_onboard_url(context, url):
    try:
        context.url = BASE_URL+url
    except Exception as e:
        log.error(e)
@given('passing header for onbaord a school')
def onboard_school_header(context):
    context.header = {}
    try:
        for row in context.table:
            context.header[row['key']] = row['value']
    except Exception as e:
        log.error(e)
@given('passing payloads for onboard a school')
def onboard_school_payload(context):
    context.payloads={}
    try:
        for row in context.table:
            context.payloads[row['key']] = helper.convert_value(row['value'])
    except Exception as e:
        log.error(e)
@when('I send request as POST method for school onbaord')
def onboard_school_request(context):
    try:
        context.response=requests.post(context.url, json=context.payloads, headers=context.header)
    except Exception as e:
        log.error(e)
@then('Response for onbaord a school would be "{status_code}"')
def onboard_school_status(context, status_code):
    declare_status = False
    try:
        log.info(status_code)
        log.info(context.response.status_code)
        log.info(context.response.json())
        if context.response.status_code == int(status_code):
            declare_status = True
    except Exception as e:
        log.error(e)
    assert declare_status is True


#   School Login
@given('Sending Request for "{url}"')
def school_login(context, url):
    try:
        context.url = BASE_URL+url
    except Exception as e:
        log.error(e)

@given('Passing Headers for School Login')
def school_login_headers(context):
    context.header = {}
    try:
        for row in context.table:
            context.header[row['key']] = row['value']
    except Exception as e:
        log.error(e)
@given('Passing Payloads for School Login')
def school_login_payloads(context):
    context.payload = {}
    try:
        for row in context.table:
            context.payload[row['key']] = row['value']
    except Exception as e:
        log.error(e)
@when('Sending Post request for School Login')
def school_login_request(context):
    try:
        context.response = requests.post(context.url, json=context.payload, headers=context.header )
    except Exception as e:
        log.error(e)
@then('Get Response as "{status_code}"')
def school_login_status(context, status_code):
    declare_status = False
    try:
        log.info(status_code)
        log.info(context.response.status_code)
        log.info(context.response.json())
        if context.response.status_code == int(status_code):
            declare_status = True
    except Exception as e:
        log.error(e)
    assert declare_status is True

# Student Login
@given('Requesting for Student Login "{url}"')
def student_login(context, url):
    try:
        context.url = BASE_URL+url
    except Exception as e:
        log.error(e)
@given('Requesting Header for Student Login')
def student_login_header(context):
    context.header = {}
    try:
        for row in context.table:
            context.header[row['key']] = row['value']
    except Exception as e:
        log.error(e)
@given('Requesting Payloads for Student Login')
def student_login_payloads(context):
    context.payloads = {}
    try:
        for row in context.table:
            context.payloads[row['key']] = row['value']
    except Exception as e:
        log.error(e)
@when('Sending for Post Request for Student Login')
def student_login_request_type(context):
    try:
        context.res = requests.post(context.url, headers=context.header, json=context.payloads)
    except Exception as e:
        log.error(e)
@then('Get Response for student login "{status_code}"')
def student_login_status(context, status_code):
    declare_status = False
    try:
        log.info(status_code)
        log.info(context.res.status_code)
        log.info(context.res.json())
        if context.res.status_code == int(status_code):
            declare_status = True
    except Exception as e:
        log.error(e)
    assert declare_status is True


#Student Login with OTP
@given('Requesting for generate OTP "{url}"')
def generate_otp(context, url):
    try:
        context.url = BASE_URL+url
    except Exception as e:
        log.error(e)

@given('Requesting header for generate OTP')
def generate_otp_header(context):
    context.header = {}
    try:
        for row in context.table:
            context.header[row['key']] = row['value']
    except Exception as e:
        log.error(e)
@given('Requesting payloads for generate OTP')
def generate_otp_payload(context):
    context.payload={}
    try:
        for row in context.table:
            context.payload[row['key']] = row['value']
    except Exception as e:
        log.error(e)
@when('Sending for Post Request for generate OTP')
def generate_otp_request_type(context):
    try:
        context.generate_otp = requests.post(context.url, headers=context.header, json=context.payload)
    except Exception as e:
        log.error(e)
@then('Get Response for generate OTP as "{status}"')
def generate_otp_status(context,status):
    try:
        log.info(status)
        log.info(context.generate_otp.status_code)
        log.info(context.generate_otp.json())
        context.generate_otp.status_code == int(status)
    except Exception as e:
        log.error(e)

@given('Requesting for Student Login with OTP "{url}"')
def student_login_otp(context,url):
    try:
        context.url = BASE_URL+url
    except Exception as e:
        log.error(e)
@given('Requesting header for Student Login with OTP')
def student_login_otp_header(context):
    context.header= {}
    try:
        for row in context.table:
            context.header[row['key']]= row['value']
    except Exception as e:
        log.error(e)
@given('Requesting payloads for Student login with OTP')
def student_login_payload(context):
    context.payload={}
    try:
        for row in context.table:
            context.payload[row['key']]=row['value']
    except Exception as e:
        log.error(e)
@when('Sending post request for student login with OTP')
def student_login_otp_request_type(context):
    try:
        context.response = requests.post(context.url, json=context.payload, headers=context.header)
    except Exception as e:
        log.error(e)
@then('will get status code as "{status_code}"')
def student_login_otp_status(context, status_code):
    declare_status = False
    try:
        log.info(status_code)
        log.info(context.response.status_code)
        log.info(context.response.json())
        if context.response.status_code == int(status_code):
            declare_status = True
    except Exception as e:
        log.error(e)
    assert declare_status is True

@given('Requesting for list of Grades "{url}"')
def student_list_grades(context, url):
    try:
        context.url = BASE_URL+url
    except Exception as e:
        log.error(e)

@given('Requesting Header for getting list of Grades')
def list_grades_header(context):
    context.header={}
    try:
        for row in context.table:
            context.header[row['key']] = row['value']
    except Exception as e:
        log.error(e)

@when('Sending Get method')
def list_grade_method(context):
    try:
        context.grade_status = requests.get(context.url, headers=context.header)
    except Exception as e:
        log.error(e)

@then('will get list of grades status code as "{status_code}"')
def list_grade_status(context, status_code):
    # declare_status = False
    try:
        log.info(status_code)
        log.info(context.grade_status.status_code)
        log.info(context.grade_status.json())
        assert context.grade_status.status_code == status_code
            # declare_status = True
    except Exception as e:
        log.error(e)
    # assert declare_status is True

# Forgot password for Student
@given('Rquesting for Forgot Password "{url}"')
def student_forgot_password(context, url):
    try:
        context.url = BASE_URL+url
    except Exception as e:
        log.error(e)
@given('Requesting header for forgot password')
def student_forgot_password_header(context):
    context.header = {}
    try:
        for row in context.table:
            context.header[row['key']] = row['value']
    except Exception as e:
        log.error(e)
@given('Requesting Payloads for Forgot password')
def student_forgot_password_payload(context):
    context.payload={}
    try:
        for row in context.table:
            context.payload[row['key']] = row['value']
    except Exception as e:
        log.error(e)

@when('Sending POST method for forgot password')
def student_forgot_password_request_type(contetx):
    try:
        contetx.response = requests.post(url =contetx.url, json=contetx.payload, headers=contetx.header)
    except Exception as e:
        log.error(e)

@then('Will get status code as "{status}" for forgot password')
def forgot_password_status(context, status):
    declare_status = False
    try:
        log.info(status)
        log.info(context.response.status_code)
        log.info(context.response.json())
        if context.response.status_code == int(status):
            declare_status = True
    except Exception as e:
        log.error(e)
    assert declare_status is True


# Reset Password Default for a user
@given('Reset to default password endpoint "{url}"')
def reset_password_endpoint(context, url):
    try:
        context.url = BASE_URL+url
    except Exception as e:
        log.error(e)
@given('Reset to default password header')
def reset_password_header(context):
    context.header = {}
    try:
        for row in context.table:
            context.header[row['key']] = row['value']
    except Exception as e:
        log.error(e)
@given('Reset to default password payloads')
def reset_password_payload(context):
    context.payload = {}
    try:
        for row in context.table:
            log.info([row['value']])
            context.payload[row['key']] = [row['value']]
    except Exception as e:
        log.error(e)
    log.info(context.payload)
@when('Sending Post Request type for default password')
def reset_password_request_type(context):
    try:
        context.response = requests.post(url=context.url, headers=context.header, json= context.payload)
    except Exception as e:
        log.error(e)
@then('Will get status code as "{status}" for default password')
def reset_password_status(context,status):
    declare_status = False
    try:
        log.info(status)
        log.info(context.response.status_code)
        log.info(context.response.json())
        log.info(context.response.status_code == int(status))
        if context.response.status_code == int(status):
            declare_status = True   
    except Exception as e:
        log.error(e)
    assert declare_status is True










