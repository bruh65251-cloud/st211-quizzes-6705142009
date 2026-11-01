# Week 07 - Mock Objects and Side Effects

This week I practiced using mock objects to control and simulate the behavior of dependencies during testing.

## What I Practiced

- Creating mock objects with `Mock`
- Calling methods dynamically on mock objects
- Setting fixed results with `return_value`
- Using `side_effect` with different behaviors
- Returning different values from mock calls
- Using functions as mock side effects
- Simulating exceptions with mocks
- Comparing `return_value` and `side_effect`
- Observing how changes to mock behavior affect test results

## In-Class Work

### Mock Basics

I created basic mock objects and observed what happens when methods are called without defining real implementations.

### Return Values

I practiced using `return_value` to make a mocked method return a fixed result every time it is called.

### Side Effect - List

I experimented with changing the values returned by repeated mock calls and observed how the test behavior changed.

### Side Effect - Function

I practiced using function behavior with mocks and compared it with a fixed return value.

### Side Effect - Exception

I used a mock to simulate an exception so that failure behavior could be tested without requiring a real dependency to fail.

### Comparison

I compared fixed mock return values with dynamic behavior where the result can depend on the provided input.

## What I Learned

Mock objects make it possible to isolate the code being tested from other dependencies.

I also learned that `return_value` is useful when the mocked result should stay fixed, while `side_effect` can simulate changing results, functions, and errors. Changing these behaviors also helped me see why a test passes or fails instead of only looking at the final result.