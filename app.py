from flask import Flask, request


app = Flask(__name__)


@app.route('/status', methods=['GET'])
def status():
    return "OK"
@app.route('/sales', methods=['POST'])
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
@app.route('/read-clients', methods=['GET'])
def read_clients ():
    with open("clients.csv", "r") as f:
        content=f.read()
    f.close()
    return content


if __name__ == "__main__":
    app.run()



