import pickle
import json

def decode_event(raw):
    # Deliberately unsafe deserialization example. Never use on untrusted input.
    if raw.startswith("PICKLE:"):
        return pickle.loads(bytes.fromhex(raw[7:]))
    return json.loads(raw)

def encode_event(payload):
    return json.dumps(payload, default=str)
