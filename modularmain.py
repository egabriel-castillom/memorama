from flask import Flask, render_template, request, session, flash
from dotenv import load_dotenv
import click
import os

load_dotenv()
p=0
def assignid():
    if session.get('id'):
                id1 = session.get('id')
                id2 = request.form.get('id')
                if id1 == id2:
                    session.clear()
                    message = ' Se ha quitado la selección'
                    return render_template('main_memo.html',message=message)
    else:
            id = str(request.form.get('id'))
            session['id'] = id                                
            message = id + ' id en sesion.'    
            return render_template('main_memo.html',id=id,message=message)      

def assigniD():
    if session.get('iD'):
                iD1 = session.get('iD')
                iD2 = session.get('id')
                if iD1 == iD2:
                    session.clear()
                    message = ' Se ha quitado la selección'
                    return render_template('main_memo.html',message=message)
                else:
                    session['iD'] = request.form.get('id')                   
                    message = iD1 + ' , ' + iD2 + ' ids en sesion.'
                    return render_template('main_memo.html',message=message)

def evaluate():
    a = float(id1)
    b = float(iD)
    RF = a + b
    rf = str(RF)
    results=[2.1, 4.1, 6.1, 8.1, 10.1, 12.1]
    if RF in results:
        rfo = 'CORRECTO ' + rf
        P = 'perr' + str(p)
        return render_template('main_memo.html',id=id1,iD=iD,message=message,rf=rfo, p=P)
    else:
        rfo = 'INCORRECTO ' + rf
        return render_template('main_memo.html',id=id1,iD=iD,message=message,rf=rfo)

def create_app(): #SE EJECUTA SIEMPRE QUE SE GENERE UNA INSTANCIA DE LA APLICACIÓN dentro del bash. 
    app = Flask(__name__) #Asigna modulo inicial para nuestra aplicación.
   
    app.config.from_mapping( #Configuración de nuestra app, obtiene las variables de entorno necesarias para ejecutar conexion con db.  
        SECRET_KEY=os.environ.get('SECRET_KEY'),        
    )
    @app.route('/',methods=('POST','GET'))
    def memo():
        if request.method == 'POST':                                                             
            if session.get('id'):
                assigniD()
            else:
                assignid()
        return render_template('main_memo.html')
    return app

app = create_app()
