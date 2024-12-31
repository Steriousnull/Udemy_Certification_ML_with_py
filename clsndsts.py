# class and static method


class welcome:
    fruit = "apple"

    @classmethod
    def organic(cls):
        print(f"{welcome.fruit}")

    @staticmethod
    def inorganic():
        return welcome.fruit


welcome.organic()
print(welcome.inorganic())
