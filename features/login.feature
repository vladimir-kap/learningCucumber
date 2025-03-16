Feature: GitHub Login and Session Management

  Scenario: User logs in and saves session
    Given the user navigates to GitHub login page
    When the user enters valid credentials
    Then the user should be logged in and session should be saved

  Scenario: User uses saved session to access private content
    Given the user has a saved session
    When the user opens GitHub with the saved session
    Then the user should see the dashboard content