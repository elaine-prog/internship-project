# Created by elain at 6/18/2026
Feature: Reelly mobile login


  Scenario: User can log in and open main menu on mobile web
    Given Open Reelly main page
    When Log in to Reelly
    Then Verify user is logged in
    When Open Main Menu page
    Then Verify Main Menu page opens