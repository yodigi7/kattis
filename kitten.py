def get_branches():
    ret_dict = {}
    inp_list = input().split()
    while not inp_list[0] == "-1":
        to_branch = int(inp_list[0])
        from_branches = inp_list[1:]
        for branch in from_branches:
            ret_dict[int(branch)] = to_branch
        inp_list = input().split()
    return ret_dict


if __name__ == '__main__':
    current_branch = int(input())
    branch_dict = get_branches()
    path = []
    while current_branch in branch_dict.keys():
        path.append(str(current_branch))
        current_branch = branch_dict[current_branch]
    path.append(str(current_branch))
    print(" ".join(path))
