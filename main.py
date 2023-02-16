from flask import Flask, render_template, request, session, flash
from dotenv import load_dotenv
import click
import os

load_dotenv()
p=0
def create_app(): #SE EJECUTA SIEMPRE QUE SE GENERE UNA INSTANCIA DE LA APLICACIÓN dentro del bash. 
    app = Flask(__name__) #Asigna modulo inicial para nuestra aplicación.
    app.config.from_mapping( #Configuración de nuestra app, obtiene las variables de entorno necesarias para ejecutar conexion con db.  
        SECRET_KEY=os.environ.get('SECRET_KEY'),        
    )
    @app.route('/',methods=('POST','GET'))
    def memo():
        if request.method == 'POST':                                                             
            results=[2.1, 4.1, 6.1, 8.1, 10.1, 12.1]
            try:
                ad = float(session.get('id')) 
                aD = float(session.get('iD')) 
                message = 'Si jala'
                return render_template('main_memo.html',id=id1,iD=id2,message=message)
            except:    
                if session.get('id'):
                    id1 = session.get('id')
                    id2 = request.form.get('id')
                    if id1 == id2:
                        session.clear()
                        message = ' Se ha quitado la selección'
                        return render_template('main_memo.html',message=message)                                     
                    else:
                        session['iD'] = id2                    
                        message = id1 + ' , ' + id2 + ' ids en sesion.'             
                        a = float(id1)
                        b = float(id2)
                        RF = a + b
                        rf = str(RF)
                        
                        if RF in results:
                            rfo = 'CORRECTO ' + rf
                            P = str(p+1)
                            return render_template('main_memo.html',id=id1,iD=id2,message=message,rf=rfo, p=P)
                        else:
                            rfo = 'INCORRECTO ' + rf
                            return render_template('main_memo.html',id=id1,iD=id2,message=message,rf=rfo)                       		        	
                else:
                    id = str(request.form.get('id'))
                    session['id'] = id                                
                    message = id + ' id en sesion.'    
                    return render_template('main_memo.html',id=id,message=message)        
                    #session.clear()
                    #click.echo('SESION REINICIADA.')
        return render_template('main_memo.html')
    return app

app = create_app()
