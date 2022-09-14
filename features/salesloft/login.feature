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



#    @melody @kafka @keyscore
#    Scenario: A user login in an places a call or whatever
#      Given I am a registered user
#      When I login to Salesloft in "us3"
#      And I navigate to Cadence
#      And I place a phone call to test number
#      Then it should connect to a keyscore router
#      And some events should show up in Kafka


