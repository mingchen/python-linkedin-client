#!/usr/bin/env python
# -*- coding: utf-8 -*-

from python_linkedin_client.linkedinclient import LinkedInClient


def test_get_authorization_url():
    client = LinkedInClient('client_key', 'client_secret', 'http://localhost:9000/oauth2/linkedin/callback')
    url = client.get_authorization_url('r_basicprofile r_emailaddress', 'state_1')
    assert url == 'https://www.linkedin.com/uas/oauth2/authorization?scope=r_basicprofile+r_emailaddress&state=state_1&redirect_uri=http%3A%2F%2Flocalhost%3A9000%2Foauth2%2Flinkedin%2Fcallback&response_type=code&client_id=client_key'

def test_get_access_token():
    client = LinkedInClient('client_key', 'client_secret', 'http://localhost:9000')
    access_code = 'AQRPYw6Bi98VBthyFyEQbDUocmiX1NyD0Mo2HL5AgaH0275Cek3vdBdyeZOIIuc+tkH21cQwcF45WXFDBicj9IO+LLC+y9ggOkrCx2Je89A3vUIoTJZ'
    (status_code, data) = client.get_access_token(access_code)
    # assert status_code == 200
    # Get access token by client.access_token
    # assert client.access_token is not None

def test_get_profile():
    client = LinkedInClient('client_key', 'client_secret', 'http://localhost:9000')
    access_code = 'AQRPYw6Bi98VBthyFyEQbDUocmiX1NyD0Mo2HL5AgaH0275Cek3vdBdyeZOIIuc+tkH21cQwcF45WXFDBicj9IO+LLC+y9ggOkrCx2Je89A3vUIoTJZ'
    (status_code, data) = client.get_access_token(access_code)
    (status_code, data) = client.get_profile(['id', 'first-name', 'last-name', 'email-address'])
    # assert status_code == 200
    # assert data['email-address'] is not None