## Python API Automation Framework

## Integration test cases for restful booker

URL: https://restful-booker.herokuapp.com/apidoc/index.html

We use Restful booker since it allows most of the HTTP methods. 
1. Verify GET,POST,PUT,PATCH DELETE.
2. Verfiy response body,status code, headers.
3. It supports AUTH like basic and cookies.
4. Json schema validation


## Tech stack(Pyton Packages used)
1. Request module
2. Pytest, Pytest-html
3. Allure Report
4. Faker,CSV,Json,YAML
5. Run via command line- Jenkins

## P.S  DB connection(in future)

## packages to be installed
` pip install requests pytest pytest-html faker allure-pytest jsonschema `
` pip install requirements.txt`

## how to run locally and see report?
`pytest TEST_SCRIPTS -s -v --html==report.html`


## How to run via jenkins?
