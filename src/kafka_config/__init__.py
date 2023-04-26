import os
from dotenv import load_dotenv
load_dotenv()

SECURITY_PROTOCOL="SASL_SSL"
SSL_MECHANISM="PLAIN"
API_KEY=os.getenv("API_KEY",None)
BOOTSTRAP_SERVER=os.getenv("BOOTSTRAP_SERVER",None)
API_SECRET_KEY=os.getenv("API_SECRET_KEY",None)
ENDPOINT_SCHEMA_URL=os.getenv("ENDPOINT_SCHEMA_URL",None)
SCHEMA_REGISTER_API_KEY=os.getenv("SCHEMA_REGISTER_API_KEY",None)
SCHEMA_REGISTER_SECRET_KEY=os.getenv("SCHEMA_REGISTER_SECRET_KEY",None)
print(API_KEY)


def sasl_conf():
    sasl_conf = {'sasl.mechanism': SSL_MECHANISM,
                 # Set to SASL_SSL to enable TLS support.
                #  'security.protocol': 'SASL_PLAINTEXT'}
                'bootstrap.servers':BOOTSTRAP_SERVER,
                'security.protocol': SECURITY_PROTOCOL,
                'sasl.username': API_KEY,
                'sasl.password': API_SECRET_KEY
                }
    print(sasl_conf)
    return sasl_conf

def schema_registry_conf():
    return {"url":ENDPOINT_SCHEMA_URL,"basic.auth.user.info":f"{SCHEMA_REGISTER_API_KEY}:{SCHEMA_REGISTER_SECRET_KEY}"}

if __name__=="__main__":
    sasl_conf()