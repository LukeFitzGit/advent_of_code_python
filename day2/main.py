def main():

        count = 0
        shapes = {'A': 'rock',
                  'B': 'paper',
                  'C': 'scissors',
                  'X': 'rock',
                  'Y': 'paper',
                  'Z': 'scissors'}

        shape_points = {'rock': 1, 'paper': 2, 'scissors': 3}

        for line in lines:
            if shapes[line[0]] == shapes[line[2]]:
                 count += shape_points[shapes[line[0]]] + 3
            elif (shapes[line[0]], shapes[line[2]]) in [('rock', 'scissors'),('paper', 'rock'), ('scissors', 'paper')]:
                count += shape_points[shapes[line[2]]]
            else:
                count += shape_points[shapes[line[2]]] + 6
        print(count)

        beats_dict = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}
        result = 0
        for line in lines:
            if line[2] == 'X':
                result += shape_points[beats_dict[shapes[line[0]]]]
            elif line[2] == 'Y':
                result += shape_points[shapes[line[0]]] + 3
            else:
                result += shape_points[beats_dict[beats_dict[shapes[line[0]]]]] + 6
        print(result)

if __name__ == "__main__":
    main()
