# Week 05 - Parameterized and Data-Driven Testing

This week I practiced using pytest parameterization to run the same test logic with multiple sets of input data.

## What I Practiced

- Using `@pytest.mark.parametrize`
- Running one test with multiple input values
- Parameterizing multiple arguments
- Using multiple parameter sets
- Testing normal and invalid inputs
- Using `pytest.raises` with parameterized tests
- Using default parameter IDs
- Creating custom parameter IDs
- Using `pytest.param()` for individual test cases
- Applying `xfail` to a specific parameter case
- Stacking multiple `@pytest.mark.parametrize` decorators

## In-Class Work

### Basic Parameterization

I used parameterization to test even and odd numbers using several values without writing a separate test function for every case.

### Factorial Testing

I tested the factorial function using several input and expected-output pairs with one parameterized test.

### Discount Testing

I tested discount calculations with different prices and discount percentages.

I also tested invalid percentage values and checked that they raise a `ValueError`.

### Parameter IDs

I compared pytest's automatically generated parameter IDs with custom IDs.

Custom IDs made the test output easier to understand because each parameter case could have a meaningful name.

### Parameter-Specific Marks

I used `pytest.param()` to apply an `xfail` mark to one specific parameter case instead of marking the entire test.

### Multiple Parameterization

I practiced stacking multiple `@pytest.mark.parametrize` decorators to generate combinations of different input values.

## What I Learned

Parameterization reduces duplicated test code because the same test logic can be reused with many different inputs.

I also learned that custom IDs make parameterized test results easier to read, and individual parameter cases can have their own marks such as `xfail`.