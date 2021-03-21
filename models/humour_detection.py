from .word_preprocess import clean_tweet
from .word_abbreviations import get_abbr
from sentence_transformers import SentenceTransformer, models
from torch import nn
import joblib

abbreviations = get_abbr()

def define_bert_encoder():
    word_embedding_model = models.Transformer('bert-base-uncased', max_seq_length=200)
    pooling_model = models.Pooling(word_embedding_model.get_word_embedding_dimension())
    dense_model = models.Dense(ni_features=pooling_model.get_sentence_embedding_dimension(), out_features=200,
                               activation_function=nn.Tanh())

    bert_model = SentenceTransformer(modules=[word_embedding_model, pooling_model, dense_model])
    return bert_model


def define_svc():
    svc = joblib.load(r"C:\Users\Thejin\Desktop\Deep Learning\rexcoe\models\svc_humour.joblib")
    return svc

svc = define_svc()

def predict_humour(data):
    bert_model = define_bert_encoder()
    text = clean_tweet(data, abbreviations)
    text = bert_model.encode([text])
    res = svc.predict(text)
    return res
