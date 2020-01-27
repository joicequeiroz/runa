Feature: Login

    To value invalid Login
    As an admin
    I want to validate invlaid Login

    Scenario Outline: Invalid Login
        Given I open the "<url>" url
        When I go to "Login" page
        When I do the invalid login with credentials "<email>" and "<password>"
        Then I should not be logged in
        Examples:
            | url                               | email                 | password               |
            | http://automation.runademos.info/ | "joice.qa@runahr.com" | "SuperSecretPassword!" |