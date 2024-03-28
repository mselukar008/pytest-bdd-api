Feature: Currency API Validations
    API Tests related to currency api

    @happy
    Scenario: Happy Path Scenario for currency api
        When I execute get currency call with "INR"
        Then I verify status code as "200"
        And I validate the country with "INR" currency as "India"

     @unhappy
    Scenario: UnHappy Path Scenario for currency api
        When I execute get currency call with "DUMMY"
        Then I verify status code as "404"
        And I verify response message as "Not Found"