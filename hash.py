# hash.py
# Purpose: This file uses a custom hash function to create a hash table 
# Author: John Quinn
# Recieved help from geeksforgeeks: https://www.geeksforgeeks.org/dsa/hash-table-data-structure/

import time
import csv

class DataItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return f"{self.key}: {self.value}"
    
    def __repr__(self):
        return f"{self.key}: {self.value}"

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for x in range(size)]
    
    # concat each ascii number of each char in the key then turn it into an int
    # Python only supports typecasting strings of size 4300
    # find the modulo of that number against a large prime number
    # find the modulo of that number against the table size
    def hashFunction(self, key):
        PRIME_NUMBER = 611953
        hashValue = 0
        if type(key) == str:
            for char in key:
                hashValue = (hashValue * PRIME_NUMBER + ord(char)) % self.size
                
        # middle = asciiKey % PRIME_NUMBER

        return hashValue
    
    # find the index of the dataItem key
    # go that index in the table and append dataItem to it
    # if there are collisions they are stored in a list at this index
    def addDataItem(self, dataItem):
        index = self.hashFunction(dataItem.key)
        self.table[index].append(dataItem)
    
    # find the index of the dataItem key
    # if dataItem key is not in the table exit
    # otherwise remove that dataItem
    def removeDataItem(self, dataItem):
        index = self.hashFunction(dataItem.key)
        if dataItem.key not in self.table[index]:
            return
        self.table[index].remove(dataItem)

# helper function to create a hashtable given a list of DataItems
def createHashTable(dataItemList):
    hashTable = HashTable(len(dataItemList))
    for i in dataItemList:
        hashTable.addDataItem(i)
    return hashTable

# helper function to display the stats of each HashTable
def stats(hashTable):
    wastedRows = 0
    collisions = 0
    for i in range(hashTable.size):
        if len(hashTable.table[i]) == 0:
            wastedRows += 1
        if len(hashTable.table[i]) > 1:
            collisions += 1
    return wastedRows, collisions

if __name__ == "__main__":
    # Create Lists for keys and values
    movieTitleKeys = []
    movieTitleValues = []
    movieQuotesKeys = []
    movieQuotesValues = []

    with open("MOCK_DATA.csv", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            # Read in first column
            movieTitleKeys.append(row[0])
            # Read in everything but first column
            movieTitleValues.append(row[1:])
            # Read in last column
            movieQuotesKeys.append(row[-1])
            # Read in everything but last column
            movieQuotesValues.append(row[:8])

    # Pop the headers
    movieTitleKeys.pop(0)
    movieTitleValues.pop(0)
    movieQuotesKeys.pop(0)
    movieQuotesValues.pop(0)

    # Create list of DataItems
    movieTitleDataItemList = []
    movieQuoteDataItemList = []

    for i in range(len(movieTitleKeys)):
        movieTitleDataItemList.append(DataItem(movieTitleKeys[i], movieTitleValues[i]))
    for i in range(len(movieQuotesKeys)):
        movieQuoteDataItemList.append(DataItem(movieQuotesKeys[i], movieQuotesValues[i]))
    
    titleStart = time.time()
    movieTitleHashTable = createHashTable(movieTitleDataItemList)
    titleEnd = time.time()
    wastedRowsTitle, collisionsTitle = stats(movieTitleHashTable)
    print(f"Movie Title Keys: Wasted Rows: {wastedRowsTitle}, Collisions: {collisionsTitle}, Time: {titleEnd-titleStart}")

    quoteStart = time.time()
    movieQuoteHashTable = createHashTable(movieQuoteDataItemList)
    quoteEnd = time.time()
    wastedRowsQuote, collisionsQuote = stats(movieQuoteHashTable)
    print(f"Movie Quote Keys: Wasted Rows: {wastedRowsQuote}, Collisions: {collisionsQuote}, Time: {quoteEnd-quoteStart}")