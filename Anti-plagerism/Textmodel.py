#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 19:27:54 2019

@author: yuanmingchai
"""

import math

class TextModel:
    def __init__(self, model_name):
        """ Constructor for the class TextModel"""
        self.name = model_name
        self.words = {}
        self.word_lengths = {}
        self.stems = {}
        self.sentence_lengths = {}
        self.word_pair = {}
        
    def __repr__(self):
        """Return a string representation of the TextModel."""
        s = 'text model name: ' + self.name + '\n'
        s += '  number of words: ' + str(len(self.words)) + '\n'
        s += '  number of word lengths: ' + str(len(self.word_lengths)) + '\n'
        s += '  number of stems: ' + str(len(self.stems)) + '\n'
        s += '  number of sentence lengths: ' + str(len(self.sentence_lengths)) + '\n'
        s += '  number of adjacent word pairs: ' + str(len(self.word_pair))
        return s
    
    def add_string(self, s):
        """Analyzes the string txt and adds its pieces
           to all of the dictionaries in this text model.
        """
        # Add code to clean the text and split it into a list of words.
        # *Hint:* Call one of the functions you have already written!
        word_list = clean_text(s)
        # Template for updating the words dictionary.
        """ word pair """
        for n in range(len(word_list[:-1])):
            pair = word_list[n] + word_list[n+1]
            if pair not in self.word_pair:
                self.word_pair[pair] = 1
            else:
                self.word_pair[pair] += 1
                
        """ word lengths """
        for w in word_list:
            if len(w) not in self.word_lengths:
                self.word_lengths[len(w)] = 1
            else:
                self.word_lengths[len(w)] += 1
                
        """ word choices """
        for w in word_list:
            if w not in self.words:
                self.words[w] = 1
            else:
                self.words[w] += 1
        
        """ stem """
        stem_wordlist = [stem(w) for w in word_list]
        for w in stem_wordlist:
            if w not in self.stems:
                self.stems[w] = 1
            else:
                self.stems[w] += 1
        
        """ sentence length """
        sentence = s.split()
        num = 0
        for each in sentence:
            num += 1
            if len(each) >=1 and each[-1] == '.' or each[-1] == '!' or each[-1] == '?':
                if num not in self.sentence_lengths:
                    self.sentence_lengths[num] = 1
                else: 
                    self.sentence_lengths[num] += 1
                num = 0
                
        
            # either add a new key-value pair for w
            # or update the existing key-value pair.
            
        # Add code to update other feature dictionaries.
        
    def add_file(self, filename):
        """ adds all of the text in the file identified by filename to the model. 
            input filename: a file
        """
        f = open(filename, 'r', encoding='utf8', errors='ignore')
        l = f.read()
        f.close()
        self.add_string(l)
        
        
    def save_model(self):
        """ saves the TextModel object self by writing its various 
            feature dictionaries to files. 
        """
        f1 = open(self.name + '_' + 'words', 'w')
        f2 = open(self.name + '_' + 'word_lengths', 'w')
        f3 = open(self.name + '_' + 'stems', 'w')
        f4 = open(self.name + '_' + 'sentence_lengths', 'w')
        f5 = open(self.name + '_' + 'word_pair', 'w')
        f1.write(str(self.words))
        f2.write(str(self.word_lengths))
        f3.write(str(self.stems))
        f4.write(str(self.sentence_lengths))
        f5.write(str(self.word_pair))
        f1.close()    
        f2.close()  
        f3.close()    
        f4.close()
        f5.close()    
        
    
    def read_model(self):
        """ reads the stored dictionaries for the called TextModel object 
            from their files and assigns them to the attributes of the called 
            TextModel.
        """
        f1 = open(self.name + '_' + 'words', 'r')
        f2 = open(self.name + '_' + 'word_lengths', 'r')
        f3 = open(self.name + '_' + 'stems', 'r')
        f4 = open(self.name + '_' + 'sentence_lengths', 'r')
        f5 = open(self.name + '_' + 'word_pair', 'r')
        d_str1 = f1.read() 
        d_str2 = f2.read() 
        d_str3 = f3.read() 
        d_str4 = f4.read() 
        d_str5 = f5.read() 
        self.words = dict(eval(d_str1))
        self.word_lengths= dict(eval(d_str2))
        self.stems = dict(eval(d_str3))
        self.sentence_lengths = dict(eval(d_str4))
        self.word_pair = dict(eval(d_str5))
        
    def similarity_scores(self, other):
        """ computes and returns a list of log similarity scores 
            measuring the similarity of self and other
        """
        word_score = compare_dictionaries(other.words, self.words)
        word_lengths_scores = compare_dictionaries(other.word_lengths, self.word_lengths)
        stems_scores = compare_dictionaries(other.stems, self.stems)
        sentence_lengths_socre = compare_dictionaries(other.sentence_lengths, self.sentence_lengths)
        word_pair_score = compare_dictionaries(other.word_pair, self.word_pair)
        return [word_score, word_lengths_scores, stems_scores, sentence_lengths_socre, word_pair_score]

    def classify(self, source1, source2):
        """ compares the called TextModel object (self) to two other “source” 
            TextModel objects (source1 and source2) and determines which of these
            other TextModels is the more likely source of the called TextModel.
        """
        decision = ''
        scores1 = self.similarity_scores(source1)
        scores2 = self.similarity_scores(source2)
        print('scores for', source1.name, ':', scores1)
        print('scores for', source2.name, ':', scores2)
        weighted_sum1 = 10*scores1[0] + 5*scores1[1] + 7*scores1[2] + 4*scores1[3] + 10*scores1[4]
        weighted_sum2 = 10*scores2[0] + 5*scores2[1] + 7*scores2[2] + 4*scores2[3] + 10*scores1[4]
        if weighted_sum1 > weighted_sum2:
            decision = source1.name
        else:
            decision = source2.name
        print(self.name + ' is more likely to have come from ' + decision)
            
    
def clean_text(txt):
    """ takes a string of text txt as a parameter and returns a list containing 
        the words in txt after it has been “cleaned”.
    """
    txtf = txt.lower()
    for i in txtf:
        if i == ',' or i == '?' or i == '!' or i == '.':
            txtf = txtf.replace(i, '')
    return txtf.split()

def stem(word):
    if word[-3:] == 'ing' and len(word) >= 5:
        if word[-4] == word[-5] and word != 'killing' and word != 'smelling' and word != 'kissing':
            word = word[:-4]
        else:
            word = word[:-3]
    elif word[-2:] == 'ly' and len(word) >= 4:
        if word[-3] == word[-4]:
            word = word[:-3]
        else:
            word = word[:-2]
    elif word[-1] == 'e' and word != 'the' and word != 'she' and word != 'he':
        word = word[:-1]
    elif word[-2:] == 'er':
        word = word[:-2]
    elif word[-4:] == 'tion' or word[-4:] == 'sion' or word[-4:] == 'list':
        word = word[:-5]
    elif word[-4:] == 'tive' or word[-4:] == 'sive':
        word = word[:-5]
    elif word[-3:] == 'ful':
        word = stem(word[:-3])
    elif word[-1] == 's':
        word = stem(word[:-1])
    elif word[-1] == 'y':
        word = word[:-1] + 'i'
    return word

def compare_dictionaries(d1, d2):
    """ take two feature dictionaries d1 and d2 as inputs, and it should 
        compute and return their log similarity score. 
    """
    score = 0
    total = 0
    for w in d1:
        total += d1[w]
    for w in d2:
        if w in d1:
            score += d2[w] * math.log(d1[w] / total)
        else:
            score += math.log(0.5 / total)
    return score


def test():
    """ your docstring goes here """
    source1 = TextModel('source1')
    source1.add_string('It is interesting that she is interested.')

    source2 = TextModel('source2')
    source2.add_string('I am very, very excited about this!')

    mystery = TextModel('mystery')
    mystery.add_string('Is he interested? No, but I am.')
    mystery.classify(source1, source2)
    


def run_tests():
    """ compare the selected mystery texts and compare to the other two source texts
        and tell which one is the writing style more similar to
    """

    source3 = TextModel('usnews')
    source3.add_file('usnews_source_text.txt')

    source4 = TextModel('newyorktimes')
    source4.add_file('newyorktimes_source_text.txt')
    
    new1 = TextModel('wr100')
    new1.add_file('wr100_source_text.txt')
    new1.classify(source3, source4)

    new2 = TextModel('bostonglobe')
    new2.add_file('bostonglobe_source_text.txt')
    new2.classify(source3, source4)
    
    new3 = TextModel('rowling')
    new3.add_file('rowling_source_text.txt')
    new3.classify(source3, source4)
    
    new4 = TextModel('shakespeare')
    new4.add_file('shakespeare_source_text.txt')
    new4.classify(source3, source4)
    
    
    
    
