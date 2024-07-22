Feature: Student Login

    Scenario: Student Login with Correct Credentials
    Given I send a GET request to "https://gatewayapi.devinfinitylearn.in/api/v1/user/login"
    And passing headers
    |key         |value|
    |accept      |application/json|
    |product-id  |100|
    |tenant-id   |99999|
    |Content-Type|application/json|

    And passing payload
    |key         |value|
    |admission_id|13907DSZS|
    |password    |QWERTY|

    When I send request as POST method

    Then The response status code should be 200
    And Validate admission_id "13907DSZS"



    Scenario: Student Login with Wrong Credentials
    Given I send a GET request to "https://gatewayapi.devinfinitylearn.in/api/v1/user/login"
    And passing headers
    |key         |value|
    |accept      |application/json|
    |product-id  |100|
    |tenant-id   |99999|
    |Content-Type|application/json|

    And Passing Incorrect Payload
    |key         |value|
    |admission_id|13907DSZS|
    |password    |123456|

    When I send request as POST method

    Then The response status code should be 400
    And In Reponse get a message as "Incorrect Password"
