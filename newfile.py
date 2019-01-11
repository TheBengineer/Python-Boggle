class Letter:
    def __init__(self, letter):
        self.letter = letter
        self.conn = {}

    def connect(self, l):
        if l not in self.conn:
            self.conn[l] = Letter(l)

    def connect_recursive(self, ar):
        if ar:
            self.connect(ar[0])
            self[ar[0]].connect_recursive(ar[1:])

    def __getitem__(self, key):
        return self.conn[key]

    def __str__(self):
        return str(self.conn.keys())

    def options(self, his):
        if len(his) > 1:
            return self.conn[his[0]].options(his[1:])
        else:
            return self.conn[his[0]].conn.keys()


f = open("words_alpha.txt")

root = Letter("")

i = 0
for word in f.readlines():
    print word,
    root.connect_recursive(word)
    i += 1
    if i > 1000:
        break

root.connect_recursive("as")
root.connect_recursive("ass")
print root.options("a")
print root.options("as")

boggle_table_1 = [["h", "u", "d", "g"],
                  ["s", "i", "d", "l"],
                  ["n", "c", "j", "a"],
                  ["g", "r", "s", "s"]]

boggle_table = [["hudg"],
                ["sidl"],
                ["ncja"],
                ["grss"]]


def print_history(history):
    print "".join([boggle_table[c][r] for c, r in history])


def next_letters((start_column, start_row), history):
    candidates = []
    rows = range(max(0, start_row - 1), min(4, start_row + 2))
    columns = range(max(0, start_column - 1), min(4, start_column + 2))
    for row in rows:
        for column in columns:
            if not (row == start_row and column == start_column):
                if not (row, column) in history:
                    candidates.append((row, column))

    return candidates


def check_valid_letter((column, row), history):
    print column, row
    print_history(history)
    cn, rn = 0, 0
    cl = history((cn, rn), (column, row))


def pos(his):
    pass


print check_valid_letter((2, 3), [])
