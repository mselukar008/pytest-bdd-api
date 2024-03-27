import logging
import os.path
import threading
import pytest
import re
# from py._xmlgen import html
from datetime import datetime
import sys
from _pytest.runner import runtestprotocol

sys.stdout = sys.stderr
server = None
test_name = ""
test_suite_name = None
t_array = []
t1 = None
current_file = ""
outcome = None

# logger = logging.getLogger(__name__)
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


# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item, call):
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     global outcome
#     outcome = yield
#     report = outcome.get_result()
#     soft_assert_failures_report(report, call)
#     extra = getattr(report, 'extra', [])
#     setattr(item, "check_" + report.when, report)
#     test_description = getattr(item.function, '__doc__', '')
#     if not test_description:
#         test_description = "Description is not provided for the Test"
#     report.description = test_description
#     if report.when == 'call' or report.when == 'setup':
#         extra.append(pytest_html.extras.url(get_current_url()))
#         xfail = hasattr(report, 'wasxfail')
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             file_name = item.name + ".png"
#             if not os.path.exists(screenshot_folder):
#                 os.makedirs(screenshot_folder)
#             folder_name = create_folder(screenshot_folder)
#             driver.save_screenshot(os.path.join(os.path.sep, screenshot_folder, folder_name, file_name))
#             extra.append(pytest_html.extras.image(os.path.join(os.path.sep, screenshot_folder, folder_name, file_name)))
#         report.extra = extra


# def pytest_html_report_title(report):
#     report.title = "API Automation Execution Report"


# command line options
# def pytest_addoption(parser):
#     parser.addoption("--slack", "--slack_integration_flag",
#                      dest="slack_integration_flag",
#                      default="no",
#                      help="Post the test report on slack channel: Y or N")
#     parser.addoption("--build", action="store")


# pytest plugin hook
# def pytest_sessionfinish(session, exitstatus):
#     "executes after whole test run finishes."
#     slack_value = 'no'
#     for val in sys.argv:
#         if '--slack' in val:
#             slack_value = val.split('=')[1]
#         if '--build' in val:
#             build = val.split('=')[1]
#             if not build:
#                 build = "it's a local run not a Jenkins run"
#         else:
#             build = "it's a local run not a Jenkins run"
#     # if slack_value.lower() == 'yes':
#     #     post_reports_to_slack(build)
#     # if os.environ.get("collect_har") == "yes":
#     #     proxy_server.stop_capture()


def get_test_file_name():
    return os.getenv('PYTEST_CURRENT_TEST').split("::")[0].split("/")[-1].split(".py")[0]


#
#
# @pytest.mark.optionalhook
# def pytest_html_results_table_header(cells):
#     cells.insert(2, html.th('Description'))
#     cells.insert(3, html.th('Time', class_='sortable time', col='time'))
#
#
# @pytest.mark.optionalhook
# def pytest_html_results_table_row(report, cells):
#     cells.insert(2, html.td(getattr(report, 'description', '')))
#     cells.insert(3, html.td(datetime.utcnow(), class_='col-time'))
#
#
# def pytest_assertion_pass(expl):
#     filter_data = re.split('== | in | > | >= | < | <= | !=', expl)
#     if "True" in expl:
#         logger.info(
#             "Test Data for Pass Assertion ->" + " Actual: True" + " Expected: True" + ' PASS')
#     elif "==" in expl:
#         logger.info(
#             "Test Data for Pass Assertion ->" + " Actual: " + filter_data[0] + " Expected: " + filter_data[0] + ' PASS')
#     elif any(op in expl for op in ["<", ">", "<=", ">=", "!="]):
#         logger.info(
#             "Test Data for Pass Assertion ->" + " Left side value: " + filter_data[0] + " Right side value: " +
#             filter_data[1] + ' PASS')
#     else:
#         logger.info(
#             "Test Data for Pass Assertion ->" + " Actual: " + filter_data[1] + " Expected: " + filter_data[0] + ' PASS')
#
#
# def pytest_exception_interact(report):
#     logging.error(f'Test exception:\n{report.longreprtext}')
#
#
# def pytest_runtest_protocol(item, nextitem):
#     reports = runtestprotocol(item, nextitem=nextitem)
#     for report in reports:
#         if report.when == 'setup':
#             if report.failed:
#                 logger.info("SETUP FAILED!!!")
#         if report.when == 'call':
#             if report.failed:
#                 logger.info(f"Execution Result:{item.name}::{report.outcome.upper()}")
#             elif report.passed:
#                 global test_name
#                 test_name = item.name
#                 logger.info(f"Execution Result:{test_name}::{report.outcome.upper()}")
#     return True
#
#
# @pytest.fixture(scope="module", autouse=True)
# def setup(request):
#     global url
#     global test_suite_name
#     test_suite_name = request.node.name
#     url = get_current_url()
#     logger.info(url)
#     if "multicloud-ibm.com" not in url or is_element_present(page_header, "Sign In Page", 10):
#         load_base_page(tenant)
#     # reset fixtures for check_status and check_order_creation to None for every new suite
#     # to handle exceptions on additional parameter page before submitting order
#     set_data(None)
#     logger.info("========================Launched to Homepage========================")
#     logger.info("========================Test Suite Execution Started : " + test_suite_name + "======================")
#
#
# def tear_down():
#     global t1
#     global outcome
#     global current_file
#     if collect_video in ["all", "on_failure"]:
#         t1.join()
#         report = outcome.get_result()
#         if collect_video == "on_failure" and report.passed:
#             logger.info("Removing the video file as test passed or skipped :" + str(current_file))
#             if os.path.exists(current_file):
#                 os.remove(current_file)


def create_folder(folder, file_name=None):
    if file_name is None:
        file_name = get_test_file_name()
    if not os.path.exists(os.path.join(os.path.sep, folder, file_name)):
        os.makedirs(os.path.join(os.path.sep, folder, file_name))
    return file_name


@pytest.fixture(scope="function", autouse=True)
def execute_teardown(request):
    request.addfinalizer(tear_down)


def tear_down():
    global t1
    global outcome
    global current_file
    # report = outcome.get_result()
    # status = "FAILED"
    # if report.passed():
    #     status = "PASSED"
    logger.info(f"===============================================")


def get_suit_list(suit):
    n = len(suit)
    suit_list = []
    for i in range(1, n):
        if "tests" in sys.argv[i]:
            suit_list.append(sys.argv[i])
    return suit_list


@pytest.fixture(scope="function", autouse=True)
def on_start():
    global t_array
    global t1
    global current_file
    test_case_name = str(os.getenv('PYTEST_CURRENT_TEST').split("::")[1].split(" ")[0])
    logger.info(f"==========Test Case Execution started for test : '{test_case_name}'")


