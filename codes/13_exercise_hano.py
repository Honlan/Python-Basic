def hano(N, source, target):
    if N == 1:
        print(1, source, '=>', target)
    else:
        pillars = ['A', 'B', 'C']
        pillars.remove(source)
        pillars.remove(target)
        media = pillars[0]

        hano(N - 1, source, media)
        print(N, source, '=>', target)
        hano(N - 1, media, target)

hano(4, 'B', 'C')
