# jira-to-csv-TDD
This is my Python vibe coding adding TDD to make it a bit more professional and prove me it is production ready

Summary Checklist:
✅ Setup testing environment (pytest, pytest-mock, pytest-cov)
✅ Refactor code for testability (dependency injection, pure functions)
✅ Write comprehensive tests (unit, integration, edge cases)
✅ Follow TDD cycle (Red-Green-Refactor)
✅ Measure coverage (aim for >80%)
✅ Test your tests (deliberately break code to verify tests fail)
✅ Continuous testing (run tests before every commit)

This TDD approach will ensure your script is robust and any future changes will immediately show if they break existing functionality!

#########################
<h1>Project history:</h1>
I was challanged by one of my collegues to create a script which enable the retrieval of Lead time from jira.
<h2>I than started with this prompt:</h2>
Considering the attached code as working (please do not change the jira connection) can you create a simple python script which get a CSV input file with at the first column the issue id and retrieve for each element using the API: GET /rest/api/2/issue/{issueIdOrKey} all the jason and retrive from the transition element the first status change to IN Progress and the last move to done creating an CSV output file where these data are reported as additional column in the input CSV with an additional column which include the difference in days from the first In progress and the last done
<h2>I than asked this prompt to improve what I got:</h2>
Considenring this last script I want to learn and implement TDD for it. My target is to be able to prove the script works and that if 
I'll do any change in the future the test will become red. Can you create a step by step procedure I can follow to achieve this objective?

<h2>Step-by-Step TDD Implementation Guide</h2>
<h3>Step 1: Understanding TDD Principles</h3>
TDD Cycle (Red-Green-Refactor):

Red: Write a failing test first
Green: Write minimal code to make the test pass
Refactor: Improve code while keeping tests green
<h3>Step 2: Setup Testing Environment</h3>
Install testing dependencies:
<i>pip install pytest pytest-mock pytest-cov</i>
Create project structure:
<i>
jira_analyzer/
├── jira_status_analyzer.py
├── test_jira_analyzer.py
├── requirements.txt
└── conftest.py
</i>
<h2>Step 3: Refactor Original Script for Testability
</h2>
Create jira_analyzer.py (refactored for testing): [see the file jira_analyzer.py]
<h2>
  Step 4: Write Your First Tests
</h2>
Create test_jira_analyzer.py: [see the file test_jira_analyzer.py]
<h2>
  Step 5: Running Tests
</h2>
Create conftest.py for test configuration: [see the file conftest.py]

<h2>Run tests</h2>
<i>
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run with coverage report
pytest --cov=jira_analyzer

# Run specific test
pytest test_jira_analyzer.py::TestJiraStatusAnalyzer::test_calculate_days_difference

# Run tests that match a pattern
pytest -k "test_parse"

</i>
<h2>
  Step 6: TDD Workflow in Practice
</h2>
Example: Adding a new feature (TDD style)
Scenario: Add validation for issue key format

1) RED: Write failing test first:
[SEE CODE]

<h2>Step 7: Continuous Testing Setup</h2>
Create pytest.ini:
Create requirements-test.txt:

<h2>Step 8: Testing Best Practices</h2>
Test Categories:

<h2>Step 9: Measuring Success</h2>
Good test coverage indicators:
<ul>
<li>Line coverage > 80%</li>
<li>All critical paths tested</li>
<li>Edge cases covered</li>
<li>Both positive and negative scenarios</li>
  </ul>
Run coverage report:
bash:
<i>pytest --cov=jira_analyzer --cov-report=html
# Open htmlcov/index.html to see detailed coverage</i>
<h2>Step 10: Making Tests Fail (Proving They Work)</h2>
Deliberately break your code to verify tests catch issues:

