from flask import Flask, request, jsonify


check_app = Flask(__name__)


@check_app.route('/status', methods=['GET'])
def status():
    return jsonify({"OK": "yes"})
@check_app.route('/sales', methods=['POST'])
def client():
        res=  request.form
        dct= res.to_dict(flat=True)
        print(dct)
        with open ("clients.csv", "a") as f:
            for  key, val in dct.items():
                f.write (key + ";" + val)
        f.close()
              
        #print (res)
        return res

check_app.run(debug=1)



