import os

base_url = os.environ.get('base_url')
jump_url = os.environ.get('jump_url', base_url)
username = os.environ.get('username')
password = os.environ.get('password')
api_key = os.environ.get('api_key')
