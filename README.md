# Urban Routes End-to-End UI Test Automation

## Objective

To automate end-to-end testing of the Urban Routes ride-hailing application, ensuring the reliability of the core taxi booking flow against regression errors and ensuring a smooth user experience across critical interactions.

## Defining the problem & Business Impact

In a competitive ride-hailing platform like Urban Routes, any UI disruption during address selection, SMS verification, payment authorization, or driver matching directly causes abandoned requests, lost bookings, and frustrated users leaving the app. 

Relying only on manual regression testing for multi-step booking flows is slow, repetitive, and prone to human error. This delays the release of new features and increases the risk of releasing broken payment or driver-matching features to users that do not function correctly.

## What I Did

- **End-to-End Funnel Automation**: Built a comprehensive automated test suite covering the complete critical path: origin/destination setup, Comfort tariff selection, phone number entry, SMS authorization code handling, credit card binding, driver messaging, and custom add-on requests (blanket, tissues, ice cream).

- **Scalable Architecture (POM)**: Implemented the Page Object Model (POM) design pattern to separate test logic from UI locators, making the scripts easier to maintain when front-end elements change.

- **Synchronization & Stability**: Implemented explicit waits (WebDriverWait) to reliably handle dynamic UI elements, such as SMS countdown timers and driver-search modal popups.

- **Version Control**: Managed iterative script development and project structure using Git and GitHub.


## Technologies Used

Python · Pytest · Selenium WebDriver · PyCharm · Git · GitHub

## Results & Business Implications

- **100% Pass Rate Across the Core Booking journey (Verified Result)**: Successfully validated that all sequential steps of the Comfort-tier taxi booking process execute without functional blockers, UI freezes, or data-loss errors.

   - Business Implication: Confirms that the primary revenue flow (from route calculation to payment binding and order dispatch) is stable and ready for release, minimizing the risk of lost rides or failed payment conversions.

- **Modular, Maintainable Test Coverage (Verified Result)**: Structured locators and actions using POM with explicit synchronization, achieving reliable test runs without intermittent timing failures.

   - Business Implication: Reduces regression testing turnaround time from manual hours to seconds, enabling the engineering team to deploy UI updates faster while maintaining high release confidence.


## Strategic Recommendations & Product Decision Support

Based on the test automation findings and observed UI behavior (such as dynamic modals and timer dependencies), the following actions are recommended to protect product quality:

1. **Prioritize Explicit Waits on Critical User Popups (User Experience Protection):**

   - Action: Keep explicit waits (WebDriverWait) consistently applied across all modal overlays and SMS countdown timers.

   - Product Decision Enabled: Helps the engineering team prevent false errors or UI freezes during peak usage, allowing Product Managers to safely release updates without risking abandoned bookings caused by slow-loading popups.

2. **Keep Page Object Models (POM) Updated Alongside UI Changes (Release Speed):**

   - Action: Maintain web element locators modular and updated in their respective page classes whenever front-end layouts evolve.

   - Product Decision Enabled: Gives QA and Engineering leads a fast, reliable way to validate new design changes before launch, avoiding delays in release schedules caused by broken test scripts.

   
3. **Automate Test Data Generation for Payment & Phone Validations (Coverage Expansion):**

    - Action: Replace hardcoded test data with dynamic test data generators (such as Python libraries to create unique mock phone numbers and test credit cards for each run).

     - Product Decision Supported: Ensures test results remain accurate and independent, giving the product team confidence to expand automated testing to additional ride options (such as Economy or Business) without risking duplicate data errors

 ## Learnings

- **Business-Focused Automation Strategy**: Learned to design test automation focused on high-risk, critical user paths—such as validating credit card binding and SMS verification first—because errors in these steps directly prevent customers from completing a ride.
- **Handling Dynamic UI Elements**: Learned to manage asynchronous UI components like modal popups and countdown timers in Selenium, preventing false test failures caused by slow loading times
- **Version Control & Collaboration**: Practiced structured version control by organizing commits, managing project updates, and maintaining clean documentation in GitHub.




## Test Evidence

#### Video Demonstration — Full automation Taxi Booking Flow
Real-time automated execution of the Urban Routes booking journey, verifying uninterrupted data flow across address inputs, SMS authentication, credit card linking, and driver assignment modals.

https://github.com/user-attachments/assets/16359309-0d3b-453c-99aa-5c1513be58a4



--------------------------------------------------------------------------------
# Instructions on how to run the tests
    ## Clone the repository
    ### git clone
## Install the dependencies
    ### pip install selenium pytest
## Run the tests
    ### python -m pytest test/
