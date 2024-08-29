class Grid:
    def __init__(self, width, height, cell_size):
        self.cell_size = cell_size
        self.cells = {}

    def add(self, boid):
        cell_x = int(boid.position.x // self.cell_size)
        cell_y = int(boid.position.y // self.cell_size)
        cell_key = (cell_x, cell_y)
        if cell_key not in self.cells:
            self.cells[cell_key] = []
        self.cells[cell_key].append(boid)

    def get_neighbors(self, boid):
        cell_x = int(boid.position.x // self.cell_size)
        cell_y = int(boid.position.y // self.cell_size)
        neighbors = []
        for x in range(cell_x - 1, cell_x + 2):
            for y in range(cell_y - 1, cell_y + 2):
                neighbors.extend(self.cells.get((x, y), []))
        return neighbors

    def clear(self):
        self.cells.clear()