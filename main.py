import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as sp


def main():

    while True:
        df = pd.read_csv('dataset1.csv')
        kickoff = df.iloc[0]
        punt = df.iloc[1]
        rushing = df.iloc[2]
        passing = df.iloc[3]
        other = df.iloc[4]
        print("the type of play with the most head injuries(96-02) was passing with: ",df['head injuries: 96-01'].max(),
             "In 02-07 it was also passing with: " ,df['head injuries: 02-07'].max())

        x = input("Enter type of play for stats(kickoff, punt, rushing, passing or other): ")
        if x == 'kickoff':
            print(kickoff)
        elif x == 'punt':
            print(punt)
        elif x == 'rushing':
            print(rushing)
        elif x == 'passing':
            print(passing)
        elif x == 'other':
            print(other)
        elif x == 'all':
            print(kickoff, punt, rushing, passing, other) # Incidence Density is measuring how often something occurs




        y = input("Display graph?")
        if y == 'yes':
            plt.figure(figsize=(10, 6))
            plt.bar(df['play type'], df['head injuries: 96-01'], label='head injuries: 96-01', color='red', alpha=0.6)
            plt.bar(df['play type'], df['head injuries: 02-07'], label='head injuries: 02-07', color='blue', alpha=0.6)
            plt.xlabel('play type')
            plt.ylabel('Number of Head Injuries')
            plt.title('Comparison of Head Injuries by Play Type')
            plt.xticks(rotation=45)
            plt.legend()
            plt.tight_layout()
            plt.scatter(x=df['play type'], y=df['head injuries: 96-01'], label='96-01')
            plt.scatter(x=df['play type'], y=df['head injuries: 02-07'], label='02-07')
            plt.legend()
            plt.show()

        print("---------------------")
        df2 = pd.read_csv('Sheet 3-Table 1.csv')
        print("Confidence intervals by position: ")
        print(df2)
        print("---------------------")
        print("Number of head injuries: 1996-2001")
        print(df2[['position','number of head injuries: 1996-2001']])
        print("---------------------")
        print("Number of head injuries: 2002-2007")
        print(df2[['position','number of head injuries: 2002-2007']])




        while True:
            answer = str(input('Run again? (y/n): '))
            if answer in ('y', 'n'):
                break
            print("invalid input.")
        if answer == 'y':
            continue
        else:
            break





if __name__ == '__main__':
    main()


