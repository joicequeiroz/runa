@payroll
Feature: Payroll

    To value Payroll
    As an admin with permission to access Payroll
    I want to validate Payroll flow

    Scenario Outline:  New Payroll
        Given I open the "<url>" url
        When I go to "Login" page
        And I do the valid login with credentials "<email>" and "<password>"
        And I want to create a new Payroll
        And I find the payroll group assigned to me
        And I inform the stardate
        Then the payroll should be generated automatically
        Examples:
            | url                               | email                          | password |
            | http://automation.runademos.info/ | producto+automation@runahr.com | runahr   |