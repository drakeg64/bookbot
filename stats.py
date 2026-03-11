def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_char(text):
    to_lowercase = text.lower()
    char_count = {}
    for char in to_lowercase:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    return(char_count)

def sort_on(items):
    return items["num"]

def sort_by_count(dict):
    sorted_list = []
    for item in dict:
        new_dict = {}
        new_dict["char"] = item
        new_dict["num"] = dict[item]
        sorted_list.append(new_dict)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
    
    
