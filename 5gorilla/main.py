import fileinput

def load_data():
    chars = list()
    costs = list()
    queries = list()
    for i, line in enumerate(fileinput.input()):
        line = line.strip().split(" ")

        if fileinput.isfirstline():
            chars = line
        elif i <= len(chars):
            costs.append(line)
        elif i > len(chars) + 1:
            queries.append(line)

    
    return chars, costs, queries



if __name__ == "__main__":
    chars, costs, queries = load_data()
    print(chars, costs, queries)