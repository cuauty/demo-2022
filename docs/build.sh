function build_api_doc()
{
    sphinx-apidoc -f -o source ${PROJECT_DIR}/python/openasce
    make clean
    make html
}

DOCS_DIR=$(cd "$(dirname $0)" && pwd)
PROJECT_DIR="$DOCS_DIR"/..

pushd "${DOCS_DIR}"
build_api_doc
popd
