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


    inizio = [int(w[4]) for w in wars if int(w[4]) > 0]
    counts = get_sorted_counts(inizio)
    counts.sort(key=lambda y: y[0])
    print(counts) 
    x, y = np.array(counts).transpose()


    plt.title("fine", fontsize=40)
    plt.xlabel("Mese")
    plt.ylabel("N° di guerre")
    plt.xlim((1, 12))
    #plt.yscale('log')

    #plt.ylim((0, 1800))
    
    plt.axvspan(0, 3.7, facecolor='blue', alpha=0.3)
    plt.axvspan(3.7, 6.7, facecolor='green', alpha=0.5)
    plt.axvspan(6.7, 9.7, facecolor='yellow', alpha=0.5)
    plt.axvspan(9.7, 12, facecolor='brown', alpha=0.5)

    plt.plot(x, y, c="black")
    plt.savefig("fine.png")
    plt.show()


if __name__ == "__main__":
    main()


