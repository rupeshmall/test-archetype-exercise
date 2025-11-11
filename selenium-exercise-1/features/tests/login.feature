@SMOKE
Feature: login
UCL Login with Test credentials

@Login
Scenario: Login with Microsoft account for Cubase
	Given I navigate to the UCL cubase app portal
	Given Microsoft login page is displayed
	When I enter a valid Microsoft test account username and password
    And I click on the Sign in button
	Then I should be redirected to the application home page