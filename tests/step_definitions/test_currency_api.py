"""Currency API Validations feature tests."""
from functools import partial

import pytest
import pytest_bdd
from pytest_bdd import (
    then, when, parsers
)

from env import CURRENCY_URL
from helpers import api_util
from helpers.utils import extract_values

scenario = partial(pytest_bdd.scenario, '../features/test_currency_api.feature')


@scenario('Happy Path Scenario for currency api')
def test_happy_path_scenario_for_currency_api():
    """Happy Path Scenario for currency api."""
    pass


@scenario('UnHappy Path Scenario for currency api')
def test_unhappy_path_scenario_for_currency_api():
    """UnHappy Path Scenario for currency api."""
    pass


@pytest.fixture
def step_context():
    return {'response': None, 'status_code': None}


@when(parsers.cfparse('I execute get currency call with "{currency}"'))
def execute_get_country_currency_request(currency, step_context):
    """I execute get currency call."""
    api_url_currency = str.format(CURRENCY_URL, currency)
    step_context['response'], step_context['status_code'] = api_util.get_request(api_url_currency)


@then(parsers.cfparse('I validate the country with "{currency}" currency as "{country}"'))
def validate_country_currency(currency, country, step_context):
    """I validate the country with currency."""
    countries = extract_values(step_context["response"], "common")
    assert country in countries


@then(parsers.cfparse('I verify status code as "{status_code:d}"'))
def verify_status_code(status_code, step_context):
    """I verify status code"""
    assert step_context[
               'status_code'] == status_code, f"Expected: {status_code} | Actual: {step_context['status_code']}"


@then(parsers.cfparse('I verify response message as "{response_message}"'))
def verify_status_code(response_message, step_context):
    """I verify status message."""
    assert step_context[
               'response'][
               'message'] == response_message, f"Expected: {response_message} | Actual: {step_context['response']['message']}"
