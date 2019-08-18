with open('data.csv', mode='r+', encoding='windows-1251') as my_file:
    f = my_file.read().splitlines()
    f.pop(0)
    fn = []
    data = set()
    for i in f:
        s = i.split(',')
        fn.append(s)

    names = set()
    cities = set()
    credit_cards = set()
    deposits = set()
    mortgages = set()

    for i in fn:
        names.add(i[0])
        cities.add(i[1])
        credit_cards.add(i[2])
        deposits.add((i[3]))
        mortgages.add(i[4])

    credit_cards.remove('')
    deposits.remove('')
    mortgages.remove('')

    final = ((name, city, credit_card, deposit, mortgage) for name in names for city in cities
             for credit_card in credit_cards for deposit in deposits for mortgage in mortgages)

    with open('results.txt', 'a') as f_txt:
        for i in final:
            f_txt.write(' '.join(i) + '\n')
