from flask import jsonify,request,Flask
import os
from getink import getink

app = Flask(__name__)

#環境変数取得
# YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
# YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]

@app.route("/",methods=["GET"])
def root():
    sentense=request.args.get("sentense",type=str)
    ink = getink(sentense)
    res = {"ink":ink}
    return jsonify(res)

if __name__ == "__main__":
    #port = int(os.getenv("PORT"))
    app.run(host=os.getenv('APP_ADDRESS', 'localhost'), port=8000)

