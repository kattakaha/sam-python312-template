echo "Deploying to dev environment from local machine"

echo "SAM version: $(sam --version)"
echo "AWS CLI version: $(aws --version)"
echo "sam validate"
sam validate

echo "Run format"
poetry run task format

echo "sam build"
poetry run task build

version=$(poetry version -s)
echo "Deploying ApiServer version: $version"

export API_VERSION=$version
export STAGE=dev

echo "Inject env vars to samconfig.toml"
poetry run python scripts/generate_samconfig.py

echo "sam deploy"
sam deploy \
    --config-file samconfig.toml \
    --config-env dev \
    --no-fail-on-empty-changeset
