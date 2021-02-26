from bs4 import BeautifulSoup
 from collections import Counter
 import numpy as np
 import matplotlib.pyplot as plt
 import requests
 import re
 
 
 def get_content(article_name): #get content from the web page
 	return BeautifulSoup(requests.get("https://en.wikipedia.org/wiki/" + article_name).text, 'lxml')
 
 def merge_contents(soup): # get only the usefull data, and collecting it in string
 	text = ""
 	for article in soup.find_all('p'): text += "".join(article.text)
 	return text
 
 def tokenize(text): #clean the usefull data
 	return re.sub("[\(\[].*?[\)\]]", "", text).replace(",","").replace('-'," ").replace("  "," ").replace(".","").replace("\n","").split(" ")
 
 def lower_collection(text): #change all text to the lower letters
 	return [i.lower() for i in text]
 
 def count_frequency(collection): # count how many times a word comes across
 	return Counter(collection)
 
 def print_most_frequent(frequencies,n): #print the n number the most frequencies words
 	print(str(n) + " the most common words:")
 	for word in frequencies.most_common(n):
 		print('"' + list(word)[0]+'"' + " occurs " + str(list(word)[1]) + " time")
 
 def vizualizing(data): # display the chart with all words
 	data = data.most_common(20)
 	labels, values = zip(*dict(data).items())
 	indSort = np.argsort(values)
 	labels,values = np.array(labels)[indSort],np.array(values)[indSort]
 	plt.barh(labels,values)
 	plt.title('Most common 20 words in article')
 	plt.show()
 
 def remove_stop_words(words, stop_words): # removing the trash (stop words)
 	return [i for i in words if i not in stop_words]
 
 def vizualizing_without_trash(data): #display the chart without the trash (stop words)
 	data = data.most_common(25)
 	labels, values = zip(*dict(data).items())
 	indSort = np.argsort(values)
 	labels,values = np.array(labels)[indSort],np.array(values)[indSort]
 	plt.barh(labels,values)
 	plt.title('Most common 25 words in article')
 	plt.show()
 
 stop_words = ['the',"of","and",'in',"to","is","a","by","that","was","are","from","for","it","as","at","be","this","have","on","this","these","which","into","because","most","about","with","has","can",'other','its','out','being',"were","an",'all',"over","used","less","than",'while','above','percent',"very","where","near",'levels','so','or',"may","been",'high']
 
 ###################
 ####DRIVE CODE#####
 ###################
 data = get_content("Ozone_layer")
 merge_content = merge_contents(data)
 collection = tokenize(merge_content)
 lower_case = lower_collection(collection)
 frequencies = count_frequency(lower_case)
 print_most_frequent(frequencies, 10)
 vizualizing = vizualizing(frequencies)
 
 # filtered words (without stop words)
 filtered_collection = remove_stop_words(lower_case, stop_words)
 frequencies_without_trash = count_frequency(filtered_collection)
 vizualizing_without_trash = vizualizing_without_trash(frequencies_without_trash)
