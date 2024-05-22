# import pickle
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import re
# import urllib.request
# from konlpy.tag import Okt
# from tqdm import tqdm
# from tensorflow.keras.preprocessing.text import Tokenizer
# from tensorflow.keras.preprocessing.sequence import pad_sequences
# from sklearn.model_selection import train_test_split
# 참고 사이트 : https://wikidocs.net/44249

# 1. 데이터 로드. 
# urllib.request.urlretrieve("https://raw.githubusercontent.com/e9t/nsmc/master/ratings_train.txt", filename="ratings_train.txt")
# urllib.request.urlretrieve("https://raw.githubusercontent.com/e9t/nsmc/master/ratings_test.txt", filename="ratings_test.txt")

# pandas를 이용하여 훈련 데이터는 train_data에 테스트 데이터는 test_data에 저장
# train_data = pd.read_table('ratings_train.txt')
# test_data = pd.read_table('ratings_test.txt')

# # print('훈련용 리뷰 개수 :',len(train_data)) # 훈련용 리뷰 개수 출력
# # print(train_data[:5])

# # 2. 데이터 정제
# # document 열과 label 열의 중복을 제외한 값의 개수
# # print(train_data['document'].nunique(), train_data['label'].nunique())

# # document 열의 중복 제거
# train_data.drop_duplicates(subset=['document'], inplace=True)
# # print('총 샘플의 수 :',len(train_data))

# # 긍정, 부정 샘플의 개수
# # print(train_data.groupby('label').size().reset_index(name = 'count'))

# # 리뷰 중에 Null 값을 가진 샘플이 있는지 확인
# # print(train_data.isnull().values.any())

# train_data = train_data.dropna(how = 'any') # Null 값이 존재하는 행 제거
# # print(train_data.isnull().values.any()) # Null 값이 존재하는지 확인

# # print(len(train_data))

# # 3. 데이터 전처리

# # 한글과 공백을 제외하고 모두 제거하는 정규 표현식을 수행
# train_data['document'] = train_data['document'].str.replace("[^ㄱ-ㅎㅏ-ㅣ가-힣 ]", "", regex=True)
# # print(train_data[:5])

# train_data['document'] = train_data['document'].str.replace('^ +', "") # white space 데이터를 empty value로 변경
# train_data.replace({'document': {'' : np.nan}}, inplace=True)
# # print(train_data.isnull().sum())

# train_data = train_data.dropna(how = 'any')
# # print(len(train_data))

# # 테스트 데이터 전처리
# test_data.drop_duplicates(subset = ['document'], inplace=True) # document 열에서 중복인 내용이 있다면 중복 제거
# test_data['document'] = test_data['document'].str.replace("[^ㄱ-ㅎㅏ-ㅣ가-힣 ]","") # 정규 표현식 수행
# test_data['document'] = test_data['document'].str.replace('^ +', "") # 공백은 empty 값으로 변경
# test_data.replace({'document': {'' : np.nan}}, inplace=True) # 공백은 Null 값으로 변경
# test_data = test_data.dropna(how='any') # Null 값 제거
# # print('전처리 후 테스트용 샘플의 개수 :',len(test_data))

# # 토큰화
# stopwords = ['의','가','이','은','들','는','좀','잘','걍','과','도','를','으로','자','에','와','한','하다']

# okt = Okt()
# okt.morphs('와 이런 것도 영화라고 차라리 뮤직비디오를 만드는 게 나을 뻔', stem = True)
# ['오다', '이렇다', '것', '도', '영화', '라고', '차라리', '뮤직비디오', '를', '만들다', '게', '나다', '뻔']

# 토큰화 진행
# X_train = []
# for sentence in tqdm(train_data['document']):
#     tokenized_sentence = okt.morphs(sentence, stem=True) # 토큰화
#     stopwords_removed_sentence = [word for word in tokenized_sentence if not word in stopwords] # 불용어 제거
#     X_train.append(stopwords_removed_sentence)

# # print(X_train[:3])
# X_test = []
# for sentence in tqdm(test_data['document']):
#     tokenized_sentence = okt.morphs(sentence, stem=True) # 토큰화
#     stopwords_removed_sentence = [word for word in tokenized_sentence if not word in stopwords] # 불용어 제거
#     X_test.append(stopwords_removed_sentence)

