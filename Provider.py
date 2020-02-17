import mysql.connector

mydb = mysql.connector.connect(host = 'localhost', username = 'root', passwd = '6800$h@#D7471', database ='login_data_base')

def register():
    user = input('Enter Your Name: ')
    email_id = input('Enter Your Email ID: ')
    passwd = input('Enter Your Password: ')
    cnfpd = input('Confirm Your Password: ')
    if passwd == cnfpd:
        mycursor = mydb.cursor()
        sql = 'insert into user_tabel (user_name, Email_Id, pass_word) values (%s,%s,%s)'
        val =  ('{}','{}','{}').format(user,email_id,passwd)
        mycursor.execute(sql , val)
        mydb.commit()
        print('Register Successfully ')

    else:
        print('Incorrect User Name Or Password')
register()



def login():

    userl = input('USER NAME: ')
    paswdl = (input('PASSWORD: '))
    cnfpasl = (input('CONFIRM PASSWORD: '))
    if paswdl == cnfpasl:
        print('LOGIN SUCCESSFULLY')
    else:
        print('WRONG PASSWORD')
# login()



















