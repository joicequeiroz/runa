@valid_login
Feature: Login

    To value Login
    As an admin
    I want to validate Login

    Scenario Outline: Valid Login
        Given I open the "<url>" url
        When I go to "Login" page
        When I do the valid login with credentials "<email>" and "<password>"
        Then I should be logged in
        Examples:
            | url                               | email                          | password |
            | http://automation.runademos.info/ | producto+automation@runahr.com | runahr   |
