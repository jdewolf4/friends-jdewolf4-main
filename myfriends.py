"""Assignment 1: Friend of a Friend

Please complete these functions, to answer queries given a dataset of
friendship relations, that meet the specifications of the handout
and docstrings below.

Notes:
- you should create and test your own scenarios to fully test your functions, 
  including testing of "edge cases"
"""

from py_friends.friends import Friends

"""
************** READ THIS ***************
************** READ THIS ***************
************** READ THIS ***************
************** READ THIS ***************
************** READ THIS ***************

If you worked in a group on this project, please type the EIDs of your groupmates below (do not include yourself).
Leave it as TODO otherwise.
Groupmate 1: TODO
Groupmate 2: TODO
"""

def load_pairs(filename):
    """
    Args:
        filename (str): name of input file

    Returns:
        List of pairs, where each pair is a Tuple of two strings

    Notes:
    - Each non-empty line in the input file contains two strings, that
      are separated by one or more space characters.
    - You should remove whitespace characters, and skip over empty input lines.
    """
    list_of_pairs = []
    with open(filename, 'rt') as infile:

# ------------ BEGIN YOUR CODE ------------
        for line in infile:
            line_strip = line.rstrip()
            split_line = line_strip.split(" ")
            tuple_split_line = tuple(split_line)
            list_of_pairs.append(tuple_split_line)
        #print(list_of_pairs)
        
        # implement your code here


# ------------ END YOUR CODE ------------

    return list_of_pairs 

def make_friends_directory(pairs):
    """Create a directory of persons, for looking up immediate friends

    Args:
        pairs (List[Tuple[str, str]]): list of pairs

    Returns:
        Dict[str, Set] where each key is a person, with value being the set of 
        related persons given in the input list of pairs

    Notes:
    - you should infer from the input that relationships are two-way: 
      if given a pair (x,y), then assume that y is a friend of x, and x is 
      a friend of y
    - no own-relationships: ignore pairs of the form (x, x)
    """
    directory = dict()

    # ------------ BEGIN YOUR CODE ------------

    dict_temp = dict()
    for pair in pairs:
        dict_temp.setdefault(pair[0], []).append(pair[1])
        dict_temp.setdefault(pair[1], []).append(pair[0])

    for key, value in dict_temp.items():
        directory.setdefault(key, set(value))
        # implement your code here


    # ------------ END YOUR CODE ------------

    return directory


def find_all_number_of_friends(my_dir):
    """List every person in the directory by the number of friends each has

    Returns a sorted (in decreasing order by number of friends) list 
    of 2-tuples, where each tuples has the person's name as the first element,
    the the number of friends as the second element.
    """
    friends_list = []

    # ------------ BEGIN YOUR CODE ------------

    for dict_key, dict_value in my_dir.items():
        friends_list.append((dict_key, len(dict_value)))

    def num_sort(num_sort_list):
        return num_sort_list[1]

    def alpha_sort(alpha_sort_list):
        return alpha_sort_list[0]

    friends_list.sort(reverse=True, key=num_sort)
    friends_list.sort(reverse=False, key=alpha_sort)
    friends_list.sort(reverse=True, key=num_sort)
    #pass    # implement your code here
    

    # ------------ END YOUR CODE ------------

    return friends_list


def make_team_roster(person, my_dir):
    """Returns str encoding of a person's team of friends of friends
    Args:
        person (str): the team leader's name
        my_dir (Dict): dictionary of all relationships

    Returns:
        str of the form 'A_B_D_G' where the underscore '_' is the
        separator character, and the first substring is the 
        team leader's name, i.e. A.  Subsequent unique substrings are 
        friends of A or friends of friends of A, in ascii order
        and excluding the team leader's name (i.e. A only appears
        as the first substring)

    Notes:
    - Team is drawn from only within two circles of A -- friends of A, plus 
      their immediate friends only
    """
    assert person in my_dir
    label = person

    # ------------ BEGIN YOUR CODE ------------

    
    #pass    # implement your code here
    label_temp = {}
    friend_label_temp = []

    for friend in my_dir[person]:
        friend_label_temp.append(friend)
        friend_label_temp.sort()
        for friend_friend in my_dir[friend]:
            if friend_friend != person:
                if friend_friend not in friend_label_temp:
                    friend_label_temp.append(friend_friend)
    label_temp = set(friend_label_temp)
    friend_label_temp = list(label_temp)
    friend_label_temp.sort()
    for name in friend_label_temp:
        label += "_" + name

    # ------------ END YOUR CODE ------------

    return label


def find_smallest_team(my_dir):
    """Find team with smallest size, and return its roster label str
    - if ties, return the team roster label that is first in ascii order
    """
    smallest_teams = []

    # ------------ BEGIN YOUR CODE


    #pass    # implement your code here
    for team in my_dir:
        n_dict = dict()
        n_dict.setdefault(make_team_roster(team, my_dir), make_team_roster(team, my_dir).count('_'))
        team_size_temp = 0
        smallest_teams = []
        for nk, nv in n_dict.items():
            if nv >= team_size_temp:
                team_size_temp = nv
        for nk2, nv2 in n_dict.items():
            if team_size_temp == nv2:
                smallest_teams.append(nk2)
        smallest_teams.sort()
    
    # ------------ END YOUR CODE

    return smallest_teams[0] if smallest_teams else ""



if __name__ == '__main__':
    # To run and examine your function calls

    print('\n1. run load_pairs')
    my_pairs = load_pairs('myfriends.txt')
    print(my_pairs)

    print('\n2. run make_directory')
    my_dir = make_friends_directory(my_pairs)
    print(my_dir) 

    print('\n3. run find_all_number_of_friends')
    print(find_all_number_of_friends(my_dir))

    print('\n4. run make_team_roster')
    my_person = 'HAN'   # test with this person as team leader
    team_roster = make_team_roster(my_person, my_dir)
    print(team_roster) 

    print('\n5. run find_smallest_team')
    print(find_smallest_team(my_dir))

    print('\n6. run Friends iterator')
    friends_iterator = Friends(my_dir)
    for num, pair in enumerate(friends_iterator):
        print(num, pair)
        if num == 10:
            break
    print(len(list(friends_iterator)) + num)
