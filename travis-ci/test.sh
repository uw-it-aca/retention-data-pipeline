#!/bin/sh
set -e
trap 'exit 1' ERR

# travis test script for django app
#
# PRECONDITION: inherited env vars from application's .travis.yml MUST include:
#      DJANGO_APP: django application directory name

# start virtualenv
source bin/activate

# install test tooling
pip install pycodestyle coverage
apt-get install -y nodejs npm
npm install -g npm@latest
hash -r

npm install -g eslint@5.0.0 stylelint@13.3.3 eslint-plugin-vue
npm install

function run_test {
    echo "##########################"
    echo "TEST: $1"
    eval $1
}

run_test "pycodestyle ${DJANGO_APP}/ --exclude='migrations,resources,static'"


run_test "eslint --ext .js,.vue retention_dashboard/static/retention_dashboard/js/"

run_test "stylelint 'retention_dashboard/**/*.vue' 'retention_dashboard/**/*.scss' "
run_test "coverage run --source=${DJANGO_APP} '--omit=*/migrations/*' manage.py test ${DJANGO_APP}"

ls -lah
# put generaged coverage result where it will get processed
cp .coverage /coverage

exit 0
