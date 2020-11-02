from transformers import AutoModel, AutoTokenizer
import torch #torchはサイズでかいからherokuにuploadするときはcpu版をrequirementsで指定する
import numpy as np
#bert-base-japaneseはcl-tohokuを入れないとうまくいかない
#fugashiが無いとか言われたからインストール->ipadic dictionaryが無いと言われてる pip install ipadicで入れたらとりあえず動いた
tokenizer = AutoTokenizer.from_pretrained("cl-tohoku/bert-base-japanese-whole-word-masking")
model = AutoModel.from_pretrained("./DistilBERT-base-jp")

#文字列からベクトルを作る関数
def get_embedding(model, tokenizer, text):
  tokenized_text = tokenizer.tokenize(text)
  tokenized_text.insert(0, '[CLS]')
  tokenized_text.append('[SEP]')
  tokens = tokenizer.convert_tokens_to_ids(tokenized_text)
  tokens_tensor = torch.tensor([tokens])
  model.eval()
  with torch.no_grad():
      layers, _ = model(tokens_tensor)
  target_layer = -2
  embedding = layers[0][target_layer].numpy()
  return embedding

def getink(s:str):
    color_embedding_list=[]
    
    f=open("./colorlist.txt",encoding="utf8")
    sentens=f.readlines()
    f.close()

    #インクの名前に対応するベクトルリスト生成
    for char in sentens:
        mbedding = get_embedding(model, tokenizer, char.strip())
        color_embedding_list.append(mbedding)

    prod = []
    res=get_embedding(model,tokenizer,s.strip())
    #入力文字列のベクトルとインクの名前のベクトルを比較し最も近いやつをreturn
    for v in color_embedding_list:
        prod.append(np.linalg.norm(v-res, ord = 2))
    return sentens[np.array(prod).argmin()].strip()

print(getink('焼肉'))