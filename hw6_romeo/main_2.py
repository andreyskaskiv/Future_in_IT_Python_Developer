import re

f = open('romeo.txt', 'r')
text = str(f.readlines())
# print("%s\n" % text)

words = re.findall('[a-zA-Z]{2,}', text)  # Регулярка для слов от двух букв
# print("%s\n" % words)

stats = {}
for w in words:
    stats[w] = stats.get(w, 0) + 1
print(stats)

w_ranks = sorted(stats.items(), key=lambda x: x[1], reverse=True)[0:10]
print(w_ranks)


_wrex = re.findall('[a-zA-Z]+', str(w_ranks))
_drex = re.findall('[0-9]+', str(w_ranks))
pl = [p for p in range(1, 11)]

for j in range(len(_wrex)):
    places = '{} place,{} - {} times'.format(pl[j], _wrex[j], _drex[j])
    print(places)
