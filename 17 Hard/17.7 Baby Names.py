class NameHashMap:

    def __init__(self):
        self.nhm = {}
        self.max_index = -1

    def add_synonyms:(self, name):
        if name[0] in self.nhm:
            self.nhm[name[1]] = self.nhm[name[0]]
        elif name[1] in self.nhm:
            self.nhm[name[0]] = self.nhm[name[1]]
        else:
            self.max_index += 1
            self.nhm[name[1]] = self.max_index
            self.nhm[name[0]] = self.max_index


def sol(names, synonyms):
    dictionary = NameHashMap()
    l = [[] for i in range(dictionary.max_index)]

    for s in synonyms:       
        dictionary.add_synonyms(s)

    for n in names:
        if not len(l[dictionary.nhm[n]]):
            l[dictionary.nhm[n[0]]] = [n[0], n[1]]
        else:
            l[dictionary.nhm[n[0]]][1] += n[1]
    return l