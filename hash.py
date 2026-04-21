# hash.py
# Purpose: This file uses a custom hash function to create a hash table 
# Author: John Quinn
# Recieved help from geeksforgeeks: https://www.geeksforgeeks.org/dsa/hash-table-data-structure/

import time
import csv
import random

class DataItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return f"{self.key}: {self.value}"
    
    def __repr__(self):
        return f"{self.key}: {self.value}"

class hash:
    # concat each ascii number of each char in the key then turn it into an int
    # Python only supports typecasting strings of size 4300
    # find the modulo of that number against a large prime number
    # find the modulo of that number against the table size
    def hashFunction(self, key):
        PRIME_NUMBER_LIST = [601021, 601031, 601037, 601039, 601043, 601061, 601067, 601079, 601093, 601127, 601147, 601187, 601189, 601193, 601201, 601207, 601219, 601231, 601241, 601247, 601259, 601267, 601283, 601291, 601297, 601309, 601313, 601319, 601333, 601339, 601357, 601379, 601397, 601411, 601423, 601439, 601451, 601457, 601487, 601507, 601541, 601543, 601589, 601591, 601607, 601631, 601651, 601669, 601687, 601697, 601717, 601747, 601751, 601759, 601763, 601771, 601801, 601807, 601813, 601819, 601823, 601831, 601849, 601873, 601883, 601889, 601897, 601903, 601943, 601949, 601961, 601969, 601981]
        hashValue = PRIME_NUMBER_LIST[random.randint(0, len(PRIME_NUMBER_LIST) - 1)]
        if type(key) == str:
            for char in key:
                hashValue = ((hashValue * PRIME_NUMBER_LIST[random.randint(0, len(PRIME_NUMBER_LIST) - 1)]) + ord(char))
                hashValue = hashValue // PRIME_NUMBER_LIST[random.randint(0, len(PRIME_NUMBER_LIST) - 1)]
        
        return hashValue % len(self.table)

class LinkedListHashTable(hash):
    def __init__(self, size):
        self.size = size
        self.table = [[] for i in range(size)]
        self.collisions = 0
    # find the index of the dataItem key
    # go that index in the table and append dataItem to it
    # if there are collisions they are stored in a list at this index
    def addDataItem(self, dataItem):
        index = self.hashFunction(dataItem.key)
        if len(self.table[index]) > 0:
            self.collisions += len(self.table[index])
        self.table[index].append(dataItem)

class LinearProbeHashTable(hash):
    def __init__(self, size, capacity):
        self.size = size
        self.capacity = capacity
        self.table = [None] * capacity
        self.collisions = 0

    # if row is none insert DataItem
    # if row is not none iterate through table until an empty row is found
    # if index reaches start_index then table is full and exit
    def addDataItem(self, dataItem):
        index = self.hashFunction(dataItem.key)
        start_index = index
        if self.table[index] == None:
            self.table[index] = dataItem
        else:
            while(self.table[index] != None):
                index = (index + 1) % self.capacity
                self.collisions += 1
                if index == start_index:
                    return
            self.table[index] = dataItem



# helper function to create a linked list hash table given a list of DataItems
def createLinkedListHashTable(dataItemList):
    hashTable = LinkedListHashTable(len(dataItemList))
    for i in dataItemList:
        hashTable.addDataItem(i)
    return hashTable

# helper function to create a linear probe hash table given a list of DataItems
def createLinearProbeHashTable(dataItemList):
    hashTable = LinearProbeHashTable(len(dataItemList), len(dataItemList)*2)
    for i in dataItemList:
        hashTable.addDataItem(i)
    return hashTable

def stats(hashTable, linkedList=True):
    collisions = hashTable.collisions
    wastedRows = 0
    if linkedList:
        for i in range(hashTable.size):
            if len(hashTable.table[i]) == 0:
                wastedRows += 1
    else:
        for i in range(hashTable.size):
            if hashTable.table[i] == None:
                wastedRows += 1
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
    movieTitleHashTable = createLinkedListHashTable(movieTitleDataItemList)
    titleEnd = time.time()
    wastedRowsTitle, collisionsTitle = stats(movieTitleHashTable)
    print(f"Movie Title Keys - Linked List: Wasted Rows: {wastedRowsTitle}, Collisions: {collisionsTitle}, Time: {titleEnd-titleStart}")

    quoteStart = time.time()
    movieQuoteHashTable = createLinearProbeHashTable(movieQuoteDataItemList)
    quoteEnd = time.time()
    wastedRowsQuote, collisionsQuote = stats(movieQuoteHashTable, linkedList=False)
    print(f"Movie Quote Keys - Linear Probe: Wasted Rows: {wastedRowsQuote}, Collisions: {collisionsQuote}, Time: {quoteEnd-quoteStart}")