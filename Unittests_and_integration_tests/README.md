## Unittests_and_integration_tests
### Difference Between Unit Tests and Integration Tests

1. **Unit Tests**:
   - **Scope**: Unit tests focus on testing individual components or "units" of code in isolation. A "unit" can be a function, method, or class.
   - **Goal**: To ensure that the logic of the individual unit works correctly. Each test is isolated and typically doesn’t rely on external systems such as databases, APIs, or file systems.
   - **Granularity**: Fine-grained; they are small and fast to run.
   - **Tools**: Tools like `unittest` (Python), `Jest` (JavaScript), or `JUnit` (Java) are used.
   - **Example**: Testing a single method in a class to check if it returns the expected output for a given input.

2. **Integration Tests**:
   - **Scope**: Integration tests evaluate how different modules or components of the system work together. This can involve integrating multiple units, external systems, or services.
   - **Goal**: To ensure that the interaction between these units works correctly. These tests often involve real-world systems like databases, APIs, or networks.
   - **Granularity**: Broader scope compared to unit tests; they test larger pieces of functionality.
   - **Tools**: Tools like `pytest`, `mocha`, or `JUnit` (for integration testing in Java) are used.
   - **Example**: Testing a function that retrieves data from a database and processes it. The test checks if both the database interaction and the processing work as expected when combined.

### Common Testing Patterns

1. **Mocking**:
   - **Definition**: Mocking is a technique used to replace real dependencies (like databases, APIs, or services) with controlled objects during tests. This is common in unit tests to isolate the code from external systems.
   - **Purpose**: Allows you to test units in isolation by simulating the behavior of dependencies.
   - **Example**: If a function relies on a third-party API call, you can mock the API call in your unit test so that you can focus only on testing your function without making actual network requests.

2. **Parametrization**:
   - **Definition**: Parametrization allows you to run the same test logic with different sets of input data, making it easier to test a function under multiple scenarios.
   - **Purpose**: Helps reduce code duplication and improve test coverage.
   - **Example**: You can test a function that adds two numbers using different sets of inputs (e.g., `(1, 2)`, `(3, 5)`, `(-1, 1)`) by using a parameterized test.

   ```python
   @pytest.mark.parametrize("a, b, expected", [(1, 2, 3), (3, 5, 8), (-1, 1, 0)])
   def test_add(a, b, expected):
       assert add(a, b) == expected
   ```

3. **Fixtures**:
   - **Definition**: Fixtures are a way to set up some known state before running tests and clean it up afterward. They are used to initialize resources such as database connections, configuration settings, or files.
   - **Purpose**: Allows the setup of a common context for tests without repeating the same setup code in every test.
   - **Example**: In `pytest`, you can define a fixture that provides a database connection for tests. The fixture can ensure the connection is available for each test and tear it down afterward.

   ```python
   @pytest.fixture
   def db_connection():
       connection = create_db_connection()
       yield connection
       connection.close()
   ```

   Using the fixture in a test:

   ```python
   def test_db_query(db_connection):
       result = db_connection.execute("SELECT * FROM users")
       assert len(result) == 10
   ```

### Summary
- **Unit tests** are about testing individual units in isolation, while **integration tests** focus on how units work together.
- Common testing patterns:
   - **Mocking** isolates the code from dependencies.
   - **Parametrization** allows you to test with multiple sets of data.
   - **Fixtures** provide reusable setup and teardown for tests.