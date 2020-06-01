from nltk.corpus import wordnet as wn

output = open("WordNet_Synset_paths.txt", 'w')
AllSynsets = list(wn.all_synsets('n'))  # The list of all nominal synsets in WordNet


def shortest(path_list):  # Computing the shortest path among all the paths to root node in the tree
    leng_list = [len(path) for path in path_list]
    min_len = min(leng_list)
    return leng_list.index(min_len)


def travers_tree(synset):  # Generating the synset hypernym chains to the root node 
    chain = ""
    all_path = synset.hypernym_paths()
    if len(all_path) > 0:
        sh_path = shortest(all_path)
        for node in reversed(range(len(all_path[sh_path]))):
            chain += all_path[sh_path][node].name() + "\t"
    else:
        for node in reversed(range(len(all_path[0]))):
            chain += all_path[0][node].name() + "\t"
    output.write(chain + "\n")


for synset in range(len(AllSynsets)):  # Iterate over all synsets to get path to the root
    if len(AllSynsets) % (synset + 1) == 1000:
        print("Progress :" + str(round((synset / len(AllSynsets)) * 100, 2)) + "%")
    travers_tree(AllSynsets[synset])

output.close()
