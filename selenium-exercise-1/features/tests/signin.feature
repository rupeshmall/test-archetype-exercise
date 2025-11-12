@SMOKE
Feature: signin 
Applicant Registration through Test user Microsoft Login

@Signin
Scenario Outline: Login with Microsoft account for Cubase and Register as an applicant
	Given the user navigates to the application URL
	Given the Microsoft login page is displayed
	When the user enters a valid Microsoft test account username and password
    And clicks on the Sign in button
	Then the user should be redirected to the application home page

	Given the applicant clicks on the Sign in button
	And the applicant is navigated to the applicant Sign in screen
	When the applicant clicks on the Sign up now link
    And enters the valid user details <TestData>
	And clicks on Create button
    Then the applicant should be redirected to the application home page and successfully signed in <TestData>
Examples: 
| TestData |
| User1    |
| User2    |
