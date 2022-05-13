import csv
import numpy as np
import matplotlib.pyplot as plt


def main():
    with open('Dataset_guerra.csv', 'r') as wars_data:
      wars_data = csv.reader(wars_data, delimiter=',', )
      wars = list(wars_data)[1:]

    regions = ["Nord america", "Sud America", "Europa", "Medio Oriente", "Africa", "Asia Centrale", "Asia Sud-Est"]

    lista = []
    
    for region in regions:   
        deaths = [int(w[1]) for w in wars if ((int(w[1]) > 0) and (w[5] == region) and (int(w[1]) < 5000))]
        lista.append(deaths)
        print(deaths)
        print(region)

  
    fig, ax = plt.subplots()
    ax.boxplot(lista, vert=False)
    ax.set_yticklabels(regions)
    
    plt.xlabel("N° di morti")
    
    plt.savefig("mortdiecimila.png")
    plt.show()


if __name__ == "__main__":
    main()

