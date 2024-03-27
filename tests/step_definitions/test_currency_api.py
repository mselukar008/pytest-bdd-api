"""Currency API Validations feature tests."""
import pytest
from pytest_bdd import (
    given,
    scenario,
    then,
    when, parsers, scenarios,
)

from helpers import api_util
from helpers.env import get_currency


scenarios('../features/test_currency_api.feature', 'Happy Path Scenario for currency api')
# def test_happy_path_scenario_for_currency_api():
#     """Happy Path Scenario for currency api."""


@pytest.fixture
def step_context():
    return {'response': None}


@when(parsers.parse('I execute get currency call with $"{currency:s}"'))
def execute_get_country_currency_request(currency, step_context):
    """I execute get currency call with "INR"."""
    api_url_currency = str.format(get_currency, currency)
    step_context['response'] = api_util.get_request(api_url_currency)


@then(parsers.parse('I validate the country with $"{currency:s}" currency as $"{country:s}"'))
def validate_country_currency(currency, country, step_context):
    """I validate the country with "INR" currency."""
    countries = step_context["response"]



@then(parsers.parse('I verify status code as $"{status_code:d}"'))
def verify_status_code(status_code, step_context):
    """I verify status code as "200"."""
    assert step_context['response'].status_code == status_code
