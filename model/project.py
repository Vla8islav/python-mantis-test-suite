class Project:

    def __init__(self, id=None, name="Stock name", enabled = True, description = ""):
        self.name = name
        self.id = id
        self.enabled = enabled
        self.description = description

    def __eq__(self, other):
        return self.name == other.name and self.enabled == other.enabled and self.description == other.description

    def id(self):
        return self.id
