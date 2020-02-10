class DavyService:
    __services = {}

    def __init__(self):
        self.services = {
            "Oil change"    : 35,
            "Tire rotation" : 19,
            "Car wash"      : 7,
            "Car wax"       : 12
        }

    def get_services(self):
        return self.services

    def print_services(self):
        print("Davy's auto shop services")
        for service in self.services:
            print('%s -- $%d' % (service, self.services[service]))
        print()