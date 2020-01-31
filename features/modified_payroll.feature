@mod_payroll
Feature: Modify Employee

    To value Modify Employee
    As an admin with permission to access Payroll
    I want to validate a modified Employee

    Scenario: Modify the field balance
    Given I want to modify the field balance an employee
    When I modify the balance to 500 pesos
    Then I should see a message successfully