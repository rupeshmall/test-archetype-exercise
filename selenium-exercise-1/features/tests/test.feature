@SMOKE
Feature: test
Google search
@UI
Scenario: Google search
	Given I navigate to google
	And I enter search string "UCL London University"
	When I click on Search button
	Then I should get the expected result "UCL - London's Global University" 

@UITestData
Scenario Outline: Google search with testdata
	Given I navigate to google
	And I enter search string from "<TestData>"
	When I click on Search button
	Then I should get the expected result from "<TestData>"
Examples: 
| TestData |
| UCL      |
| CRM      |