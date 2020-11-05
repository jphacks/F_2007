from transformers import AutoModel, AutoTokenizer
import torch 
#torchはサイズでかいからherokuにuploadするときはcpu版をrequirementsで指定する
#bert-base-japaneseはcl-tohokuを入れないとうまくいかない
#fugashiが無いとか言われたからインストール->ipadic dictionaryが無いと言われてる pip install ipadicで入れたらとりあえず動いた
#numpyは重くてherokuの500MB制限に引っかかるからtorchのtensor形式で計算
#colorlistはheroku側で消されるぽいからリストで読み込ませる

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
  embedding = layers[0][target_layer]
  return embedding

def getink(s:str):
    color_embedding_list=[]
    
    sentens = ["朝顔","紫陽花","露草","紺碧","天色","月夜","孔雀","深海","松露","深緑","竹林","冬将軍","霧雨","竹炭","躑躅","秋桜","紅葉","紫式部","山葡萄","夕焼け","冬柿","稲穂","土筆","山栗"]

    #インクの名前に対応するベクトルリスト生成
    for char in sentens:
        mbedding = get_embedding(model, tokenizer, char.strip())
        color_embedding_list.append(mbedding)

    prod = []
    res=get_embedding(model,tokenizer,s.strip())
    #入力文字列のベクトルとインクの名前のベクトルを比較し最も近いやつをreturn
    for v in color_embedding_list:
        prod.append(torch.norm(v-res))
    return sentens[int(torch.argmin(torch.tensor(prod)))]

print(getink("カツオ"))