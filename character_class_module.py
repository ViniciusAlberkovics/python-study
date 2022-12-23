class CharacterClass:
    def __init__(self, name, avatar) -> None:
        self.name = name
        self.avatar = avatar

    def describe(self) -> None:
        print(self.name + " - " + self.avatar)
