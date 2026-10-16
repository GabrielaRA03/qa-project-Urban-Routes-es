# Urban Routes Web Application Test Automation

## Objective

To automate end-to-end testing of the Urban Routes ride-hailing application, ensuring the reliability of the core taxi booking flow through UI automation and safeguarding critical business interactions from regression errors.

## Defining the problem

Manual testing of multi-step booking flows is time-consuming, repetitive, and susceptible to human oversight. In a ride-hailing platform like Urban Routes, any disruption during address selection, payment authorization, or driver assignment directly impacts user conversion and retention. 

Automating this complex flow mitigates business risks by validating critical UI components, dynamic countdown timers, modal overlays, and form submissions in seconds.

## What I Did

- Built an automated test suite covering the full booking lifecycle: address setup, Comfort fare selection, phone number entry, credit card binding, driver messaging, and add-on requests (blanket, tissues, ice cream).
- Applied the POM design pattern to separate test logic from page locators, improving script maintainability and code reusability.
- Implemented explicit waits to manage dynamic UI elements, such as authorization SMS timers and driver search modal popups.
- Managed project iterations using Git/GitHub workflow.

## Technologies Used

Python · Pytest · Selenium WebDriver · PyCharm · Git · GitHub

## Results and Learnings

- **100% Test Pass Rate:** Successfully automated and validated the entire end-to-end taxi booking flow in Urban Routes, including location setup, Comfort fare selection, driver messaging, and item requests.
- *Code Reliability:* Achieved clean test execution using the Page Object Model (POM) pattern, ensuring reusable and scalable UI/API automation scripts
- Learned to handle dynamic UI elements such as modals and countdown timers in Selenium.
- Learned to design test automation strategies focused on high-risk, user-critical business paths.
- Practiced version control workflow by committing and pushing a complete project to GitHub

## Test Evidence

#### Video Demonstration — Full automation Taxi Booking Flow
The video below demonstrates the automated execution of the complete Urban Routes booking journey. It verifies that form field submissions, credit card payment addition, SMS verification code handling, and driver search modals load smoothly without breaking the user experience.

https://github.com/user-attachments/assets/16359309-0d3b-453c-99aa-5c1513be58a4



--------------------------------------------------------------------------------
# Instructions on how to run the tests
    ## Clone the repository
    ### git clone
## Install the dependencies
    ### pip install selenium pytest
## Run the tests
    ### python -m pytest test/
