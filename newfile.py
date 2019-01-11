class letter:
    def __init__(self, l):
        self.l = l
        self.conn = {}

    def c(self, l):
        if l not in self.conn:
            self.conn[l] = letter(l)

    def cr(self, ar):
        if ar:
            self.c(ar[0])
            self[ar[0]].cr(ar[1:])

    def __getitem__(self, key):
        return self.conn[key]

    def __str__(self):
        return str(self.conn.keys())

    def options(self, his):
        if len(his) > 1:
            return self.conn[his[0]].options(his[1:])
        else:
            return self.conn[his[0]].keys()


f = open("words_alpha.txt")

root = letter("")

i = 0;
for word in f.readlines():
    print word,
    root.cr(word)
    i += 1
    if i > 1000:
        break

root.cr("as")
root.cr("ass")
print root.options("a")
print root.options("as")

B = [["h", "u", "d", "g"],
     ["s", "i", "d", "l"],
     ["n", "c", "j", "a"],
     ["g", "r", "s", "s"]]
for r in range(4):
    print r, range(max(0, r - 1), min(4, r + 2))


def word(his):
    return "".join([B[c][r] for c, r in his])


def close((r, c), (rp, cp)):
    a = []
    r0 = range(max(0, r - 1), min(4, r + 2))
    c0 = range(max(0, c - 1), min(4, c + 2))
    for rt in r0:
        for ct in c0:
            if not (rt == r and ct == c) and not (rt == rp and ct == cp):
                a.append(((rt, ct)))
    return a


def check((c, r), his):
    print c, r
    print word(his)
    cn, rn = 0, 0
    cl = close((cn, rn), (c, r))


def pos(his):
    ass


print check((2, 3), [])
