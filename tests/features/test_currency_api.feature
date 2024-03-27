Feature: Currency API Validations
    API Tests related to currency api

    @successful
    Scenario: Happy Path Scenario for currency api
#        Given The API endpoint for currency "INR"
        When I execute get currency call with "INR"
        Then I verify status code as 200
        And I validate the country with "INR" currency as "INDIA"
