from nltk.corpus import wordnet as wn
import argparse


def which_path(path_list):  # Computing the shortest or longest path among all the paths to root node in the tree
    leng_list = [len(path) for path in path_list]
    if mode == 'shortest':
        which_len = min(leng_list)
    else:
        which_len = max(leng_list)
    All_len.append(which_len)
    return leng_list.index(which_len)


def travers_tree(synset):  # Generating the synset hypernym chains to the root node
    chain = ""
    all_path = synset.hypernym_paths()
    if len(all_path) > 0:
        wh_path = which_path(all_path)
        for node in reversed(range(len(all_path[wh_path]))):
            chain += all_path[wh_path][node].name() + "\t"
    else:
        for node in reversed(range(len(all_path[0]))):
            chain += all_path[0][node].name() + "\t"
    output.write(chain + "\n")


def run():
    for synset in range(len(AllSynsets)):  # Iterate over all synsets to get path to the root
        if len(AllSynsets) % (synset + 1) == 1000:
            print("Progress :" + str(round((synset / len(AllSynsets)) * 100, 2)) + "%")
        travers_tree(AllSynsets[synset])

    output.close()
    print("Minumum Synset Chain Distance is: " + str(min(All_len)))
    print("Maximum Synset Chain Distance is: " + str(max(All_len)))
    print("Average Synset Chain Distance is: " + str(round((sum(All_len) / len(All_len)), 2)))


if __name__ == "__main__":
    output = open("WordNet_Synset_paths.txt", 'w')
    AllSynsets = list(wn.all_synsets('n'))  # The list of all nominal synsets in WordNet
    All_len = []
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "mode")  # Command line argument to define the mode of path finding ('shortest' or 'longest' path)
    args = parser.parse_args()
    mode = args.mode
    run()
