import csv
import numpy as np
import matplotlib.pyplot as plt



def main():
    with open('Dataset_guerra.csv', 'r') as wars_data:
      wars_data = csv.reader(wars_data, delimiter=',', )
      wars = list(wars_data)[1:]

    minimo = 1400
    massimo = 1500
    y = [] 
    for i in range(6):
        secolo = [int(w[7]) for w in wars if ((int(w[2]) >= minimo) and (int(w[2]) < massimo))]
        n_guerre = 0
        somma = 0
        for guerra in secolo:
            n_guerre += 1
            somma += guerra
            
        media = somma/n_guerre
        y.append(media)
        minimo += 100
        massimo += 100

    x = ["15esimo", "16esimo", "17esimo", "18esimo", "19esimo", "20esimo"]
    c = ["red", "green", "blue", "orange", "purple", "pink"]
    plt.title("differenze tra i secoli", fontsize=40)
    plt.xlabel("Secolo")
    plt.ylabel("Durata in anni")

    plt.bar(x, y, color=c)
    plt.savefig("Durateneisecoli.png")
    plt.show()


if __name__ == "__main__":
    main()


