def main():
    with open('sectiondata.txt', 'r') as f:
        lines = f.readlines()
        pair_count = 0
        overlap = 0
        for line in lines:
            nums = eval(line.replace('-',','))
            section_list = [[i for i in range(nums[0],nums[1]+1)],[i for i in range(nums[2],nums[3]+1)]]
            if sorted(section_list[0]) == sorted([i for i in section_list[1] if i in section_list[0]]):
                pair_count += 1
            elif sorted(section_list[1]) == sorted([i for i in section_list[0] if i in section_list[1]]):
                pair_count += 1
            else:
                pair_count += 0

            for i in section_list[0]:
                if i in section_list[1]:
                    overlap+=1
                    break

        print(pair_count)
        print(overlap)

if __name__ == '__main__':
    main()
