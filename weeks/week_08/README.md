# Week 08 - Mocking and Patching

This week I practiced using mocks and patching to control dependencies and verify how mocked functions are used during testing.

## What I Practiced

- Creating mock objects with `Mock`
- Setting mock return values
- Using `side_effect` for multiple return values
- Using `patch()` with a context manager
- Using `@patch` as a decorator
- Replacing external dependencies during testing
- Verifying whether mocked methods were called
- Using `assert_called()` and `assert_called_once()`

## In-Class Work

### Mocking and Patching Lab

I practiced testing functions that depend on other functions or external services without using the real dependency.

The exercises included mocking a payment gateway, preventing a real email from being sent, controlling weather and date values, returning different values from repeated mock calls, and verifying how many times a mocked method was called.

## What I Learned

Mocking makes tests more predictable because I can control dependencies instead of relying on their real behavior.

I also learned that `patch()` is useful when I need to temporarily replace an existing function during a test, while mock assertions can be used to verify whether a dependency was called correctly.