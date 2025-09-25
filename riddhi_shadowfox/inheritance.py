# inheritance 
class MobilePhone:
    def __init__(self, screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage):
        self.screen_type = screen_type
        self.network_type = network_type
        self.dual_sim = dual_sim
        self.front_camera = front_camera
        self.rear_camera = rear_camera
        self.ram = ram
        self.storage = storage

    def make_call(self, number):
        print(f"Calling {number}...")

    def receive_call(self, caller):
        print(f"Incoming call from {caller}...")

    def take_a_picture(self):
        print(f"Taking a picture with {self.rear_camera} rear camera.")

    def phone_details(self):
        print("\n--- Mobile Phone Details ---")
        print(f"Screen Type: {self.screen_type}")
        print(f"Network Type: {self.network_type}")
        print(f"Dual SIM: {self.dual_sim}")
        print(f"Front Camera: {self.front_camera}")
        print(f"Rear Camera: {self.rear_camera}")
        print(f"RAM: {self.ram}")
        print(f"Storage: {self.storage}")
        print("----------------------------")



# this is child class for Apple
class Apple(MobilePhone):
    def __init__(self, model, front_camera, rear_camera, ram, storage):
        super().__init__("Touch Screen", "5G", False, front_camera, rear_camera, ram, storage)
        self.model = model

    def face_id(self):
        print(f"{self.model} is unlocking using Face ID!")

    def phone_details(self):
        print(f"\n*** Apple {self.model} ***")
        super().phone_details()



# this is child class for Samsung
class Samsung(MobilePhone):
    def __init__(self, model, dual_sim, front_camera, rear_camera, ram, storage):
        super().__init__("Touch Screen", "4G/5G", dual_sim, front_camera, rear_camera, ram, storage)
        self.model = model

    def use_stylus(self):
        print(f"{self.model} is using the S-Pen stylus!")

    def phone_details(self):
        print(f"\n*** Samsung {self.model} ***")
        super().phone_details()



# Created objects for apple here
iphone1 = Apple("iPhone 13", "12MP", "48MP", "4GB", "64GB")
iphone2 = Apple("iPhone SE", "8MP", "12MP", "3GB", "32GB")

# for display details, we use
iphone1.phone_details()
iphone1.make_call("9876543210")
iphone1.face_id()

iphone2.phone_details()
iphone2.take_a_picture()


# Created objects for samsung here
samsung1 = Samsung("Galaxy S21", True, "16MP", "48MP", "4GB", "64GB")
samsung2 = Samsung("Galaxy A32", True, "8MP", "32MP", "3GB", "32GB")

# for display details, we use
samsung1.phone_details()
samsung1.receive_call("John")
samsung1.use_stylus()

samsung2.phone_details()
samsung2.make_call("1234567890")

