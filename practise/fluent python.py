import collections
from random import choice
import itertools
import functools
import random
import concurrent.futures
# 用于构建只有少数属性但是没有方法的对象
Card = collections.namedtuple("Card", ["rank", 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')

    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
        print(self._cards)

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


beer_card = Card('7', 'diamonds')
print(beer_card, type(beer_card))
deck = FrenchDeck()
print(len(deck))
print(deck.ranks, deck.suits)
print(deck[0], deck[-1])
print(choice(deck))
print(deck[: 3])
print(deck[12::13])
for card in deck:
    print(card)

for card in reversed(deck):
    print(card)
suit_values = dict(spades=3, heards=2, diamonds=1, clubs=0)
print(suit_values)
#
#
# def spades_high(card):
#     rank_value = FrenchDeck.ranks.index(card.rank)
#     return rank_value * len(suit_values) + suit_values[card.suit]
#
#
# for card in sorted(deck, key=spades_high(Card)):
#     print(card)
# v1 = Vector(2, 4)
# v2 = Vextor(2, 1)
# print(v1 + v2)
print(range(10), list(range(10)))
print(iter(range(10)))
lst = [1, 2, 3]


def gen():
    for num in lst:
        yield num


def gen_123():
    yield 1
    yield 2
    yield 3


for i in gen_123():
    print(i)


def gen_AB():
    print('start')
    yield 'A'
    print('continue')
    yield 'B'
    print('end')


res1 = [x * 3 for x in gen_AB()]
print(res1)
res2 = (x * 3 for x in gen_AB())
print(res2)
for i in res2:
    print('-->', i)


class A:
    def __init__(self, begin, step, end=None):
        self.begin = begin
        self.step = step
        self.end = end

    def __iter__(self):
        result = type(self.begin + self.step)(self.begin)
        forever = self.end is None
        index = 0
        while forever or result < self.end:
            yield result
            index += 1
            result = self.begin + self.step * index


ap = A(0, 1, 3)
print(ap, list(ap))

gen = itertools.count(1, .5)
print(gen, next(gen))
gen = itertools.takewhile(lambda n: n < 3, itertools.count(1, .5))
print(gen, list(gen))

print((lambda n: 2 < 3, 3))


def vowel(c):
    return c.lower() in 'aeiou'


print(list(filter(vowel, 'Aardvark')), filter(vowel, 'Aardvark'))
print(list(itertools.filterfalse(vowel, 'Aardvark')), filter(vowel, 'Aardvark'))
print(list(itertools.dropwhile(vowel, 'Aardvark')))
print(list(map(abs, [-1, 2, 3])))

print(all([1, 2, 3]))
print(all([1, 0, 2]))
print(all([]))
print(functools.reduce(lambda a, b: a*b, range(1, 6)))


def d6():
    return random.randint(1, 6)


# d6_iter = iter(d6, 1)
# print(d6_iter)
# for i in d6_iter:
#     print(i)
with open('git 命令') as fp:
    src = fp.read(60)
print(src)
print(fp.closed, fp.encoding)
x = ('cd sc vf ax oh fsg').split()
print(x)
import json
str = '{"name": "zhangbo", "sex": "man"}'
o = json.loads(str)
# p = json.load(str)
print(o, type(o))
# print(p, type(p))
print(sorted(o.keys()), type(sorted(o.keys())))  # 只取键
print(sorted(o.values()), type(sorted(o.values())))

dict1 = {"info1": {"name": "Bob", "sex": "man"}, "info2": {"name": "Tom", "sex": "woman"}}
print(dict1["info1"]["name"])
