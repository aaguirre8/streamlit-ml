from typing import Dict

import yaml
from yaml.loader import SafeLoader

import streamlit_authenticator as stauth


def get_users() -> Dict:
    """
    Returns authenticator object with the user credentials from YAML config file.

    Returns:
        Dict: A dict containing the authenticator object and the configuration dictionary.
    """

    with open("src/authentication/credentials.yaml") as file:
        config = yaml.load(file, Loader=SafeLoader)

    authenticator = stauth.Authenticate(
        config["credentials"],
        config["cookie"]["name"],
        config["cookie"]["key"],
        config["cookie"]["expiry_days"],
        config["preauthorized"],
    )

    return authenticator