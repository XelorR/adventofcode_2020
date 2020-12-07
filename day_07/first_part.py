with open("input.txt") as input_file:
    INPUT = input_file.read()


def count_bags_which_contain(bag_list: list, looking_for: str) -> set:
    found_list = []
    for bag in bag_list:
        sep = bag.find(' bags contain')
        if looking_for in bag[sep:]:
            found_list.append(bag[:sep])
            found_list.extend(count_bags_which_contain(bag_list, bag[:sep]))
    return set(found_list)


print(len(count_bags_which_contain(INPUT.splitlines(), "shiny gold")))
