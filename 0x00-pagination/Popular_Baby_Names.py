#!/usr/bin/env python3
"""
Create a CSV file containing fetched data
"""
import requests


def fetch_data(url, filename):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(filename, 'w') as f:
                f.write(response.text)
            return 'Data saved to {}'.format(filename)  # Updated to use .format()
        else:
            return 'Error occurred with status code {}'.format(response.status_code)  # Updated to use .format()
    except requests.exceptions.RequestException as e:
        return 'Error: {}'.format(e)  # Updated to use .format()


if __name__ == '__main__':
    url = 'https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/misc/2020/5/7d3576d97e7560ae85135cc214ffe2b3412c51d7.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240902%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240902T134138Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=ca441acae1ba5cd402e72e074e4f3e5f5d42508743fd9d4c213fa60e077270c4'
    filename = 'Popular_Baby_Names.csv'
    result = fetch_data(url, filename)
    print(result)
