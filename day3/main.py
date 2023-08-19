def main():
   with open('stringdata.txt', 'r') as f:
        count = 0
        lines = f.readlines()
        for strng in lines:
            compartments = [strng[0:len(strng)//2], strng[len(strng)//2:]]
            matching_items = "".join([i for i in compartments[0] if i in compartments[1]])
            count += get_priority(matching_items[0])
        print(count)


        groups = [[i,lines[lines.index(i)+1],lines[lines.index(i)+2]] for i in lines[::3]]
        count_2 = 0
        for group in groups:
            match = [i for i in group[0] if i in group[1] and i in group[2]]
            count_2 += get_priority(match[0])
        print(count_2)

def get_priority(character):
    if character.isupper():
        return ord(character) - 38
    elif character.islower():
        return ord(character) - 96
    else:
        return 0


if __name__ == "__main__":
    main()
