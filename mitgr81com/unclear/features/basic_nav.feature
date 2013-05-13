Feature: Doing something

Scenario: User can create a secret password - 1
    Given I browse to the "unclear" page
    When I enter "this is a silly password" in the "password" field
        And I enter "here is a passphrase" in the "passphrase" field
        And I click the "Pass It" button
    Then I see the text "Thank you for not sending that password in the clear!"
        And I see the text "You can pass this password by telling the other party to enter your passphrase at:"
        And I capture the unclear URI
