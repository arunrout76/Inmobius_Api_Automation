Feature: Organic Registration for Student

    Scenario: Register a Organic New Student.
    Given I send a POST request to "https://gatewayapi.devinfinitylearn.in/api/v1/user/register"
    And passing headers for organic registration
    |key         |value|
    |accept      |application/json|
    |product-id  |100|
    |tenant-id   |99999|
    |Content-Type|application/json|
    |platform    |web|
    And passing payload for organic new registration
    |key                  |value|
    |first_name           |sahi|
    |last_name            |test|
    |isd_code             |+91|
    |phone                |1119998884|
    |email                |sahib@uio.com|
    |role_ids             |[1]|
    |password             |QWERTY|
    |grade_id             |8|
    |school_id            |SCH10013149|
    |registration_source  |organic|

    When I send request as POST method for organic registration
    Then The response status code of organic registration should be "201"
    And Validate message for organic registration should "User registered"


    Scenario: Register a Organic Exist Student.
    Given I send a POST request to "https://gatewayapi.devinfinitylearn.in/api/v1/user/register"
    And passing headers for organic registration
    |key         |value|
    |accept      |application/json|
    |product-id  |100|
    |tenant-id   |99999|
    |Content-Type|application/json|
    |platform    |web|
    And passing payload for organic exist registration
    |key                  |value|
    |first_name           |sahilb|
    |last_name            |test|
    |isd_code             |+91|
    |phone                |1256156661|
    |email                |sahilrp@uio.com|
    |role_ids             |[1]|
    |password             |QWERTY|
    |grade_id             |8|
    |school_id            |SCH10013149|
    |registration_source  |organic|

    When I send request as POST method for organic registration
    Then The response status code of organic registration should be "409"
    And Validate message for organic registration should "User already exist"

 

    Scenario: Register a Organic Student for Exist mail
    Given I send a POST request to "https://gatewayapi.devinfinitylearn.in/api/v1/user/register"
    And passing headers for organic registration
    |key         |value|
    |accept      |application/json|
    |product-id  |100|
    |tenant-id   |99999|
    |Content-Type|application/json|
    |platform    |web|
    And passing payload for organic registration using exist mail
    |key                  |value|
    |first_name           |sahilm|
    |last_name            |test|
    |isd_code             |+91|
    |phone                |1256156670|
    |email                |mahi@uio.com|
    |role_ids             |[1]|
    |password             |QWERTY|
    |grade_id             |8|
    |school_id            |SCH10013149|
    |registration_source  |organic|
    When I send request as POST method for organic registration
    Then The response status code of organic registration should be "409"
    And Validate message for organic registration should "Similar users found"


    Scenario: Register a Organic Student for Exist Phone Number
    Given I send a POST request to "https://gatewayapi.devinfinitylearn.in/api/v1/user/register"
    And passing headers for organic registration
    |key         |value|
    |accept      |application/json|
    |product-id  |100|
    |tenant-id   |99999|
    |Content-Type|application/json|
    |platform    |web|
    And passing payload for organic registration using exist Phone Number
    |key                  |value|
    |first_name           |sahilm|
    |last_name            |test|
    |isd_code             |+91|
    |phone                |1256156670|
    |email                |nahi@uio.com|
    |role_ids             |[1]|
    |password             |QWERTY|
    |grade_id             |8|
    |school_id            |SCH10013149|
    |registration_source  |organic|
    When I send request as POST method for organic registration
    Then The response status code of organic registration should be "409"
    And Validate message for organic registration should "Similar users found"