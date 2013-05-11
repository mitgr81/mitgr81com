Feature: Doing something

Scenario: User can create a secret password
    Given I browse to the "password passer" page
    When I enter "this is a silly password" in the "Password" field
        And I enter "here is a passphrase" in the "Passphrase" field
        And I click the "Pass it" button