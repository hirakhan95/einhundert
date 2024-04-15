import pytz
from datetime import datetime, timedelta

from .utils import to_iso_string, request_json_from_http, convert_iso_to_datetime



def create_carbonintensity_request_url(from_date: datetime,
                                       to_date: datetime):
    """
    Given from_date to to_date return carbon intensity request url
    """
    from_date = to_iso_string(from_date)
    to_date = to_iso_string(to_date)
    return f"https://api.carbonintensity.org.uk/intensity/{from_date}/{to_date}"


def fetch_previous_intensity(from_date: datetime,
                             to_date: datetime = datetime.utcnow().replace(tzinfo=pytz.utc),
                             days_limit=10):
    """
    Using date from and date to fetch data from carbon instensity endpoint
    """
    merged_data = []

    # initialization
    window_from_date = from_date
    window_to_date = window_from_date + timedelta(days=days_limit)

    while window_from_date < to_date:
        # processing
        url = create_carbonintensity_request_url(
            window_from_date,
            window_to_date - timedelta(minutes=1)
        )
        data = request_json_from_http(url)
        merged_data.extend(data['data'])

        # increment
        window_from_date = window_to_date
        window_to_date = window_from_date + timedelta(days=days_limit)

    final_data = []
    for data in merged_data:
        if data['intensity']['actual'] is not None:
            data = {
                'from_date': convert_iso_to_datetime(data['from']),
                'to_date': convert_iso_to_datetime(data['to']),
                'intensity_forecast': data['intensity']['forecast'],
                'intensity_actual': data['intensity']['actual'],
                'intensity_index': data['intensity']['index']
            }
            final_data.append(data)

    return final_data
