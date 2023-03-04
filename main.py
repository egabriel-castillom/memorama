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
                    id1 = session.get('id')
                    id2 = session.get('iD')
                    P = 'PUNTAJE ACTUAL: ' + session.get('P')
                    message = 'La ronda 1 es correcta, vuelve a iniciar ronda 2'
                    session.pop('r2id',None)
                    session.pop('r2iD',None)
                    session.pop('F',None)
                    return render_template('main_memo.html',id=id1,iD=id2,message=message, p=P)
                else:
                    session.clear()
                    return render_template('main_memo.html')
            elif session.get('P'):
                id = session.get('id')
                iD = session.get('iD')
                if session.get('r2id'):
                    r2id = session.get('r2id')
                    r2iD = request.form.get('id')
                    if r2iD == id:
                        message = 'Ya se ha seleccionado previamente el id (' + id + ')'
                        return render_template('main_memo.html',id=id,iD=iD,message=message)
                    elif r2iD == iD:
                        message = 'Ya se ha seleccionado previamente el iD (' + iD + ')'
                        return render_template('main_memo.html',id=id,iD=iD,message=message)
                    elif r2iD == r2id:
                        session.pop('r2id')
                        PA = 'PUNTAJE ACTUAL ' + session.get('P')
                        message = 'Se ha quitado la seleccion'
                        return render_template('main_memo.html',id=id,iD=iD,message=message, p=PA)
                    else:
                        session['r2iD'] = r2iD
                        r2id = session.get('r2id')
                        message = '(' + r2iD + ') iD en sesión2'
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
                            r2PA = 'PUNTAJE ACTUAL: ' + r2P
                            return render_template('main_memo.html',id=id,iD=iD,id1=r2id,iD1=r2iD,message=message, p=r2PA, rf = r2rfo)
                        else:
                            r2rfo = 'NO SE ENCUENTRA EN RESULTADOS | id (' + r2id + ') + iD (' + r2iD + ') = (' + r2rf + ').'
                            session['F'] = 1
                            F = session.get('F')
                            return render_template('main_memo.html',id=id,iD=iD,rf=r2rfo,F=F)                       		        	                            
                else:
                    r2id = request.form.get('id')
                    if r2id == id:
                        message = 'Ya se ha seleccionado previamente el id (' + id + ')'
                        return render_template('main_memo.html',id=id,iD=iD,message=message)
                    elif r2id == iD:
                        message = 'Ya se ha seleccionado previamente el iD (' + iD + ')'
                        return render_template('main_memo.html',id=id,iD=iD,message=message)
                    else:
                        session['r2id'] = r2id
                        message = '(' + r2id + ') id en sesión2'
                        P = 'PUNTAJE ACTUAL: ' + session.get('P')
                        return render_template('main_memo.html',id=id,iD=iD,id1=r2id,message=message, p=P)
            else:    
                if session.get('id'):
                    id = session.get('id')
                    iD = request.form.get('id')
                    if id == iD:
                        session.clear()
                        message = ' Se ha quitado la selección'
                        return render_template('main_memo.html',message=message)                                     
                    else:
                        session['iD'] = iD                    
                        message = '(' + id + ') , (' + iD + ') ids en sesion.'             
                        a = float(id)
                        b = float(iD)
                        RF = a + b
                        rf = str(RF)
                        results=[2.1, 4.1, 6.1, 8.1, 10.1, 12.1]
                        if RF in results:
                            rfo = 'CORRECTO ' + rf
                            P = str(p+1)
                            session['P'] = P
                            PA = 'PUNTAJE ACTUAL: ' + P
                            return render_template('main_memo.html',id=id,iD=iD,message=message,rf=rfo, p=PA)
                        else:
                            rfo = 'NO SE ENCUENTRA EN RESULTADOS | id (' + id + ') + iD (' + iD + ') = ' + rf
                            session['F'] = 1
                            F = session.get('F')
                            return render_template('main_memo.html',id=id,iD=iD,rf=rfo,F=F)                       		        	
                else:
                    id = str(request.form.get('id'))
                    session['id'] = id                                
                    message = '(' + id + ') id en sesion.'    
                    return render_template('main_memo.html',id=id,message=message)        
                    #session.clear()
                    #click.echo('SESION REINICIADA.')
        elif request.method == 'GET':
            session.clear()
        return render_template('main_memo.html')
    return app

app = create_app()