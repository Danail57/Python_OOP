#1
text = input()

unique_symbols = set()
for ch in text:
    unique_symbols.add(ch)

for ch in sorted(unique_symbols):
    print(f'{ch}: {text.count(ch)} time/s')


#2
text = tuple(sorted([x for x in input()]))
symbols = {}

for symbol in text:
    if symbol not in symbols:
        symbols[symbol] = text.count(symbol)

for symbol, count in symbols.items():
    print(f'{symbol}: {count} time/s')
