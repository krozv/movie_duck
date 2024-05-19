import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense

# 간단한 훈련 데이터: 영화 제목
movie_titles = [
    "The Shawshank Redemption",
    "The Godfather",
    "The Dark Knight",
    # 추가적인 영화들...
]

# 입력 데이터: 장르와 배우를 조합한 문자열
X_train = [
    "Action, Tom Cruise",
    "Crime, Marlon Brando",
    "Thriller, Christian Bale",
    # 추가적인 입력 데이터...
]

# 출력 데이터: 영화 제목
y_train = movie_titles

# 각 문자를 ASCII 코드로 변환하여 벡터화하는 함수
def text_to_vector(text):
    return [ord(char) for char in text]

# 입력 데이터를 벡터화
X_train_vectorized = [text_to_vector(text) for text in X_train]

# 배열로 변환
X_train_vectorized = np.array(X_train_vectorized)
y_train = np.array(y_train)

# 신경망 모델 정의
model = Sequential([
    Embedding(input_dim=128, output_dim=64, input_length=X_train_vectorized.shape[1]),
    LSTM(128),
    Dense(len(movie_titles), activation='softmax')
])

# 모델 컴파일
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# 모델 학습
model.fit(X_train_vectorized, y_train, epochs=10, batch_size=1)

# 학습된 모델을 사용하여 특정 장르와 배우에 대한 영화 제목 예측
input_genre_actor = "Action, Tom Cruise"  # 예측할 장르와 배우
input_vector = np.array([text_to_vector(input_genre_actor)])  # 입력 데이터 벡터화
predicted_index = model.predict_classes(input_vector)
predicted_title = movie_titles[predicted_index[0]]
print("예측된 영화 제목:", predicted_title)
