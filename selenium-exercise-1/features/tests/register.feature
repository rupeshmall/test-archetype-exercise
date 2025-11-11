@SMOKE
Feature: register
Applicant Registration through Test user Microsoft Login

@RegisterTestData
Scenario Outline: Register for UCL portal as an applicant with testdata 
	Given I click on the Sign in button
	And I am navigated to the applicant Sign in screen
	When I click on the Sign up now link
	Then I enter the my valid details such as "<TestData>"
    And I click on Create button
    Then I should be redirected to the application home page and succesfully signed in
Examples: 
| TestData |
| User1    |
