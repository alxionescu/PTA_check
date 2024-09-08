from flask import Flask, request
import os

check_app = Flask(__name__)


@check_app.route('/status', methods=['GET'])
def status():
    return "OK"
@check_app.route('/sales', methods=['POST'])
def client():
        res=  request.form
        dct= res.to_dict(flat=True)
        print(dct)
        with open ("clients.csv", "a") as f:
            f.write ("\n" )
            for  key, val in dct.items():
                f.write (val + ";")
        f.close()
              
        #print (res)
        return res
@check_app.route('/read-clients/<passwd>', methods=['GET'])
def read_clients (passwd):
    if ( passwd in ['cineva', 'altcineva']):
        with open("clients.csv", "r") as f:
            content=f.read()
        f.close()
        return content
#check_app.run()



