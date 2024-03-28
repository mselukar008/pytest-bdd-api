# pytest-bdd-api
API Tests automation repo with pytest-bdd and python
## Prerequisites:
- Python version 3 or higher
- IDE - Pycharm
- Clone the repo and import the project in Pycharm
- Create virtual environment and activate it (e.g.Windows PF)
  - `python -m venv venv`
  - `source venv/Scripts/activate`
- Install all dependencies from requirements.txt `pip install -r requirements.txt`

## Test Execution
- Feature file path - `tests/features`
- Step definitions path - `tests/step_definitions`
- To run all tests - `pytest`
- To run tests which are marked/tagged - `pytest -m "tagname"`
- `Test Results` are generated with multiple components
    - `Logs` - `Test specific` logs can be viewed from `test_results/test_logs` folder
    - `Consolidated logs` for complete test run is present in `consolidated_test_logs` folder.
    - `HTML Report` can be viewed from `test_results/report.html` file
    - Customization on reports can be further done using `junitresults.xml`

## Folder Structure
- `helpers`- Generic utility files that can be used for writing tests
    - `api_util` - Generic functions for handling api calls
    - `logger` - for reporting logs to text files
    - `resources` - for holding constants or paths of folder
    - `utils` - Generic functions that can be used anywhere
- `test_data` - Test specific data if any
- `config.ini` - Configuration file for holding environment specific data
- `env` - Global variables that will be mapped with the values of config.ini
- `pytest.ini` - pytest configuration
- `conftest` - Starting point of framework from where execution is driven
