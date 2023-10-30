
from teanaps.nlp import MorphologicalAnalyzer

ma = MorphologicalAnalyzer()




ma.set_tagger("okt")



text = "손흥민이 골을 작렬하며 토트넘 홋스퍼의 승리를 이끌었다."
pos_list = ma.parse(text)
print(pos_list)
