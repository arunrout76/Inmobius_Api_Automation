Feature: Onboarding

    Background: 
        Given Set the base URL to "https://adminpreprod.inmobiusinfinitylearn.com"
# School Register
    Scenario: School Register
    Given Sent get request "/api/v1/onboarding/school-register"
    And passing HEADERS for school registration
    |key         |value|
    |accept      |application/json|
    |product-id  |100|
    |tenant-id   |99999|
    |Content-Type|application/json|

    And passing PAYLOAD for school registration
    |key                             |value|
    |primary_contact_info.name       |barc test|
    |primary_contact_info.isd_code   |+91|
    |primary_contact_info.phone      |2364715888|
    |primary_contact_info.designation|School Owner|
    |school_name                     |karunb school|
    |email                           |user23461@example.com|
    |activation_code                 |IM23-296A5D-DD0069|
    |whatsapp_consent                |false|

    When I send request as POST method for school registration
    Then Response is "200"
    
# School Onboard
    Scenario: School Onboard
    Given onbaord school request url "/api/v1/onboarding/school-onboard"
    And passing header for onbaord a school
    |key         |value|
    |accept      |application/json|
    |product-id  |100|
    |tenant-id   |99999|
    |Content-Type|application/json|
    |authorization|Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjYwMzYyODUsImlhdCI6MTcyNTk0OTg4NSwiaWQiOiI2NmRlZTAzMmE0MzEzY2JmNTZlMjA4NWYiLCJzY2hvb2xfaWQiOiJTQ0gxMDAxMDAwMTAyIiwiZmlyc3RfbmFtZSI6ImphYW11IHRlc3QiLCJsYXN0X25hbWUiOm51bGwsInNjaG9vbF9uYW1lIjoiamFtdW4gc2Nob29sIiwiaXNkX2NvZGUiOiIrOTEiLCJSb2xlSWQiOiIyIiwicGhvbmUiOiIxMzUyMTUzMTUzIiwiZW1haWwiOiJqYW1tdUBqa2wuY29tIiwicHJvZHVjdF9pZCI6MTAwLCJ0ZW5hbnRfaWQiOjEwMDAxMCwiYnJhbmNoX2lkIjoyLCJhY2NvdW50X3R5cGUiOiJzY2hvb2wiLCJpc19hY3RpdmUiOnRydWV9.KWhuEFnwGiGEoCF2cvw8GjqCTCeVa4nhzK08fkx498k|

    And passing payloads for onboard a school
    | key                        | value                        |
    | school_type                | Public                       |
    | address                    | Puram                        |
    | country                    | India                        |
    | state                      | KARNATAKA                    |
    | city                       | BENGALURU URBAN              |
    | tier                       | Tier-1                       |
    | school_id                  | SCH1001033                   |
    | pincode                    | 560037                       |
    | fee                        | 10-20K                       |
    | board                      | CBSE                         |
    | branch_name                | KR                           |
    | category                   | D                            |
    | grade_wise                 | false                        |
    | total_student_count        | 50                           |
    | grade_wise_count           | {"nursery":0,"lkg":0,"ukg":0,"grade_1":0,"grade_2":0,"grade_3":0,"grade_4":0,"grade_5":0,"grade_6":0,"grade_7":0,"grade_8":0,"grade_9":0,"grade_10":0,"grade_11":0,"grade_12":0} |
    | primary_contact_name       | bila test                    |
    | primary_contact_designation| Principal                    |
    | primary_contact_phone      | 911564846346                 |
    | primary_contact_email      | bila@jkl.com                 |
    | secondary_contact_info     | null                         |
    When I send request as POST method for school onbaord
    Then Response for onbaord a school would be "200"

# School Login
    Scenario: School Login
    Given Sending Request for "/api/v1/onboarding/school-login"
    And Passing Headers for School Login
    |key         |value|
    |accept      |application/json|
    |product-id  |100|
    |tenant-id   |99999|
    |Content-Type|application/json|

    And Passing Payloads for School Login
    |key     |value     |
    |isd_code|+91       |
    |phone   |1352153153|
    |password|school153 |
    When Sending Post request for School Login
    Then Get Response as "200"

# Student Login
    Scenario: Student Login.
    Given Requesting for Student Login "/api/v1/onboarding/student-login"
    And Requesting Header for Student Login
    |key         |value|
    |accept      |application/json|
    |product-id  |100|
    |tenant-id   |99999|
    |Content-Type|application/json|
    And Requesting Payloads for Student Login
    |key         |value|
    |admission_id|1000108SJZUHHB|
    |password    |QWERTY|
    When Sending for Post Request for Student Login
    Then Get Response for student login "200"

# Generatin OTP
    Scenario: Student Login with OTP
    Given Requesting for generate OTP "/api/generateOTP"
    And Requesting header for generate OTP
    |key         |value|
    |accept      |application/json|
    |product-id  |100|
    |tenant-id   |99999|
    And Requesting payloads for generate OTP
    |key|value|
    |isd_code|+91|
    |phone|2031200518|
    |tenant_id|99999|
    |product_id|100|
    When Sending for Post Request for generate OTP
    Then Get Response for generate OTP as "True"

#  Student Login with OTP
    Given Requesting for Student Login with OTP "/api/v1/onboarding/student-login-otp"
    And Requesting header for Student Login with OTP
    |key         |value|
    |accept      |application/json|
    |product-id  |100|
    |tenant-id   |99999|
    And Requesting payloads for Student login with OTP
    |key     |value|
    |isd_code|+91|
    |phone   |2031200518|
    |otp     |1111|
    When Sending post request for student login with OTP
    Then will get status code as "200"

# List of Grades
    Scenario: list of Student Grades
    Given Requesting for list of Grades "/api/v1/onboarding/student-grades"
    And Requesting Header for getting list of Grades
    |key         |value|
    |accept      |application/json|
    |product-id  |100|
    |tenant-id   |99999|
    When Sending Get method
    Then will get list of grades status code as "200"

# Forgot Password
    Scenario: Forgot password for Student
    Given Rquesting for Forgot Password "/api/v1/onboarding/forget-password/user"
    And Requesting header for forgot password
    |key         |value|
    |accept      |application/json|
    |product-id  |100|
    |tenant-id   |99999|
    And Requesting Payloads for Forgot password
    |key            |value|
    |isd_code       |+91|
    |phone          |2031200518|
    |new_password   |123456|
    When Sending POST method for forgot password
    Then Will get status code as "200" for forgot password

# Reset Password to Default 
    Scenario: Reset password to Default for a user
    Given Reset to default password endpoint "/api/v1/onboarding/reset-password-to-default?api_secret_key=PMA4qXWFZ3uJstb8qtYWVjiFLgtAsm8UULe7cuhGydsdKcwJ"
    And Reset to default password header
    |key         |value|
    |accept      |application/json|
    |product-id  |100|
    |tenant-id   |99999|
    And Reset to default password payloads
    |key          |value|
    |admission_ids|1000108SJZUHHB|
    When Sending Post Request type for default password
    Then Will get status code as "200" for default password





    









    







