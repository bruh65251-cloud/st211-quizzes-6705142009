# Week 09 - Code Coverage and Branch Coverage

This week I practiced measuring how much of the program is exercised by the test suite and identifying logic that is still not tested.

## What I Practiced

- Measuring test coverage
- Comparing incomplete and more complete test suites
- Understanding line coverage
- Understanding branch coverage
- Testing different decision paths
- Testing normal and exceptional behavior
- Using additional tests to improve coverage

## In-Class Work

### Coverage Lab

I used simple access-control and shipping functions to compare different levels of test coverage.

For the access example, I compared a smaller test suite with a more complete set of cases covering different combinations of user roles and active states.

For the shipping example, I tested normal shipping, express shipping, invalid weights, heavy-item surcharges, and free-shipping eligibility.

## What I Learned

A high line-coverage percentage does not always mean that every possible behavior has been tested.

Branch coverage is useful when the program contains conditions because it checks whether different decision paths have been exercised. Adding tests for missing paths makes the test suite more complete.