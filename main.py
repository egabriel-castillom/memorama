from flask import Flask, render_template, request, session, flash
from dotenv import load_dotenv
import click
import os
import time

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
            if session.get('F'):
                if session.get('P'):
                    P = session.get('P')
                    message = 'La ronda 1 es correcta, vuelve a iniciar ronda 2'
                    session.pop('r2id')
                    session.pop('r2iD')
                    session.pop('F')
                    return render_template('main_memo.html',id=id1,iD=id2,message=message,rf=rfo, p=P)
                else:
                    session.clear()
                    return render_template('main_memo.html')
            elif session.get('P'):
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
                        r2a = float(r2id)
                        r2b = float(r2iD)
                        r2RF = r2a + r2b
                        r2rf = str(r2RF)
                        results=[2.1, 4.1, 6.1, 8.1, 10.1, 12.1]
                        if r2RF in results:
                            r2rfo = 'CORRECTO ' + r2rf
                            r2p = int(session.get('P'))
                            r2P = str(r2p+1)
                            session['P'] = r2P
                            return render_template('main_memo.html',id=id,iD=iD,id1=r2id,iD1=r2iD,message=message, p=r2P, rf = r2rfo)
                        else:
                            r2rfo = 'INCORRECTO ' + r2rf + ' Vuelve a intentarlo.'
                            session['F'] = 1
                            F = session.get('F')
                            return render_template('main_memo.html',id=id,iD=iD,rf=r2rfo,F=F)                       		        	                            
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
                            session['P'] = P
                            return render_template('main_memo.html',id=id1,iD=id2,message=message,rf=rfo, p=P)
                        else:
                            rfo = 'INCORRECTO ' + rf + ' Vuelve a intentarlo.'
                            session['F'] = 1
                            F = session.get('F')
                            return render_template('main_memo.html',id=id1,iD=id2,rf=rfo,F=F)                       		        	
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
