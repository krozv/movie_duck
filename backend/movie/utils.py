# 해당 폴더를 사용하려면 JAVA를 다운받아서 시스템 환경 변수 편집에서 환경 변수누르고 위쪽에서 새로만들기 누른 후 변수 : JAVA_HOME, 값: C:\Program Files\Java\jdk-22\bin\server 로 설정해야한다.
# 1줄 요약 : JAVA WINDOWS x64 MSI Installer 다운 -> 시스템 환경 변수 편집 -> 환경 변수 -> 새로 만들기 -> 변수 : JAVA_HOME, 값 : C:\Program Files\Java\jdk-22\bin\server
# movie/utils.py
import re
import pandas as pd
from konlpy.tag import Okt
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

okt = Okt()

def clean_text(text):
    p = re.compile('[가-힇ㄱ-ㅎㅏ-ㅣ]*')
    return ' '.join(p.findall(text)).strip()

def extract_keywords(text):
    noun, verb, adj = [], [], []
    for word, pos in okt.pos(text, stem=True):
        if pos == 'Noun':
            noun.append(word)
        elif pos == 'Verb':
            verb.append(word)
        elif pos == 'Adjective':
            adj.append(word)
    return noun, verb, adj

def process_movie_descriptions(descriptions):
    df = pd.DataFrame(descriptions, columns=['title', 'description'])
    
    # Clean descriptions
    df['description_clean'] = df['description'].apply(clean_text)
    
    # Extract keywords
    df[['noun', 'verb', 'adj', 'all']] = df['description_clean'].apply(
        lambda text: pd.Series([
            ' '.join(extract_keywords(text)[0]),
            ' '.join(extract_keywords(text)[1]),
            ' '.join(extract_keywords(text)[2]),
            ' '.join(extract_keywords(text)[0]) + ' ' + ' '.join(extract_keywords(text)[1]) + ' ' + ' '.join(extract_keywords(text)[2])
        ])
    )
    
    # Apply TF-IDF
    tfidf = TfidfVectorizer()
    res = tfidf.fit_transform(df['all']).toarray()
    
    # Extract top TF-IDF keywords
    n_top = 300
    importance = np.argsort(np.asarray(res.sum(axis=0)).ravel())[::-1]
    tfidf_feature_names = np.array(tfidf.get_feature_names_out())
    top_keywords = tfidf_feature_names[importance[:n_top]]
    
    # Extract top POS keywords
    top_noun, top_verb, top_adj = extract_keywords(' '.join(top_keywords))
    
    return {
        'tfidf_keywords': list(top_keywords),
        'top_noun': top_noun[:5],
        'top_verb': top_verb[:5],
        'top_adj': top_adj[:5]
    }