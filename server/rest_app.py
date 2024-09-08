from flask import Flask, request

check_app = Flask(__name__)


@check_app.route('/status', methods=['GET'])
def status():
    return "100"
@check_app.route('/sales', methods=['POST'])
def client():
        res=  request.form
        dct= res.to_dict(flat=True)
        with open ("clients.csv", "a") as f:            
            for  key, val in dct.items():
                f.write (val + ";")
            f.write ("\n")
        f.close()
              
        #print (res)
        return res
@check_app.route('/read-clients', methods=['GET'])
def read_clients ():    
    passwd = request.args.get('passwd')
    if ( passwd == 'cineva'):
        with open("clients.csv", "r") as f:            
            content = f.readlines()
        f.close()
        return content
        
    else:
         return 'Wrong passwd'
@check_app.route('/delete')
def delete_csv ():
    passwd = request.args.get('passwd')
    if ( passwd == 'cineva'):
        open("clients.csv", 'w').close()        
    else:
        return 'Wrong passwd'

#check_app.run()



