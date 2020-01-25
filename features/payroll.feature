Feature: Payroll

    To value Payroll
    As a admin with permission to access Payroll
    I want to validate Payroll flow

    Scenario: New Payroll
        Given I have access to Runa RH as admin
        When I want to create a new Payroll
        And I find the payroll group assigned to me
        And I inform the stardate
        Then the payroll should be generated automatically