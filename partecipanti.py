import csv
import numpy as np
import matplotlib.pyplot as plt


def get_sorted_counts(sequence):
    counts = {}

    for x in sequence:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1

    pairs = counts.items()
    return sorted(pairs, key=lambda p:p[1], reverse=True)


def main():
    with open('Dataset_guerra.csv', 'r') as wars_data:
      wars_data = csv.reader(wars_data, delimiter=',', )
      wars = list(wars_data)[1:]


    partecipanti = [int(w[0]) for w in wars if int(w[0]) >= 0]
    counts = get_sorted_counts(partecipanti)
    counts.sort(key=lambda y: y[0])
    print(counts) 
    x, y = np.array(counts).transpose()


    #plt.title(region, fontsize=40)
    plt.xlabel("Partecipanti")
    plt.ylabel("N° di guerre")
    plt.xlim((2, 10))
    #plt.yscale('log')

    plt.ylim((0, 3200))
    plt.plot(x, y)
    plt.savefig("partecipanti.png")
    plt.show()


if __name__ == "__main__":
    main()


