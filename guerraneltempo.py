import csv
import numpy as np
import matplotlib.pyplot as plt


def get_sorted_counts(sequence):
    counts = {}

    for x in sequence:
        if (x//10) * 10 in counts:
            counts[(x//10) * 10] += 1
        else:
            counts[(x//10) * 10] = 1

    pairs = counts.items()
    return sorted(pairs, key=lambda p:p[1], reverse=True)


def main():
    with open('Dataset_guerra.csv', 'r') as wars_data:
      wars_data = csv.reader(wars_data, delimiter=',', )
      wars = list(wars_data)[1:]

    region = "Asia Sud-Est"
    c = "#ffffbf"
    
    years = [int(w[2]) for w in wars if ((int(w[2]) != 0) and (int(w[2]) < 2000) and w[5]==region)]
    counts = get_sorted_counts(years)
    counts.sort(key=lambda y: y[0]) #ORDINA COUNTS IN BASE ALL'ANNO
    print(counts) 
    x, y = np.array(counts).transpose()
    z = np.polyfit(x, y, 5)
    p = np.poly1d(z)
    plt.plot(x,p(x),"r--")

    plt.title(region, fontsize=40)
    plt.xlabel("Anno")
    plt.ylabel("N° di guerre")
    
    plt.bar(x, y, width=5, color=c)
    plt.ylim((0, 100))
    plt.savefig("Asia Sud-Est-ylim.png")
    plt.show()


if __name__ == "__main__":
    main()


'''
Nord America 1 #91bfdb
Sud America 2 #d73027
Europa 3 4 #4575b4
Medio Oriente 5 #fee090
Africa 6 7 8 #fc8d59
Asia Centrale 9 #e0f3f8
Asia Sud-Est 10 11 12 #ffffbf
'''
