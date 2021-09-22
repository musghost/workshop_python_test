from dataclasses import dataclass, field
import requests
import sys

@dataclass
class CrazyScript:
    element: dict = field(default_factory=dict, init=False)

    def populate(self, path):
        print("Pulling information...")
        r = requests.get('http://localhost:5000{}'.format(path))
        if r.status_code == 200:
            data = r.json()
            self.element["age"] = data["age"]
            self.element["account"] = data["account"]
        else:
            raise Exception('Something happened!')
    
    def process_age(self):
        result = 'Unkown age'
        if self.element['age'] >= 18 and self.element['age'] > 2:
            result = 'Adult'
        elif self.element['age'] < 18 and self.element['age'] > 2:
            result = 'Child'
        else:
            result = 'Baby'
        return result
    
    def process_account(self):
        if self.element['account']['enabled'] is True:
            result = 'All is good'
        else:
            result = 'Cannot access anymore!'
        return result

if __name__ == '__main__':
    
    print("Starting script")

    cs = CrazyScript()
    cs.populate('/some_user')

    age = cs.process_age()
    print("This user is: {}".format(age))

    account_status = cs.process_account()
    print("Account status: {}".format(account_status))
