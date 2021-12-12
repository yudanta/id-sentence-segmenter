# import sentence segmentation class 
from idsentsegmenter.sentence_segmentation import SentenceSegmentation

news_content = ""
# open sample news content 
with open("news_example.txt", "r") as fio:
    news_content = fio.read()

print("news content: ")
print(news_content)

print("-" * 82)

# create sentence segmenter instance from SentenceSegmentation class
sentence_segmenter = SentenceSegmentation()

# parse text to sentences 
sentences = sentence_segmenter.get_sentences(news_content)

print("news sentences: ")
# print sentences from previous sentence segmentation process
for i, sent in enumerate(sentences):
    print(i, sent)