import secrets

generate_api_key = lambda: str(secrets.token_hex(10))
