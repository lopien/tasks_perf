import json

tests_file = input('Введите путь к файлу tests.json:')
with open('tests.json', "r") as tests_json:
    tests = json.load(tests_json)

values_file = input('Введите путь к файлу values.json:')
with open(values_file, "r") as values_json:
    values = json.load(values_json)

def report(tests, values):
    for test in tests:
        if 'values' in test:
            report(test['values'], values)
        for value in values:
            if test['id'] == value['id'] and 'value' in test:
                test['value'] = value['value']

report(tests.get('tests'), values.get('values'))

with open('report.json', 'w') as file:
    json.dump(tests, file, indent=2)
