import re 
from konlpy.tag import Okt
from keras.preprocessing.text import Tokenizer
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences  # 시퀀스를 패딩하는 데 사용되는 라이브러리


class AI_Service:
    def AI_predict(new_sentence):
        new_sentence = re.sub(r'[^ㄱ-ㅎㅏ-ㅣ가-힣 ]','', new_sentence)
        new_sentence = Okt().morphs(new_sentence, stem=True) # 토큰화
        encoded = Tokenizer().texts_to_sequences([new_sentence]) # 정수 인코딩
        pad_new = pad_sequences(encoded, maxlen = 100) # 패딩
        loaded_model = load_model("./app/static/best_model.h5")
        score = float(loaded_model.predict(pad_new)) # 예측
        return score