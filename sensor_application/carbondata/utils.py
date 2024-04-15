from datetime import datetime

import requests


def to_iso_string(date_time: datetime):
    """
    Given a datetime object return iso string (i.e. 2017-10-01T12:00Z)
    """
    return date_time.strftime('%Y-%m-%dT%H:%MZ')


def convert_iso_to_datetime(iso_string: str):
    """
    Parse the ISO 8601 formatted string to a datetime object
    The 'Z' in the ISO string stands for UTC, so replace it with '+00:00' which is recognized by fromisoformat
    """
    iso_string = iso_string.replace('Z', '+00:00')
    return datetime.fromisoformat(iso_string)


def request_json_from_http(url: str):
    """
    Given a url (that is string) return json if able to fetch data else return None
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None
