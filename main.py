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
                if session.get('P') == '1':
                    id = session.get('id')
                    iD = session.get('iD')
                    P = 'PUNTAJE ACTUAL: ' + session.get('P')
                    message = 'La ronda 1 es correcta, vuelve a iniciar ronda 2'
                    session.pop('r2id',None)
                    session.pop('r2iD',None)
                    session.pop('F',None)
                    return render_template('main_memo.html',id=id,iD=iD,message=message, p=P)
                elif session.get('P') == '2':
                    id = session.get('id')
                    iD = session.get('iD')
                    r2id = session.get('r2id')
                    r2iD = session.get('r2iD')
                    P = 'PUNTAJE ACTUAL: ' + session.get('P')
                    message = 'La ronda 2 es correcta, vuelve a iniciar ronda 3'
                    session.pop('r3id',None)
                    session.pop('r3iD',None)
                    session.pop('F',None)
                    return render_template('main_memo.html',id=id,iD=iD,message=message,id2=r2id,iD2=r2iD,p=P)
                else:
                    session.clear()
                    return render_template('main_memo.html')
            elif session.get('P') == '3':
                id = session.get('id')
                iD = session.get('iD')
                r2id = session.get('r2id')
                r2iD = session.get('r2iD')
                r3id = session.get('r3id')
                r3iD = session.get('r3iD')
                if session.get('r4id'):
                    r4id = session.get('r4id')
                    r4iD = request.method.get('id')
                    session['r4iD'] = r4iD
                    r4a = float(r4id)
                    r4b = float(r4iD)
                    r4RF = r4a + r4b
                    r4rf = str(r4RF)
                    results=[1.1, 2.2, 3.3, 4.4, 5.5, 6.6]
                    if r4RF in results:
                        message = 'Correcto'
                        return render_template('main_memo.html',message=message, id=id,iD=iD,id2=r2id,iD2=r2iD,id3=r3id,iD3=r3iD,id4=r4id,iD4=r4iD)
                    else:
                        message = 'Incorrecto'
                        return render_template('main_memo.html',message=message, id=id,iD=iD,id2=r2id,iD2=r2iD,id3=r3id,iD3=r3iD)
                else:
                    r4id = request.form.get('id')
                    session['r4id'] = r4id
                    return render_template('main_memo.html',message=message, id=id,iD=iD,id2=r2id,iD2=r2iD,id3=r3id,iD3=r3iD,id4=r4id)
            elif session.get('P') == '2':
                id = session.get('id')
                iD = session.get('iD')
                r2id = session.get('r2id')
                r2iD = session.get('r2iD')
                if session.get('r3id'):
                    r3id = session.get('r3id')
                    r3iD = request.form.get('id')
                    r3a = float(r3id)
                    r3b = float(r3iD)
                    r3RF = r3a + r3b
                    r3rf = str(r3RF)
                    results=[1.1, 2.2, 3.3, 4.4, 5.5, 6.6]
                    if r3iD == id:
                        message = 'Ya se ha seleccionado previamente el id (' + id + ') en la primer ronda'
                        return render_template('main_memo.html',message=message,id=id,iD=iD,id2=r2id,iD2=r2iD, id3=r3id)
                    elif r3iD == iD:
                        message = 'Ya se ha seleccionado previamente el iD (' + iD + ') en la primer ronda'    
                        return render_template('main_memo.html',message=message,id=id,iD=iD,id2=r2id,iD2=r2iD, id3=r3id)
                    elif r3iD == r2id:
                        message = 'Ya se ha seleccionado previamente el id (' + r2id + ') en la segunda ronda'
                        return render_template('main_memo.html',message=message,id=id,iD=iD,id2=r2id,iD2=r2iD, id3=r3id)
                    elif r3iD == r2iD:
                        message = 'Ya se ha seleccionado previamente el iD (' + iD + ') en la segunda ronda'    
                        return render_template('main_memo.html',message=message,id=id,iD=iD,id2=r2id,iD2=r2iD, id3=r3id)
                    elif r3iD == r3id:
                        session.pop('r3id')
                        r3PA = 'PUNTAJE ACTUAL ' + session.get('P')
                        message = 'Se ha quitado la seleccion'    
                        return render_template('main_memo.html',message=message,id=id,iD=iD,id2=r2id,iD2=r2iD,p=r3PA)
                    elif r3RF in results:
                        r3rfo = 'CORRECTO ' + r3rf
                        r3p = int(session.get('P'))
                        r3P = str(r3p+1)
                        session['r3iD'] = r3iD
                        session['P'] = r3P
                        r3PA = 'PUNTAJE ACTUAL: ' + r3P
                        return render_template('main_memo.html',id=id,iD=iD,id2=r2id,iD2=r2iD,id3=r3id,iD3=r3iD, p=r3PA, rf = r3rfo)
                    else:
                        r3rfo = 'NO SE ENCUENTRA EN RESULTADOS | id (' + r3id + ') + iD (' + r3iD + ') = (' + r3rf + ').'
                        session['F'] = 1
                        F = session.get('F')
                        return render_template('main_memo.html',id=id,iD=iD,id2=r2id,iD3=r2iD,rf=r3rfo,F=F)
                else:
                    r3id = request.form.get('id')
                    if r3id == id:
                        message = 'Ya se ha seleccionado previamente el id (' + id + ') en la primer ronda'
                        return render_template('main_memo.html',message=message,id=id,iD=iD,id2=r2id,iD2=r2iD)
                    elif r3id == iD:
                        message = 'Ya se ha seleccionado previamente el iD (' + iD + ') en la primer ronda'    
                        return render_template('main_memo.html',message=message,id=id,iD=iD,id2=r2id,iD2=r2iD)
                    elif r3id == r2id:
                        message = 'Ya se ha seleccionado previamente el id (' + r2id + ') en la segunda ronda'
                        return render_template('main_memo.html',message=message,id=id,iD=iD,id2=r2id,iD2=r2iD)
                    elif r3id == r2iD:
                        message = 'Ya se ha seleccionado previamente el iD (' + iD + ') en la segunda ronda'    
                        return render_template('main_memo.html',message=message,id=id,iD=iD,id2=r2id,iD2=r2iD)
                    else:
                        session['r3id'] = r3id                                
                        message = '(' + r3id + ') id en sesión3.'            
                        return render_template('main_memo.html',message=message, id=id,iD=iD,id2=r2id,iD2=r2iD,id3=r3id)
            elif session.get('P'):
                id = session.get('id')
                iD = session.get('iD')
                if session.get('r2id'):
                    r2id = session.get('r2id')
                    r2iD = request.form.get('id')
                    if r2iD == id:
                        message = 'Ya se ha seleccionado previamente el id (' + id + ') en la primer ronda'
                        return render_template('main_memo.html',id=id,iD=iD,message=message,id2=r2id)
                    elif r2iD == iD:
                        message = 'Ya se ha seleccionado previamente el iD (' + iD + ') en la primer ronda'
                        return render_template('main_memo.html',id=id,iD=iD,message=message,id2=r2id)
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
                        results=[1.1, 2.2, 3.3, 4.4, 5.5, 6.6]
                    if r2RF in results:
                        r2rfo = 'CORRECTO ' + r2rf
                        r2p = int(session.get('P'))
                        r2P = str(r2p+1)
                        session['P'] = r2P
                        r2PA = 'PUNTAJE ACTUAL: ' + r2P
                        return render_template('main_memo.html',id=id,iD=iD,id2=r2id,iD2=r2iD,message=message, p=r2PA, rf = r2rfo)
                    else:
                        r2rfo = 'NO SE ENCUENTRA EN RESULTADOS | id (' + r2id + ') + iD (' + r2iD + ') = (' + r2rf + ').'
                        session['F'] = 1
                        F = session.get('F')
                        return render_template('main_memo.html',id=id,iD=iD,rf=r2rfo,F=F)                       		        	                            
                else:
                    r2id = request.form.get('id')
                    if r2id == id:
                        message = 'Ya se ha seleccionado previamente el id (' + id + ') en la primer ronda'
                        return render_template('main_memo.html',id=id,iD=iD,message=message)
                    elif r2id == iD:
                        message = 'Ya se ha seleccionado previamente el iD (' + iD + ') en la primer ronda'
                        return render_template('main_memo.html',id=id,iD=iD,message=message)
                    else:
                        session['r2id'] = r2id
                        message = '(' + r2id + ') id en sesión2'
                        P = 'PUNTAJE ACTUAL: ' + session.get('P')
                        return render_template('main_memo.html',id=id,iD=iD,id2=r2id,message=message, p=P)
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
                        results=[1.1, 2.2, 3.3, 4.4, 5.5, 6.6]
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
                    id = request.form.get('id')
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
