import re 
from tensorflow.keras.preprocessing.text import Tokenizer  # 텍스트 데이터를 토큰화하기 위한 모듈
from tensorflow.keras.preprocessing.sequence import pad_sequences  # 시퀀스 데이터 패딩을 위한 모듈
from tensorflow.keras.models import load_model  # 저장된 딥러닝 모델을 불러오기 위한 모듈
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from .movie_service import MoiveService
from kiwipiepy import Kiwi  # 형태소 분석을 위한 Kiwipie 패키지
import pickle



class AI_Service:
    kiwi = Kiwi()
    loaded_model = load_model('./app/static/best_model.h5')
    with open('./app/static/tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)
    def AI_predict(self, new_sentence):
        new_sentence = re.sub(r'[^ㄱ-ㅎㅏ-ㅣ가-힣 ]','', new_sentence)
        new_sentence = self.kiwi.tokenize(new_sentence)
        new_sentence = [x.form for x in new_sentence]
        encoded = self.tokenizer.texts_to_sequences([new_sentence]) # 정수 인코딩
        pad_new = pad_sequences(encoded, maxlen = 60) # 패딩
        score = float(self.loaded_model.predict(pad_new)) # 예측
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