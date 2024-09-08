from flask import Flask, request
import os


check_app = Flask(__name__)

passwd_g = os.environ.get('passwd')
with open('/etc/secrets/status', 'r')as fs:
    status = fs.read()
    fs.close()


@check_app.route('/status', methods=['GET', 'POST'])
def status(): 
    passwd = request.args.get('passwd')
    status=request.args.get('status')
    if (passwd and status and passwd == passwd_g ):
        with open('/etc/secrets/status', 'w') as f:            
            f.write(status)
        f.close()

    else:
        with open('/etc/secrets/status', 'r') as f:            
            status = f.read()
        f.close()       
    return status

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
    if ( passwd == passwd_g):
        with open("clients.csv", "r") as f:            
            content = f.readlines()
        f.close()
        return content
        
    else:
         return 'Wrong passwd'
@check_app.route('/delete')
def delete_csv ():
    passwd = request.args.get('passwd')
    if ( passwd == passwd_g):
        open("clients.csv", 'w').close()        
    else:
        return 'Wrong passwd'

#check_app.run()



