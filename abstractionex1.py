class Phone:
    def __init__(self,contact_no, name):
        self.contact_no = contact_no
        self.name = name

    def call(self):
        print(f"Calling {self.name} at {self.contact_no}...")

    def take_pics(self):
        print(f"taking picture of {self.name}")

phone1=Phone("5656564566","alice")

phone1.take_pics()
phone1.call()
