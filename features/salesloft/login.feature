@login
Feature: Login Feature
  As a user
  I want to be able to login to salesloftg
  So that i can create people

  @frontend
  Scenario Outline: A valid user can log in to SalesLoft and create a person
    Given I am a registered user in <region>
    When I login to Salesloft
    And I create a new person
    Then the person should be in the database
    Examples:
     |region |
     | us4|
     | eu1|



