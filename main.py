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
            if session.get('id') and session.get('iD'):
#                if session.get('id1'):
#                    id1 = session.get('id1')
#                    id2 = request.form.get('id')
#                    if id1 == id2:
#                        session.clear()
#                        message = ' Se ha quitado la selección'
#                        return render_template('main_memo.html',message=message)                                     
#                    else:
#                        if session.get('iD1'):
#                            iD1 = session.get('iD1')
#                            iD2 = id2
#                            if iD1 == iD2:
#                                session.clear()
#                                message = ' Se ha quitado la selección'
#                                return render_template('main_memo.html',message=message)
#                        else:
#                            session['iD1'] = id2                    
#                            message = id1 + ' , ' + id2 + ' ids en sesion.'             
#                            a = float(id1)
#                            b = float(id2)
#                            RF = a + b
#                            rf = str(RF)
#                            results=[2.1, 4.1, 6.1, 8.1, 10.1, 12.1]
#                            if RF in results:
#                                rfo = 'CORRECTO ' + rf
#                                P1 = str(P+1)
#                                return render_template('main_memo.html',id=id1,iD=id2,message=message,rf=rfo, p=P)
#                            else:
#                                rfo = 'INCORRECTO ' + rf
#                                return render_template('main_memo.html',id=id1,iD=id2,message=message,rf=rfo)                       		       
                    message = 'Si jala'
                    return render_template('main_memo.html',id=id1,iD=id2,message=message)
                else:
                    id1 = request.form.get('id')
                    id = session.get('id')
                    iD = session.get('iD')
                    if id1 == id:
                        message = 'ID ' + id1 + ' actualmente en sesion.'
                        return render_template('main_memo.html',id=id1,iD=iD,p=P, message=message)
                    elif id1 == iD:
                        message = 'ID ' + id1 + ' actualmente en sesion.'
                        return render_template('main_memo.html',id=id,iD=id1,p=P, message=message)
                    else:
                        session['id1'] = id1                                
                        message = id1 + ' id en sesion.'
                        return render_template('main_memo.html', id=id1,iD=iD,id1=id1,message=message, p=P)        
                        #session.clear()
                        #click.echo('SESION REINICIADA.')
            else:    
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
                        results=[2.1, 4.1, 6.1, 8.1, 10.1, 12.1]
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