# tokenizer = Tokenizer()
# tokenizer.fit_on_texts(X_train)
# print(tokenizer.word_index)

# threshold = 3
# total_cnt = len(tokenizer.word_index) # 단어의 수
# rare_cnt = 0 # 등장 빈도수가 threshold보다 작은 단어의 개수를 카운트
# total_freq = 0 # 훈련 데이터의 전체 단어 빈도수 총 합
# rare_freq = 0 # 등장 빈도수가 threshold보다 작은 단어의 등장 빈도수의 총 합

# # 단어와 빈도수의 쌍(pair)을 key와 value로 받는다.
# for key, value in tokenizer.word_counts.items():
#     total_freq = total_freq + value

#     # 단어의 등장 빈도수가 threshold보다 작으면
#     if(value < threshold):
#         rare_cnt = rare_cnt + 1
#         rare_freq = rare_freq + value

# vocab_size = total_cnt - rare_cnt + 1
# # print('단어 집합의 크기 :',vocab_size)

# tokenizer = Tokenizer(vocab_size) 
# tokenizer.fit_on_texts(X_train)
# X_train = tokenizer.texts_to_sequences(X_train)
# X_test = tokenizer.texts_to_sequences(X_test)
# print(X_train[:3])

# y_train = np.array(train_data['label'])
# y_test = np.array(test_data['label'])

# drop_train = [index for index, sentence in enumerate(X_train) if len(sentence) < 1]

# max_len = 30
# X_train = np.delete(X_train, drop_train, axis=0)
# y_train = np.delete(y_train, drop_train, axis=0)

# print(len(X_train))
# print(len(y_train))

# from tensorflow.keras.layers import Embedding, Dense, LSTM
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.models import load_model
# from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
# 모델 학습하는 구간
# embedding_dim = 100
# hidden_units = 128

# model = Sequential()
# model.add(Embedding(vocab_size, embedding_dim))
# model.add(LSTM(hidden_units))
# model.add(Dense(1, activation='sigmoid'))

# es = EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience=4)
# mc = ModelCheckpoint('review_model.keras', monitor='val_acc', mode='max', verbose=1, save_best_only=True)

# model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['acc'])
# # 데이터 분할
# X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.2, random_state=42)

# # 입력 데이터를 패딩된 시퀀스로 변환

# X_train = pad_sequences(X_train, maxlen=max_len)
# X_val = pad_sequences(X_val, maxlen=max_len)

# # 모델 훈련
# history = model.fit(X_train, y_train, epochs=15, callbacks=[es, mc], batch_size=64, validation_data=(X_val, y_val))
# model.save('review_model.keras')


# loaded_model = load_model('review_model.keras')
# X_test = pad_sequences(X_test, maxlen=max_len)

# with open('tokenizer.pickle', 'rb') as handle:
#     tokenizer = pickle.load(handle)

# print("\n 테스트 정확도: %.4f" % (loaded_model.evaluate(X_test, y_test)[1]))

# with open('tokenizer.pickle', 'wb') as handle:
#      pickle.dump(tokenizer, handle)

import re
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from konlpy.tag import Okt
import pickle

# 학습시킨 딥러닝 모델 load
loaded_model = load_model('review_model.keras')
# 토크나이저한 값 load
with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

max_len = 30
stopwords = ['의','가','이','은','들','는','좀','잘','걍','과','도','를','으로','자','에','와','한','하다']
okt = Okt()


def sentiment_predict(new_sentence):
  new_sentence = re.sub(r'[^ㄱ-ㅎㅏ-ㅣ가-힣 ]','', new_sentence)
  new_sentence = okt.morphs(new_sentence, stem=True) # 토큰화
  new_sentence = [word for word in new_sentence if not word in stopwords] # 불용어 제거
  encoded = tokenizer.texts_to_sequences([new_sentence]) # 정수 인코딩
  pad_new = pad_sequences(encoded, maxlen = max_len) # 패딩
  score = loaded_model.predict(pad_new)[0] # 배열에서 하나의 값만 추출하여 할당
  score = float(score) # 추출한 값을 스칼라로 변환
  if(score > 0.5):
    print("{:.2f}% 확률로 긍정 리뷰입니다.\n".format(score * 100))
  else:
    print("{:.2f}% 확률로 부정 리뷰입니다.\n".format((1 - score) * 100))
  return {'score': score}
