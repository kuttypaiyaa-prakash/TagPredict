# IMPORTING MODEL
import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import MultiLabelBinarizer
df = pd.read_csv("dataset/Tags.csv")
df1 = df.dropna()
import ast
df1['Tag'] = df1['Tag'].apply(lambda x: ast.literal_eval(x))

tagPredictorModel = joblib.load('tag_predictor.pkl')
tfidf = TfidfVectorizer (analyzer='word', max_features=10000, ngram_range=(1,3), stop_words='english')
X = tfidf.fit_transform(df1['Body'].values.astype(str))
multilabel = MultiLabelBinarizer()
y=df1['Tag'] 
y=multilabel.fit_transform(y)

def getTags(question):
    question = tfidf.transform(question)
    tags = multilabel.inverse_transform(tagPredictorModel.predict(question))
    print(tags)
    return tags