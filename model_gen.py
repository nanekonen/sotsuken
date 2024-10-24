from gensim.models import Word2Vec
import time

time1 = time.time()

def read_corpus(file_path):
    with open(file_path, 'r', encoding='shift_jis', errors='ignore') as file:
        for line in file:
            yield line.strip().split()

file_path = './seg_code_Java2.txt'
corpus = list(read_corpus(file_path))

model = Word2Vec(sentences=corpus, vector_size=100, window=10, min_count=10, workers=4)

model.save("java_code_word2vec.model")

print(model.wv.most_similar('int'))

time2 = time.time()
print(time2-time1)
