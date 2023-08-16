def main():
    with open("calories_data.txt", "r") as f:
        lines = f.readlines()
        cal_sum_list = []
        n = 0
        for l in lines:
            if l.strip().isdigit():
                n += int(l.strip())
            else:
                cal_sum_list.append(n)
                n = 0

        fattest_elf = { cal_sum_list.index(max(cal_sum_list)) : max(cal_sum_list)}
        top_fatties = sorted(cal_sum_list)[-3:]
        print('answer', fattest_elf)
        print('answer2', sum(top_fatties))

if __name__ == "__main__":
    main()



