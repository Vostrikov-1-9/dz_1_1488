class Matrix:
    def __init__(self, spisok=None):
        if spisok is None:
            spisok = [[0]]
        self.spisok = spisok

    def input(self):
        self.spisok = []
        line = int(input("Введите количество строк - "))
        column = int(input("Введите количество столбцов - "))
        for _ in range(line):
            self.spisok.append([])
            for _ in range(column):
                x = int(input("Ввод - "))
                self.spisok[-1].append(x)

    def __str__(self):
        return "\n".join(["\t".join(map(str, i)) for i in self.spisok])
