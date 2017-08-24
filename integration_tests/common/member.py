import requests

from config.config import CORE_DOMAIN, GET_ONLY_AUTH_KEY

headers = {
    'Authorization': GET_ONLY_AUTH_KEY
}


def get_member(msisdn):
    end_point = CORE_DOMAIN + '/api/v3/members/' + msisdn

    response = requests.get(end_point, headers=headers)
    status_code = response.status_code

    return status_code, response.json()


def add_new_member(msisdn, channel):
    end_point = CORE_DOMAIN + '/api/v3/members/'
    data = {
        "msisdn": msisdn,
        "channel": channel
    }

    response = requests.post(end_point, headers=headers, data=data)
    status_code = response.status_code

    return status_code, response.json()


def get_members(membership_type=None, status=None):
    params = {}
    if membership_type:
        params['membership_type'] = membership_type
    if status:
        params['status'] = status
    end_point = CORE_DOMAIN + '/api/v3/members?'

    response = requests.get(end_point, headers=headers, params=params)
    status_code = response.status_code

    return status_code, response.json()


def update_member_info(msisdn, data=None):
    end_point = CORE_DOMAIN + '/api/v3/members/' + msisdn

    response = requests.put(end_point, headers=headers, data=data)
    status_code = response.status_code

    return status_code, response.json()

