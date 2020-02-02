def basic_auth(username, password, required_scopes=None):
    if username == "guest" and password == "secret":
        return {"sub": "guest", "valid": True}
    return None
