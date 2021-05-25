class Edge():
    def __init__(self, input, output, weight) -> None:
        self.input = input
        self.output = output
        self.weight = weight

        output.add_connection(self)

    def call(self):
        out = self.input.call()
        return out * self.weight

    def get_dependencies(self):
        return self.input.get_dependencies()

    def change_input(self, node):
        self.input = node

    def __repr__(self) -> str:
        return self.input.id + " -> " + self.output.id