Feature: Passwords can be created and retrieved

Scenario: User can create a secret password - 1
    Given I browse to the "unclear" page
    When I enter "this is a silly password" in the "passphrase" field
        And I enter "here is a passphrase" in the "unlock_phrase" field
        And I click the "Pass It" button
    Then I see the text "Thank you for not sending that password in the clear!"
        And I see the text "You can pass this password by telling the other party to enter your passphrase at:"
        And I capture the unclear URI
    When I browse to the last unclear page
    Then I see the text "This passphrase may be retrieved 1 more time."

Scenario: User can create a secret password that can be accessed multiple times - 2
    Given I browse to the "unclear" page
        And I enter "this is an optimal passphrase" in the "passphrase" field
        And I enter "correct horse battery staple" in the "unlock_phrase" field
    When I enter "5" in the "max_access" field
        And I click the "Pass It" button
        And I capture the unclear URI
        And I browse to the last unclear page
    Then I see the text "This passphrase may be retrieved 5 more times."

Scenario: A passphrase, once stored, can be later retrieved - 3
    Given I browse to the "unclear" page
        And I enter "bob's your passphrase" in the "passphrase" field
        And I enter "but weave is your salvation" in the "unlock_phrase" field
        And I click the "Pass It" button
        And I capture the unclear URI
        And I browse to the last unclear page
        And "bob's your passphrase" is not in the "passphrase" field
    When I enter "but weave is your salvation" in the "unlock_phrase" field
    Then "bob's your passphrase" is in the "passphrase" field
