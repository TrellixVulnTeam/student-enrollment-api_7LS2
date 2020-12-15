Feature: Test CRUD methods in student REST API testing framework

Background:
	Given I set student REST API url

Scenario: POST students example
  Given I Set POST students api endpoint
 When I Set HEADER param request content type as "application/json." 
    And Set request Body
 And Send a POST HTTP request 
 Then I receive valid HTTP response code 201
    And Response BODY "POST" is non-empty. 


Scenario: GET students example
  Given I Set GET students api endpoint "1"
  When I Set HEADER param request content type as "application/json." 
	And Send GET HTTP request
  Then I receive valid HTTP response code 200 for "GET." 
	And Response BODY "GET" is non-empty


Scenario: UPDATE students example
  Given I Set PUT students/id api endpoint for "1"
  When I Set Update request Body
	And Send PUT HTTP request
  Then I receive valid HTTP response code 200 for "PUT." 
	And Response BODY "PUT" is non-empty


Scenario: DELETE students example
  Given I Set DELETE students api endpoint for "1"
  When I Send DELETE HTTP request
  Then I receive valid HTTP response code 200 for "DELETE." 