# Week 04 – Pytest Fixtures and Markers

This week, I practised using pytest fixtures and markers to improve test organization and execution.

## What I Practised

* Creating reusable test fixtures with `@pytest.fixture`.
* Using custom markers to categorize tests.
* Running selected tests using the `-m` option.
* Skipping tests using `skip` and `skipif`.
* Handling expected failures using `xfail`.
* Registering custom markers in `pytest.ini`.

## In-Class Work

### Fixture Lab

Created a reusable `account` fixture using the `BankAccount` class from Week 02.

The fixture initializes a bank account with a balance of 100 and provides a fresh account for each test. I used it to test deposit and withdrawal operations without repeating the setup code.

### Marker Lab

Practised different pytest markers:

* `smoke` – Tests for critical functionality.
* `slow` – Tests that take longer to execute.
* `regression` – Tests for previously fixed bugs.
* `skip` – Skips a test unconditionally.
* `skipif` – Skips a test when a specified condition is met.
* `xfail` – Marks a test as an expected failure.

I also experimented with an unregistered marker to understand how `--strict-markers` detects invalid marker names.

## Pytest Configuration

Updated the shared `pytest.ini` at the repository root to register custom markers and enable strict marker checking.

Keeping one configuration allows all weekly exercises to use consistent pytest settings.

## What I Learned

Fixtures help reduce repeated setup code and keep tests independent. Markers make it easier to organize and execute specific groups of tests. I also learned the difference between skipped tests, expected failures (XFAIL), and unexpected passes (XPASS).
