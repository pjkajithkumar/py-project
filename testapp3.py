from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('intro.html')


@app.route('/ebcalc',methods = ['POST', 'GET'])
def ebcalc():
   if request.method == 'POST':
      units = int(request.form['units'])
      ebtype = request.form['ebtype']
      if ebtype=="domestic":
          amount=int(units*2)
          if units<=100:
            return "For your domestic EB type, Your amount is: "+str (amount)+". Less than 100 units and no need to pay. Thank you!"
          else:
              return "For your domestic EB type, Your amount is: "+str (amount)+". Kindly pay the amount for your "+str(units)+" units. Thank you!"
      else:
          amount=units*4
          return "For your commercial EB type, Your amount is: "+str (amount)+". Kindly pay the amount for your "+str(units)+" units. Thank you!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
