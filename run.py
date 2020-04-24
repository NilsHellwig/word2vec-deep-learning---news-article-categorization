import numpy as np
import pandas
import csv
import itertools

class Word2Vec:

    def __init__(self):
        self.dict = {}
        self.class_vectors = {}

    def read_in_vectors(self):
        with open("./vectors.txt", "r") as text_file:
            for line in itertools.islice(text_file, 0, 10000):
                word_in_line = line.split()[0]
                word_vector = line.split()
                word_vector.pop(0)
                self.dict[word_in_line] = word_vector

    def read_in_training_data(self):
        reader = csv.reader(open("./news_train_feed.csv"), delimiter=";")
        self.classes = set()
        self.counted_classes = dict()
        for row in reader:
            self.classes.add(row[0])
            try:
                print(row[0])
                self.counted_classes[row[0]] += 1
            except Exception:
                self.counted_classes[row[0]] = 0
        print("my_classes",self.counted_classes)

    def init_sentence_vector(self):
        reader = csv.reader(open("./news_test_feed.csv"), delimiter=";")
        self.vectors = dict()
        for row in reader:
            try:
                self.class_vectors[row[0]] = [sum(i) for i in zip(self.class_vectors[row[0]] , self.calculate_new_vector(row))]
            except Exception:
                self.class_vectors[row[0]] = self.calculate_new_vector(row)
        self.calculate_means()
        print(self.class_vectors)


    def calculate_new_vector(self,row):
        words_in_sentence = row[1].split()
        new_vector = []
        for index in range(300):
            new_vector.append(0.0)
        for word in words_in_sentence:
            try:
                for index in range(300):
                    sum = float(self.dict[word][index]) + new_vector[index]
                    new_vector[index] = sum
            except Exception:
                new_vector = new_vector
        print(row[0],new_vector)
        return new_vector

    def calculate_means(self):
        for cathegory in self.classes:
            print(cathegory)
            for index in range(300):
                self.class_vectors[cathegory][index] = self.class_vectors[cathegory][index] / self.amount_of_cathegory(cathegory)

    def amount_of_cathegory(self, cathegory):
        return self.counted_classes[cathegory]

    def init_read_input(self):
        text = input("prompt")  # Python 3


vec = Word2Vec()
init_read_input()
# self.dict includes all words and their vectors
vec.read_in_vectors()
vec.read_in_training_data()
vec.init_sentence_vector()
