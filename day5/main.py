def main():
    part_one = False #set to True for part 1 solution
    with open('boxdata.txt', 'r') as f:
        lines = f.readlines()
        col_dict = {}
        letters_indexes = [1,5,9,13,17,21,25,29,33]
        for i in letters_indexes:
            col_dict[i] = []

        for line in lines[:8]:
            for i in letters_indexes:
                if line[i] != " ":
                    col_dict[i].append(line[i])

        actions = []
        for line in lines[10:]:
           split_line = line.split()
           actions.append([i for i in split_line if i.isdigit()])

        for action in actions:
            _from = int(action[1])
            _to = int(action[2])
            _amount = int(action[0])
            if (part_one):
                for i in range(int(_amount)):
                    col_dict[index_conversion(_to)].insert(0, col_dict[index_conversion(_from)][i])
            else:
                col_dict[index_conversion(_to)][0:0] = col_dict[index_conversion(_from)][:_amount]
            col_dict[index_conversion(_from)] = col_dict[index_conversion(_from)][_amount:]

        print(col_dict)


def index_conversion(index):
    conversion_dict = {1: 1, 2: 5, 3: 9, 4: 13, 5: 17, 6: 21, 7: 25, 8: 29, 9: 33}
    return conversion_dict[index]


if __name__ == '__main__':
    main()
