import toml
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STAGE = os.getenv("STAGE", "dev")

API_VERSION = os.getenv("API_VERSION", "latest")
API_VERSION_KEY = "ApiVersion"


samconfig_path = os.path.join(BASE_DIR, "samconfig.toml")

dict_toml = toml.load(open(samconfig_path))
parameters = dict_toml[STAGE]["global"]["parameters"]["parameter_overrides"]

# update parameters
updated_parameters = []
for parameter in parameters:
    key, value = parameter.split("=")
    if key == API_VERSION_KEY:
        value = API_VERSION
    updated_parameters.append(f"{key}={value}")

# update SAM deploy parameters with new API_VERSION
dict_toml[STAGE]["global"]["parameters"]["parameter_overrides"] = updated_parameters

# write to the toml file
with open(samconfig_path, "w") as f:
    toml.dump(dict_toml, f)

print(f"Updated {API_VERSION_KEY} to {API_VERSION} in {samconfig_path}")
