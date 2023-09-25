import re 
from konlpy.tag import Okt
from keras.preprocessing.text import Tokenizer
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences  # 시퀀스를 패딩하는 데 사용되는 라이브러리
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from .movie_service import MoiveService



class AI_Service:
    def AI_predict(new_sentence):
        new_sentence = re.sub(r'[^ㄱ-ㅎㅏ-ㅣ가-힣 ]','', new_sentence)
        new_sentence = Okt().morphs(new_sentence, stem=True) # 토큰화
        encoded = Tokenizer().texts_to_sequences([new_sentence]) # 정수 인코딩
        pad_new = pad_sequences(encoded, maxlen = 100) # 패딩
        loaded_model = load_model("./app/static/crawling_best_model.h5")
        score = float(loaded_model.predict(pad_new)) # 예측
        return score
    
    def get_recommend_movie_list(title):
        data = MoiveService.get_movie()
        df = pd.DataFrame(data)
        # 영화 데이터 가공 및 유사도 행렬 생성
        count_vector = CountVectorizer(ngram_range=(1, 3))
        c_vector_genres = count_vector.fit_transform(df.genre)
        genre_c_sim = cosine_similarity(c_vector_genres, c_vector_genres).argsort()[:, ::-1]
        # 입력한 영화와 유사한 영화 목록을 반환하는 함수
        # 입력한 영화의 인덱스를 찾기
        target_movie_index = df[df['title'] == title].index.values[0]
        
        # 유사도 측정 결과를 리스트로 저장
        sim_scores = list(enumerate(genre_c_sim[target_movie_index]))
        
        # 유사도에 따라 정렬
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        
        # 자기 자신을 제외하고 top 개수만큼 선택
        sim_scores = sim_scores[1:6]
        
        # 선택한 영화의 인덱스를 리스트로 저장
        movie_indices = [i[0] for i in sim_scores]
        result = df.iloc[movie_indices].to_dict(orient='records')
        # 추천 영화를 반환
        return result