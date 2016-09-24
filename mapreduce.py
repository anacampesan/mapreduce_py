from collections import Counter
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

def mapper(path):
    # opens the file, reads it and splits into single words
    text = open(path, 'r').read().strip().split()
    result = open('mapper_result.txt', 'w')
    for word in text:
        result.write('%s ' % word)

def reducer(mapper_result):
    text = open(mapper_result).read().split()
    freq = Counter(text)
    dataset = pd.DataFrame.from_dict(freq, orient="index")
    dataset.columns = ['Frequency']
    dataset.to_csv('reducer_result.csv')



mapper('tweets.txt')
reducer('mapper_result.txt')

final_result = pd.read_csv('reducer_result.csv')
print final_result.sort_values(by=['Frequency'])
