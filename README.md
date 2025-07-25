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
<br>
Red: Write a failing test first<br>
Green: Write minimal code to make the test pass<br>
Refactor: Improve code while keeping tests green<br>

<h3>Step 2: Setup Testing Environment</h3>
Install testing dependencies:<br>
<i>pip install pytest pytest-mock pytest-cov</i>
Create project structure:<br>
<i>
jira_analyzer/<br>
├── jira_status_analyzer.py<br>
├── test_jira_analyzer.py<br>
├── requirements.txt<br>
└── conftest.py<br>
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

<h1>New prompt after some issue founds</h1>
I've some doubt:<br/>
Step 2 you report jira_status_analyzer.py while in step 3 it's named jira_analyzer.py<br/>
Step 6 you reported python but not the file where this changes should be<br/>
Step 7 you mention "Create pytest.ini" which is a file not present in Step 2<br/>
Step 7 you mention "Create requirements-test.txt" which is a file not present in Step 2 (or at least with a different name)<br/>
Step 8 you reported python but not the file where this changes should be<br/>
Step 10 you reported python but not the file where this changes should be<br/>
Can you please review and correct the whole process? Please note I've already created the file mentioned so if they are unchanged please do not report all the file content in the new procedure but only a reference to the previous procedure
<br/>
Step 1: Understanding TDD Principles
(No changes - as per previous procedure)

Step 2: Setup Testing Environment
Install testing dependencies: (No changes - as per previous procedure)<br>
Create project structure:<br/>
<i>
jira_analyzer/<br/>
├── jira_analyzer.py                    # ← CORRECTED: Main script (refactored version from Step 3)<br/>
├── test_jira_analyzer.py               # ← Test file (from Step 4) <br/>
├── requirements.txt                    # ← Dependencies for main app<br/>
├── requirements-test.txt               # ← NEW: Testing dependencies (see Step 7)<br/>
├── conftest.py                         # ← Test configuration (from Step 5)<br/>
└── pytest.ini                         # ← NEW: Pytest configuration (see Step 7)<br>
<br>
</i>

Step 3: Refactor Original Script for Testability
File: jira_analyzer.py
(Content as provided in previous Step 3 - no changes)

Step 4: Write Your First Tests
File: test_jira_analyzer.py
(Content as provided in previous Step 4 - no changes)

Step 5: Running Tests
File: conftest.py
(Content as provided in previous Step 5 - no changes)

Step 6: TDD Workflow in Practice
Example: Adding a new feature (TDD style)
Scenario: Add validation for issue key format

RED: Write failing test first in test_jira_analyzer.py:


Run test - it will fail (RED)

GREEN: Add minimal code to make it pass in jira_analyzer.py:

Run test - it will fail (RED)

GREEN: Add minimal code to make it pass in jira_analyzer.py:

Create new file: requirements-test.txt

pytest==7.4.0
pytest-mock==3.11.1
pytest-cov==4.1.0
pytest-xdist==3.3.1

Update existing file: requirements.txt

jira==3.5.0
Step 8: Testing Best Practices
Test Categories - ADD to test_jira_analyzer.py:

Run specific test types:
# Run only unit tests
pytest -m unit

# Run only integration tests  
pytest -m integration

# Skip slow tests
pytest -m "not slow"

Step 9: Measuring Success
(No changes - as per previous procedure)

Step 10: Making Tests Fail (Proving They Work)
Deliberately break your code in jira_analyzer.py to verify tests catch issues:

Run tests - they should fail, proving they work!
Remember to revert this change after testing!

Summary of Files Created/Modified:
New Files to Create:

pytest.ini (Step 7)
requirements-test.txt (Step 7)
Files with Content from Previous Steps:

jira_analyzer.py (Step 3 - refactored main script)
test_jira_analyzer.py (Step 4 - test file)
conftest.py (Step 5 - test configuration)
Files to Modify:

requirements.txt (Step 7 - add main dependencies)
test_jira_analyzer.py (Step 6 & 8 - add new tests as needed)
jira_analyzer.py (Step 6 & 10 - add new methods or temporary breaks for testing)
Installation Commands:
<i> # Install main dependencies
pip install -r requirements.txt

# Install testing dependencies  
pip install -r requirements-test.txt</i>
