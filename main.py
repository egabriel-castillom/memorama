from flask import Flask, render_template, request, session, flash
from dotenv import load_dotenv
import click
import os
import time

load_dotenv()
p=0
results=[2.1, 4.1, 6.1, 8.1, 10.1, 12.1]
def create_app(): #SE EJECUTA SIEMPRE QUE SE GENERE UNA INSTANCIA DE LA APLICACIÓN dentro del bash. 
    app = Flask(__name__) #Asigna modulo inicial para nuestra aplicación.
    app.config.from_mapping( #Configuración de nuestra app, obtiene las variables de entorno necesarias para ejecutar conexion con db.  
        SECRET_KEY=os.environ.get('SECRET_KEY'),        
    )
    @app.route('/',methods=('POST','GET'))
    def memo():
        if request.method == 'POST':                                                             
            if session.get('P'):
                id = session.get('id')
                iD = session.get('iD')
                if session.get('r2id'):
                    r2iD = request.form.get('id')
                    if r2iD == id:
                        message = 'Already selected ' + id
                        return render_template('main_memo.html',id=id,iD=iD,message=message)
                    elif r2iD == iD:
                        message = 'Already selected ' + iD
                        return render_template('main_memo.html',id=id,iD=iD,message=message)
                    else:
                        session['r2iD'] = r2iD
                        r2id = session.get('r2id')
                        message = r2iD + ' iD en sesión2'
                        P = session.get('P')
                        p = int(P)
                        a = float(r2id)
                        b = float(r2iD)
                        RF = a + b
                        rf = str(RF)
                        if RF in results:
                            rfo = 'CORRECTO ' + rf
                            P = str(p+1)
                            session['P'] = P
                            return render_template('main_memo.html',id=id,iD=iD,id1=r2id,iD1=r2iD,message=message, p=P, rf=rfo)
                        else:
                            rfo = 'INCORRECTO ' + rf + ' Vuelve a intentarlo.'
                            session['F'] = 1
                            F = session.get('F')
                            return render_template('main_memo.html',id=id1,iD=id2,rf=rfo,F = F)                  
                else:
                    r2id = request.form.get('id')
                    if r2id == id:
                        message = 'Already selected ' + id
                        return render_template('main_memo.html',id=id,iD=iD,message=message)
                    elif r2id == iD:
                        message = 'Already selected ' + iD
                        return render_template('main_memo.html',id=id,iD=iD,message=message)
                    else:
                        session['r2id'] = r2id
                        message = r2id + ' id en sesión2'
                        P = session.get('P')
                        return render_template('main_memo.html',id=id,iD=iD,id1=r2id,message=message, p=P)
            elif session.get('F'):
                session.pop('id')
                session.pop('iD')
                session.pop('F')
                return render_template('main_memo.html')
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
                        if RF in results:
                            rfo = 'CORRECTO ' + rf
                            P = str(p+1)
                            session['P'] = P
                            return render_template('main_memo.html',id=id1,iD=id2,message=message,rf=rfo, p=P)
                        else:
                            rfo = 'INCORRECTO ' + rf + ' Vuelve a intentarlo.'
                            session['F'] = 1
                            F = session.get('F')
                            return render_template('main_memo.html',id=id1,iD=id2,rf=rfo,F = F)                       		        	
                else:
                    id = str(request.form.get('id'))
                    session['id'] = id                                
                    message = id + ' id en sesion.'    
                    return render_template('main_memo.html',id=id,message=message)        
                    #session.clear()
                    #click.echo('SESION REINICIADA.')
        elif request.method == 'GET':
            session.clear()
        return render_template('main_memo.html')
    return app

app = create_app()
