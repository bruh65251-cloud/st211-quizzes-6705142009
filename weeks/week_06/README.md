# Week 06 - Data-Driven Testing, Parameterized Fixtures, and Mocking

This week I practiced using external test data, parameterized fixtures, and an introduction to mocking.

## What I Practiced

- Loading test cases from JSON files
- Loading test data from CSV files
- Using external data with `@pytest.mark.parametrize`
- Creating parameterized fixtures with `params`
- Accessing fixture parameters through `request.param`
- Using `yield` for fixture setup and teardown
- Running the same tests with different browser and database values
- Understanding problems caused by unpredictable dependencies
- Using `patch()` to control dependency return values during testing

## In-Class Work

### Data-Driven Lab

I used JSON and CSV files as external sources for test data.

The JSON exercise loaded input and expected values and used them in a parameterized uppercase test.

The CSV exercise loaded usernames, passwords, and expected login results to test a login validation function.

### Parameterized Fixture Lab

I practiced parameterizing fixtures with different values.

The exercises reused the same test logic with multiple browser and database types instead of creating separate tests for each one.

I also practiced using `yield` to separate fixture setup and teardown behavior.

### Mock Introduction Lab

I tested a weather function that depends on a randomly generated temperature.

Because the result can change randomly, I practiced using `patch()` to control the temperature and test specific weather results without depending on the random value.

## What I Learned

External test data makes it easier to separate test cases from test logic. Parameterized fixtures also allow the same setup and tests to be reused with different environments.

I also learned why unpredictable dependencies can make tests unreliable and how mocking can give the test control over those dependencies.