import os.path
import pytest
from datetime import datetime
import sys
import env

sys.stdout = sys.stderr
server = None
test_name = ""
test_suite_name = None
t_array = []
t1 = None
current_file = ""
outcome = None

from helpers.logger import Logger

# Get logger instance for consolidated logs
logger = Logger().getLogger()


# Update logging plugin to store logs from individual tests
@pytest.hookimpl
def pytest_runtest_setup(item):
    logging_plugin = item.config.pluginmanager.get_plugin("logging-plugin")
    timestamp = datetime.strftime(datetime.now(), '%Y-%m-%d')
    timestamp_test = "_" + str(datetime.strftime(datetime.now(), '%Y-%m-%d_%H-%M-%S'))
    logging_plugin.set_log_path(
        os.path.join('test_results/test_logs', timestamp, f'{item.name}' + timestamp_test + '.log'))


# Get filename from running test
def get_test_file_name():
    return os.getenv('PYTEST_CURRENT_TEST').split("::")[0].split("/")[-1].split(".py")[0]


# Fixture to run after each test function
@pytest.fixture(scope="function", autouse=True)
def execute_teardown(request):
    request.addfinalizer(tear_down)


def tear_down():
    logger.info(f"===============================================")


# Fixture to run before each test function
@pytest.fixture(scope="function", autouse=True)
def on_start():
    test_case_name = str(os.getenv('PYTEST_CURRENT_TEST').split("::")[1].split(" ")[0])
    logger.info(f"==========Test Case Execution started for test : '{test_case_name}'")


# Support for command line arguments
# def pytest_addoption(parser):
#     parser.addoption("--api_base_url", default="https://restcountries.com")
#     parser.addoption("--api_version", default="v3.1")

# Add Environment variable in global scope
def pytest_configure():
    env.load_config_variables()


# Update title of html report
def pytest_html_report_title(report):
    report.title = "API Automation Test Run Summary"
