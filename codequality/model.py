from transformers import BertModel, GPT2Model


class BaseModel:
    transformer_model = None

    def __init__(self, learning_rate, epochs):
        self.learning_rate = learning_rate
        self.epochs = epochs


class Bert(BaseModel):
    transformer_model = BertModel


class GPT2(BaseModel):
    transformer_model = GPT2Model
