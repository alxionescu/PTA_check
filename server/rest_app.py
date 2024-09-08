from flask import Flask, request
import os


check_app = Flask(__name__)

passwd_g = os.environ.get('passwd')



@check_app.route('/status', methods=['GET', 'POST'])
def status():
    passwd = request.args.get('passwd')
    stat_in=request.args.get('status') 
    with open('/etc/secrets/status', 'r')as fs:
        status = fs.read()
        fs.close()
    if (request.method=='GET'):
        return status
    elif (passwd and stat_in and passwd == passwd_g ):
        with open('/etc/secrets/status', 'w') as f:            
            f.write(stat_in)
            f.close()
        return stat_in
    else:
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
@check_app.route('/delete', methods=['POST'])
def delete_csv ():
    passwd = request.args.get('passwd')
    if ( passwd == passwd_g):
        open("clients.csv", 'w').close()
        return       
    else:
        return 'Wrong passwd'

#check_app.run()



