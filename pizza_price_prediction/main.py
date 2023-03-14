from flask import Flask , render_template, request
import numpy as np
import pickle
import CONFIG


app = Flask(__name__)



@app.route("/",methods = ["GET" , "POST"])
def price():
    prediction = 0
    if request.method == "POST":
        Extra_cheese = int(request.form.get("Extra_cheese"))
        Extra_mushroom = int(request.form.get("Extra_mushroom"))
        Size_by_Inch = int(request.form.get("Size_by_Inch"))
        Extra_spicy = int(request.form.get("Extra_spicy"))
        print(Extra_cheese , Extra_mushroom , Size_by_Inch , Extra_spicy  )
        print(type(Size_by_Inch))
        model = pickle.load(open(CONFIG.MODEL_PATH,"rb"))
        prediction = round(model.predict([[Extra_cheese , Extra_mushroom , Size_by_Inch , Extra_spicy  ]])[0],2)
        print(prediction)
    return render_template("index.html" , Predict = prediction)


if __name__ == "__main__":
    app.run(host=CONFIG.HOST_NUMBER,port=CONFIG.PORT_NUMBER,debug=True)

