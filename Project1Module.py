# Manar Abouhenidi
# Project #1 implementation of HASH class
# Project1Module.py
# -------------------------------------------------------------

import math


class HASH:

    def __init__(self, M, HashF):
        if HASH.__IsPrime__(self, M):
            self.M = M
        else:
            self.M = HASH.__NextPrime__(self, M)
        self.HashF = HashF
        self.N = 0
        self.table = {}
        for num in range(self.M):
            self.table.update({num: []})

    def __del__(self):
        item = self.__len__()
        del self.table[item - 1]

    def __str__(self):
        row_to_str = ""
        for elem in self.table.keys():
            row_to_str = row_to_str + str(elem) + ':\t'
            if self.table[elem]:
                for item in self.table[elem]:
                    row_to_str = row_to_str + '({}, {})'.format(item[0], item[1]) + " "
            else:
                row_to_str = row_to_str + '***EMPTY***'
            row_to_str = row_to_str + "\n"
        return row_to_str

    def Add(self, itemkey, itemdata):
        hindex = self.HashF(itemkey, self.M)
        self.table[hindex].append((itemkey, itemdata))
        self.N += 1

    def __add__(self, item):
        hindex = self.HashF(item[0], self.M)
        self.table[hindex].append((item[0], item[1]))
        self.N += 1
        return self

    def __radd__(self, item):
        hindex = self.HashF(item[0], self.M)
        self.table[hindex].append((item[0], item[1]))
        self.N += 1
        return self

    def __iadd__(self, item):
        hindex = self.HashF(item[0], self.M)
        self.table[hindex].append((item[0], item[1]))
        self.N += 1
        return self

    def Sub(self, itemkey):
        hindex = self.HashF(itemkey, self.M)
        i = 0
        for i in range(0, len(self.table[hindex])):
            item = self.table[hindex][i]
            if (itemkey == item[0]):
                self.table[hindex].remove(item)
                self.N -= 1
                return
        else:
            raise (KeyError)

    def __sub__(self, itemkey):
        hindex = self.HashF(itemkey, self.M)
        i = 0
        for i in range(0, len(self.table[hindex])):
            item = self.table[hindex][i]
            if (itemkey == item[0]):
                self.table[hindex].remove(item)
                self.N -= 1
                return self
        else:
            raise (KeyError)

    def __rsub__(self, itemkey):
        hindex = self.HashF(itemkey, self.M)
        i = 0
        for i in range(0, len(self.table[hindex])):
            item = self.table[hindex][i]
            if (itemkey == item[0]):
                self.table[hindex].remove(item)
                self.N -= 1
                return self
        else:
            raise (KeyError)

    def __isub__(self, itemkey):
        hindex = self.HashF(itemkey, self.M)
        i = 0
        for i in range(0, len(self.table[hindex])):
            item = self.table[hindex][i]
            if (itemkey == item[0]):
                self.table[hindex].remove(item)
                self.N -= 1
                return self
        else:
            raise (KeyError)

    def __contains__(self, itemkey):
        hindex = self.HashF(itemkey, self.M)
        ret2con = False
        for i in range(0, len(self.table[hindex])):
            item = self.table[hindex][i]
            if (itemkey == item[0]):
                ret2con = True
        return ret2con

    def __len__(self):
        return len(self.table)

    def __getitem__(self, itemkey):
        hindex = self.HashF(itemkey, self.M)
        for item in self.table[hindex]:
            if (itemkey == item[0]): return (item[1])
        raise (KeyError)

    def __IsPrime__(self, x):
        r = True
        for d in range(2, int(math.sqrt(x) + 1)): r = r and (x % d != 0)
        return (r)

    def __NextPrime__(self, x):
        while (not self.__IsPrime__(x)): x += 1
        return (x)
