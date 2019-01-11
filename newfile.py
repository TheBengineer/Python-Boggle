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

    def options(self, history_string):
        if len(history_string) > 1:
            return self.conn[history_string[0]].options(history_string[1:])
        elif len(history_string) == 1:
            return "".join(self.conn[history_string[0]].conn.keys())
        else:
            return "".join(self.conn.keys())


f = open("words_alpha.txt")

root = Letter("")

i = 0
for word in f.readlines():
    print word,
    root.connect_recursive(word)
    i += 1
    if i > 1000:
        break

root.connect_recursive("as\n")
root.connect_recursive("ass\n")
print root.options("a")
print root.options("as")

boggle_table_1 = [["h", "u", "d", "g"],
                  ["s", "i", "d", "l"],
                  ["n", "c", "j", "a"],
                  ["g", "r", "s", "s"]]

boggle_table = ["hudg",
                "sidl",
                "ncja",
                "grss"]


def history_string(history):
    return "".join([boggle_table[r][c] for c, r in history])


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
    # print column, row, boggle_table[row][column]
    # print history_string(history)
    # print root.options(history_string(history))
    return boggle_table[row][column] in root.options(history_string(history))


def walk_tree((column, row), history, words):

    return words


print walk_tree((3, 2), [], [])

for rowt in range(4):
    for columnt in range(4):
        print check_valid_letter((columnt, rowt), []) * 1,
    print
