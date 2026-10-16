# Urban Routes Web Application Test Automation

## Objective

To automate end-to-end testing of the Urban Routes ride-hailing application, ensuring the complete taxi booking flow works correctly through UI automation.

## Defining the problem

Manual testing of multi-step user flows is time-consuming and prone to human error. Urban Routes required automated tests to validate a complex booking process involving multiple UI interactions across different form fields, modals, and dynamic content.

## What I Did

- *Built an automated test suite covering the full taxi booking flow:* verified setting pickup and dropoff addresses, selecting the Comfort fare, entering a phone number, adding a credit card as a payment method, writing a message to the driver, requesting additional items (blanket, tissues, ice cream), confirming that the taxi assignment modal and driver information loaded correctly upon booking completion.
- Defined locators and methods using the Page Object Model pattern to keep the code organized and reusable.
- Verified that the driver search modal appeared correctly and that driver information loaded upon booking completion.
- Pushed the project to a GitHub repository and wrote a README with project description, technologies used, and instructions to run the tests.

## Technologies Used

Python · Pytest · Selenium WebDriver · PyCharm · Git · GitHub

## Results and Learnings

- Gained hands-on experience structuring automated tests using Page Object Model.
- Learned to handle dynamic UI elements such as modals and countdown timers in Selenium.
- Practiced version control workflow by committing and pushing a complete project to GitHub

## Test Evidence

[Video of Urban Routes test automation](https://www.loom.com/share/32db248eddb34a5ab5a7212dc213644b)

--------------------------------------------------------------------------------
# Instructions on how to run the tests
    ## Clone the repository
    ### git clone
## Install the dependencies
    ### pip install selenium pytest
## Run the tests
    ### python -m pytest test/
