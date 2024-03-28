import requests
from requests.adapters import HTTPAdapter
from urllib3 import Retry

import env
from helpers.logger import Logger

logger = Logger().getLogger()

baseUrl = env.API_URL_WITH_VERSION

# Create HTTP session for hitting apis

session = requests.Session()
retries = Retry(total=5, connect=10, backoff_factor=1,
                status_forcelist=[500, 502, 503, 504])
adapter = requests.adapters.HTTPAdapter(max_retries=retries)
session.mount('http://', adapter)
session.mount('https://', adapter)


def get_headers():
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    return headers


def get_request(api_url_get, query_param=None):
    url = baseUrl + api_url_get
    logger.info(f"GET Request call url: {url}")
    headers = get_headers()

    try:
        response = session.get(headers=headers, url=url, params=query_param, verify=None, timeout=(5, 20))
        logger.info(f"Response code is {response.status_code}")
        if response.status_code == 401:
            raise Exception("User is not Authorized")
    except requests.exceptions.ConnectionError as conError:
        return "A connection error has occurred::" + repr(conError)
    except requests.exceptions.HTTPError as httpErr:
        return "An HTTP Error occurred::" + repr(httpErr)
    except requests.exceptions.Timeout as timeoutErr:
        return "A timeout error occurred" + repr(timeoutErr)
    except requests.exceptions.RequestException as error:
        return "An unknown error has occurred" + repr(error)
    json_obj = response.json()
    return json_obj, response.status_code
