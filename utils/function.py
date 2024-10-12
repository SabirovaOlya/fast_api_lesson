import hmac
import hashlib

my_secret = "dc3abf2ff68da30f758963a859e4b98d"


def create_hash(message, key=my_secret):
    hmac_text = hmac.new(key=my_secret.encode('utf-8'), msg=message.encode('utf-8'), digestmod=hashlib.sha256)
    message_digest = hmac_text.hexdigest()
    return message_digest

