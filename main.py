from flask import Flask, render_template, request, session, flash, g
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
            if session.get('start'):
                g.startCounter = True
                session.pop('start',None)
                return render_template('main_memo.html')
            elif session.get('F'):
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
                elif session.get('P') == '3':
                    id = session.get('id')
                    iD = session.get('iD')
                    r2id = session.get('r2id')
                    r2iD = session.get('r2iD')
                    r3id = session.get('r3id')
                    r3iD = session.get('r3iD')
                    P = 'PUNTAJE ACTUAL: ' + session.get('P')
                    message = 'La ronda 3 es correcta, vuelve a iniciar ronda 4'
                    session.pop('r4id',None)
                    session.pop('r4iD',None)
                    session.pop('F',None)
                    return render_template('main_memo.html',id=id,iD=iD,message=message,id2=r2id,iD2=r2iD,id3=r3id,iD3=r3iD,p=P)
                elif session.get('P') == '4':
                    id = session.get('id')
                    iD = session.get('iD')
                    r2id = session.get('r2id')
                    r2iD = session.get('r2iD')
                    r3id = session.get('r3id')
                    r3iD = session.get('r3iD')
                    r4id = session.get('r4id')
                    r4iD = session.get('r4iD')
                    P = 'PUNTAJE ACTUAL: ' + session.get('P')
                    message = 'La ronda 4 es correcta, vuelve a iniciar ronda 5'
                    session.pop('r5id',None)
                    session.pop('r5iD',None)
                    session.pop('F',None)
                    return render_template('main_memo.html',id=id,iD=iD,message=message,id2=r2id,iD2=r2iD,id3=r3id,iD3=r3iD,id4=r4id,iD4=r4iD,p=P)
                elif session.get('P') == '5':
                    id = session.get('id')
                    iD = session.get('iD')
                    r2id = session.get('r2id')
                    r2iD = session.get('r2iD')
                    r3id = session.get('r3id')
                    r3iD = session.get('r3iD')
                    r4id = session.get('r4id')
                    r4iD = session.get('r4iD')
                    r5id = session.get('r5id')
                    r5iD = session.get('r5iD')
                    P = 'PUNTAJE ACTUAL: ' + session.get('P')
                    message = 'La ronda 5 es correcta, vuelve a iniciar ronda 6'
                    session.pop('r6id',None)
                    session.pop('r6iD',None)
                    session.pop('F',None)
                    return render_template('main_memo.html',id=id,iD=iD,message=message,id2=r2id,iD2=r2iD,id3=r3id,iD3=r3iD,id4=r4id,iD4=r4iD,id5=r5id,iD5=r5iD,p=P)
                else:
                    session.clear()
                    return render_template('main_memo.html')
            elif session.get('P') == '6':
                id = session.get('id')
                iD = session.get('iD')
                r2id = session.get('r2id')
                r2iD = session.get('r2iD')
                r3id = session.get('r3id')
                r3iD = session.get('r3iD')
                r4id = session.get('r4id')
                r4iD = session.get('r4iD')
                r5id = session.get('r5id')
                r5iD = session.get('r5iD')            
                r6id = session.get('r6id')
                r6iD = session.get('r6iD')
                message = 'Juego resuelto, felicidades!... AHORA SI VIENE LO CHIDO'            
                return render_template('main_memo.html',id=id,iD=iD,id2=r2id,iD2=r2iD,id3=r3id,iD3=r3iD,id4=r4id,iD4=r4iD,id5=r5id,iD5=r5iD,id6=r6id,iD6=r6iD, message = message)
            elif session.get('P') == '5':
                id = session.get('id')
                iD = session.get('iD')
                r2id = session.get('r2id')
                r2iD = session.get('r2iD')
                r3id = session.get('r3id')
                r3iD = session.get('r3iD')
                r4id = session.get('r4id')
                r4iD = session.get('r4iD')
                r5id = session.get('r5id')
                r5iD = session.get('r5iD')
                results = [1.1,2.2,3.3,4.4,5.5,6.6]
                if session.get('r6id'):
                    r6id = session.get('r6id')
                    r6iD = request.form.get('id')
                    r6a = float(r6id)
                    r6b = float(r6iD)
                    r6RF = r6a + r6b                   
                    r6rf = str(r6RF)
                    if r6iD == id:
                        message = 'Ya se ha seleccionado previamente el id (' + id + ') en la primer ronda'
                        return render_template('main_memo.html',message=message,id=id,iD=iD,id2=r2id,iD2=r2iD, id3=r3id, iD3=r3iD,id4=r4id,iD4=r4iD,id5=r5id,iD5=r5iD,id6=r6id)
                    elif r6iD == iD:
                        message = 'Ya se ha seleccionado previamente el iD (' + iD + ') en la primer ronda'    
                        return render_template('main_memo.html',message=message,id=id,iD=iD,id2=r2id,iD2=r2iD, id3=r3id, iD3=r3iD,id4=r4id,iD4=r4iD,id5=r5id,iD5=r5iD,id6=r6id)
                    elif r6iD == r2id:
                        message = 'Ya se ha seleccionado previamente el id (' + r2id + ') en la segunda ronda'
                        return render_template('main_memo.html',message=message,id=id,iD=iD,id2=r2id,iD2=r2iD, id3=r3id, iD3=r3iD,id4=r4id,iD4=r4iD,id5=r5id,iD5=r5iD,id6=r6id)
                    elif r6iD == r2iD:
                        message = 'Ya se ha seleccionado previamente el iD (' + r2iD + ') en la segunda ronda'    
                        return render_template('main_memo.html',message=message,id=id,iD=iD,id2=r2id,iD2=r2iD, id3=r3id, iD3=r3iD,id4=r4id,iD4=r4iD,id5=r5id,iD5=r5iD,id6=r6id)
                    elif r6iD == r3id:
                        message = 'Ya se ha seleccionado previamente el id (' + r3id + ') en la tercera ronda'
                        return render_template('main_memo.html',message=message,id=id,iD=iD,id2=r2id,iD2=r2iD, id3=r3id, iD3=r3iD,id4=r4id,iD4=r4iD,id5=r5id,iD5=r5iD,id6=r6id)
                    elif r6iD == r3iD:
                        message = 'Ya se ha seleccionado previamente el iD (' + r3iD + ') en la tercera ronda'    
                        return render_template('main_memo.html',message=message,id=id,iD=iD,id2=r2id,iD2=r2iD, id3=r3id, iD3=r3iD,id4=r4id,iD4=r4iD,id5=r5id,iD5=r5iD,id6=r6id)
                    elif r6iD == r4id:
                        message = 'Ya se ha seleccionado previamente el id (' + r4id + ') en la cuarta ronda'
                        return render_template('main_memo.html',message=message,id=id,iD=iD,id2=r2id,iD2=r2iD, id3=r3id, iD3=r3iD,id4=r4id,iD4=r4iD,id5=r5id,iD5=r5iD,id6=r6id)
                    elif r6iD == r4iD:
                        message = 'Ya se ha seleccionado previamente el iD (' + r4iD + ') en la cuarta ronda'    
                        return render_template('main_memo.html',message=message,id=id,iD=iD,id2=r2id,iD2=r2iD, id3=r3id, iD3=r3iD,id4=r4id,iD4=r4iD,id5=r5id,iD5=r5iD,id6=r6id)
                    elif r6iD == r5id:
                        message = 'Ya se ha seleccionado previamente el id (' + r5id + ') en la quinta ronda'
                        return render_template('main_memo.html',message=message,id=id,iD=iD,id2=r2id,iD2=r2iD, id3=r3id, iD3=r3iD,id4=r4id,iD4=r4iD,id5=r5id,iD5=r5iD,id6=r6id)
                    elif r6iD == r5iD:
                        message = 'Ya se ha seleccionado previamente el iD (' + r5iD + ') en la quinta ronda'    
                        return render_template('main_memo.html',message=message,id=id,iD=iD,id2=r2id,iD2=r2iD, id3=r3id, iD3=r3iD,id4=r4id,iD4=r4iD,id5=r5id,iD5=r5iD,id6=r6id)
                    elif r6iD == r6id:
                        session.pop('r6id')
                        r6PA = 'PUNTAJE ACTUAL ' + session.get('P')
                        message = 'Se ha quitado la seleccion'    
                        return render_template('main_memo.html',message=message,id=id,iD=iD,id2=r2id,iD2=r2iD, id3=r3id, iD3=r3iD, id4=r4id, iD4=r4iD,id5=r5id,iD5=r5iD, p=r6PA)
                    if r6RF in results:
                        r6rfo = 'CORRECTO ' + r6rf
                        r6p = int(session.get('P'))
                        r6P = str(r6p+1)
                        session['P'] = r6P
                        r6PA = 'PUNTAJE ACTUAL: ' + r6P
                        session['r6iD'] = r6iD
                        return render_template('main_memo.html',id=id,iD=iD,id2=r2id,iD2=r2iD,id3=r3id,iD3=r3iD,id4=r4id,iD4=r4iD,id5=r5id,iD5=r5iD,id6=r6id,iD6=r6iD,rf=r6rfo,p=r6PA)
                    else:
                        r6rfo = 'NO SE ENCUENTRA EN RESULTADOS | id (' + r6id + ') + iD (' + r6iD + ') = (' + r6rf + ').'
                        session['F'] = 1
                        F = session.get('F')
                        return render_template('main_memo.html',message=r6rfo, id=id,iD=iD,id2=r2id,iD2=r2iD,id3=r3id,iD3=r3iD,id4=r4id,iD4=r4iD,id5=r5id,iD5=r5iD, F=F)
                else:
                    r6id = request.form.get('id')
                    if r6id== id:
                        message = 'Ya se ha seleccionado previamente el id (' + id + ') en la primer ronda'
                        return render_template('main_memo.html',message=message,id=id,iD=iD,id2=r2id,iD2=r2iD, id3=r3id,iD3=r3iD, id4=r4id,iD4=r4iD, id5=r5id,iD5=r5iD)
                    elif r6id == iD:
                        message = 'Ya se ha seleccionado previamente el iD (' + iD + ') en la primer ronda'    
                        return render_template('main_memo.html',message=message,id=id,iD=iD,id2=r2id,iD2=r2iD, id3=r3id,iD3=r3iD, id4=r4id,iD4=r4iD, id5=r5id,iD5=r5iD)
                    elif r6id == r2id:
                        message = 'Ya se ha seleccionado previamente el id (' + r2id + ') en la segunda ronda'
                        return render_template('main_memo.html',message=message,id=id,iD=iD,id2=r2id,iD2=r2iD, id3=r3id,iD3=r3iD, id4=r4id,iD4=r4iD, id5=r5id,iD5=r5iD)
                    elif r6id == r2iD:
                        message = 'Ya se ha seleccionado previamente el iD (' + r2iD + ') en la segunda ronda'    
                        return render_template('main_memo.html',message=message,id=id,iD=iD,id2=r2id,iD2=r2iD, id3=r3id,iD3=r3iD, id4=r4id,iD4=r4iD, id5=r5id,iD5=r5iD)
                    elif r6id == r3id:
                        message = 'Ya se ha seleccionado previamente el id (' + r3id + ') en la tercera ronda'
                        return render_template('main_memo.html',message=message,id=id,iD=iD,id2=r2id,iD2=r2iD, id3=r3id,iD3=r3iD, id4=r4id,iD4=r4iD, id5=r5id,iD5=r5iD)
                    elif r6id == r3iD:
                        message = 'Ya se ha seleccionado previamente el iD (' + r3iD + ') en la tercera ronda'    
                        return render_template('main_memo.html',message=message,id=id,iD=iD,id2=r2id,iD2=r2iD, id3=r3id,iD3=r3iD, id4=r4id,iD4=r4iD, id5=r5id,iD5=r5iD)
                    elif r6id == r4id:
                        message = 'Ya se ha seleccionado previamente el id (' + r4id + ') en la cuarta ronda'
                        return render_template('main_memo.html',message=message,id=id,iD=iD,id2=r2id,iD2=r2iD, id3=r3id,iD3=r3iD, id4=r4id,iD4=r4iD, id5=r5id,iD5=r5iD)
                    elif r6id == r4iD:
                        message = 'Ya se ha seleccionado previamente el iD (' + r4iD + ') en la cuarta ronda'    
                        return render_template('main_memo.html',message=message,id=id,iD=iD,id2=r2id,iD2=r2iD, id3=r3id,iD3=r3iD, id4=r4id,iD4=r4iD, id5=r5id,iD5=r5iD)
                    elif r6id == r5id:
                        message = 'Ya se ha seleccionado previamente el id (' + r5id + ') en la quinta ronda'
                        return render_template('main_memo.html',message=message,id=id,iD=iD,id2=r2id,iD2=r2iD, id3=r3id,iD3=r3iD, id4=r4id,iD4=r4iD, id5=r5id,iD5=r5iD)
                    elif r6id == r5iD:
                        message = 'Ya se ha seleccionado previamente el iD (' + r5iD + ') en la quinta ronda'    
                        return render_template('main_memo.html',message=message,id=id,iD=iD,id2=r2id,iD2=r2iD, id3=r3id,iD3=r3iD, id4=r4id,iD4=r4iD, id5=r5id,iD5=r5iD)
                    session['r6id'] = r6id
                    message = '(' + r6id + ') id en sesión6.'            
                    return render_template('main_memo.html', id=id,iD=iD,id2=r2id,iD2=r2iD,id3=r3id,iD3=r3iD,id4=r4id,iD4=r4iD,id5=r5id,iD5=r5iD,id6=r6id,message=message)
            elif session.get('P') == '4':
                id = session.get('id')
                iD = session.get('iD')
                r2id = session.get('r2id')
                r2iD = session.get('r2iD')
                r3id = session.get('r3id')
                r3iD = session.get('r3iD')
                r4id = session.get('r4id')
                r4iD = session.get('r4iD')
                results = [1.1,2.2,3.3,4.4,5.5,6.6]
                if session.get('r5id'):
                    r5id = session.get('r5id')
                    r5iD = request.form.get('id')
                    r5a = float(r5id)
                    r5b = float(r5iD)
                    r5RF = r5a + r5b                   
                    r5rf = str(r5RF)
                    if r5iD == id:
                        message = 'Ya se ha seleccionado previamente el id (' + id + ') en la primer ronda'
                        return render_template('main_memo.html',message=message,id=id,iD=iD,id2=r2id,iD2=r2iD, id3=r3id, iD3=r3iD,id4=r4id,iD4=r4iD,id5=r5id)
                    elif r5iD == iD:
                        message = 'Ya se ha seleccionado previamente el iD (' + iD + ') en la primer ronda'    
                        return render_template('main_memo.html',message=message,id=id,iD=iD,id2=r2id,iD2=r2iD, id3=r3id, iD3=r3iD,id4=r4id,iD4=r4iD,id5=r5id)
                    elif r5iD == r2id:
                        message = 'Ya se ha seleccionado previamente el id (' + r2id + ') en la segunda ronda'
                        return render_template('main_memo.html',message=message,id=id,iD=iD,id2=r2id,iD2=r2iD, id3=r3id, iD3=r3iD,id4=r4id,iD4=r4iD,id5=r5id)
                    elif r5iD == r2iD:
                        message = 'Ya se ha seleccionado previamente el iD (' + r2iD + ') en la segunda ronda'    
                        return render_template('main_memo.html',message=message,id=id,iD=iD,id2=r2id,iD2=r2iD, id3=r3id, iD3=r3iD,id4=r4id,iD4=r4iD,id5=r5id)
                    elif r5iD == r3id:
                        message = 'Ya se ha seleccionado previamente el id (' + r3id + ') en la tercera ronda'
                        return render_template('main_memo.html',message=message,id=id,iD=iD,id2=r2id,iD2=r2iD, id3=r3id, iD3=r3iD,id4=r4id,iD4=r4iD,id5=r5id)
                    elif r5iD == r3iD:
                        message = 'Ya se ha seleccionado previamente el iD (' + r3iD + ') en la tercera ronda'    
                        return render_template('main_memo.html',message=message,id=id,iD=iD,id2=r2id,iD2=r2iD, id3=r3id, iD3=r3iD,id4=r4id,iD4=r4iD,id5=r5id)
                    elif r5iD == r4id:
                        message = 'Ya se ha seleccionado previamente el id (' + r4id + ') en la cuarta ronda'
                        return render_template('main_memo.html',message=message,id=id,iD=iD,id2=r2id,iD2=r2iD, id3=r3id, iD3=r3iD,id4=r4id,iD4=r4iD,id5=r5id)
                    elif r5iD == r4iD:
                        message = 'Ya se ha seleccionado previamente el iD (' + r4iD + ') en la cuarta ronda'    
                        return render_template('main_memo.html',message=message,id=id,iD=iD,id2=r2id,iD2=r2iD, id3=r3id, iD3=r3iD,id4=r4id,iD4=r4iD,id5=r5id)
                    elif r5iD == r5id:
                        session.pop('r5id')
                        r5PA = 'PUNTAJE ACTUAL ' + session.get('P')
                        message = 'Se ha quitado la seleccion'    
                        return render_template('main_memo.html',message=message,id=id,iD=iD,id2=r2id,iD2=r2iD, id3=r3id, iD3=r3iD, id4=r4id, iD4=r4iD, p=r5PA)
                    if r5RF in results:
                        r5rfo = 'CORRECTO ' + r5rf
                        r5p = int(session.get('P'))
                        r5P = str(r5p+1)
                        session['P'] = r5P
                        r5PA = 'PUNTAJE ACTUAL: ' + r5P
                        session['r5iD'] = r5iD
                        return render_template('main_memo.html',id=id,iD=iD,id2=r2id,iD2=r2iD,id3=r3id,iD3=r3iD,id4=r4id,iD4=r4iD,id5=r5id,iD5=r5iD,rf=r5rfo,p=r5PA)
                    else:
                        r5rfo = 'NO SE ENCUENTRA EN RESULTADOS | id (' + r5id + ') + iD (' + r5iD + ') = (' + r5rf + ').'
                        session['F'] = 1
                        F = session.get('F')
                        return render_template('main_memo.html',message=r5rfo, id=id,iD=iD,id2=r2id,iD2=r2iD,id3=r3id,iD3=r3iD,id4=r4id,iD4=r4iD, F=F)
                else:
                    r5id = request.form.get('id')
                    if r5id== id:
                        message = 'Ya se ha seleccionado previamente el id (' + id + ') en la primer ronda'
                        return render_template('main_memo.html',message=message,id=id,iD=iD,id2=r2id,iD2=r2iD, id3=r3id,iD3=r3iD, id4=r4id,iD4=r4iD)
                    elif r5id == iD:
                        message = 'Ya se ha seleccionado previamente el iD (' + iD + ') en la primer ronda'    
                        return render_template('main_memo.html',message=message,id=id,iD=iD,id2=r2id,iD2=r2iD, id3=r3id,iD3=r3iD, id4=r4id,iD4=r4iD)
                    elif r5id == r2id:
                        message = 'Ya se ha seleccionado previamente el id (' + r2id + ') en la segunda ronda'
                        return render_template('main_memo.html',message=message,id=id,iD=iD,id2=r2id,iD2=r2iD, id3=r3id,iD3=r3iD, id4=r4id,iD4=r4iD)
                    elif r5id == r2iD:
                        message = 'Ya se ha seleccionado previamente el iD (' + r2iD + ') en la segunda ronda'    
                        return render_template('main_memo.html',message=message,id=id,iD=iD,id2=r2id,iD2=r2iD, id3=r3id,iD3=r3iD, id4=r4id,iD4=r4iD)
                    elif r5id == r3id:
                        message = 'Ya se ha seleccionado previamente el id (' + r3id + ') en la tercera ronda'
                        return render_template('main_memo.html',message=message,id=id,iD=iD,id2=r2id,iD2=r2iD, id3=r3id,iD3=r3iD, id4=r4id,iD4=r4iD)
                    elif r5id == r3iD:
                        message = 'Ya se ha seleccionado previamente el iD (' + r3iD + ') en la tercera ronda'    
                        return render_template('main_memo.html',message=message,id=id,iD=iD,id2=r2id,iD2=r2iD, id3=r3id,iD3=r3iD, id4=r4id,iD4=r4iD)
                    elif r5id == r4id:
                        message = 'Ya se ha seleccionado previamente el id (' + r4id + ') en la cuarta ronda'
                        return render_template('main_memo.html',message=message,id=id,iD=iD,id2=r2id,iD2=r2iD, id3=r3id,iD3=r3iD, id4=r4id,iD4=r4iD)
                    elif r5id == r4iD:
                        message = 'Ya se ha seleccionado previamente el iD (' + r4iD + ') en la cuarta ronda'    
                        return render_template('main_memo.html',message=message,id=id,iD=iD,id2=r2id,iD2=r2iD, id3=r3id,iD3=r3iD, id4=r4id,iD4=r4iD)
                    session['r5id'] = r5id
                    message = '(' + r5id + ') id en sesión5.'            
                    return render_template('main_memo.html', id=id,iD=iD,id2=r2id,iD2=r2iD,id3=r3id,iD3=r3iD,id4=r4id,iD4=r4iD,id5=r5id,message=message)
            elif session.get('P') == '3':
                id = session.get('id')
                iD = session.get('iD')
                r2id = session.get('r2id')
                r2iD = session.get('r2iD')
                r3id = session.get('r3id')
                r3iD = session.get('r3iD')
                results = [1.1,2.2,3.3,4.4,5.5,6.6]
                if session.get('r4id'):
                    r4id = session.get('r4id')
                    r4iD = request.form.get('id')
                    r4a = float(r4id)
                    r4b = float(r4iD)
                    r4RF = r4a + r4b                   
                    r4rf = str(r4RF)
                    if r4iD == id:
                        message = 'Ya se ha seleccionado previamente el id (' + id + ') en la primer ronda'
                        return render_template('main_memo.html',message=message,id=id,iD=iD,id2=r2id,iD2=r2iD, id3=r3id, iD3=r3iD,id4=r4id)
                    elif r4iD == iD:
                        message = 'Ya se ha seleccionado previamente el iD (' + iD + ') en la primer ronda'    
                        return render_template('main_memo.html',message=message,id=id,iD=iD,id2=r2id,iD2=r2iD, id3=r3id, iD3=r3iD,id4=r4id)
                    elif r4iD == r2id:
                        message = 'Ya se ha seleccionado previamente el id (' + r2id + ') en la segunda ronda'
                        return render_template('main_memo.html',message=message,id=id,iD=iD,id2=r2id,iD2=r2iD, id3=r3id, iD3=r3iD,id4=r4id)
                    elif r4iD == r2iD:
                        message = 'Ya se ha seleccionado previamente el iD (' + r2iD + ') en la segunda ronda'    
                        return render_template('main_memo.html',message=message,id=id,iD=iD,id2=r2id,iD2=r2iD, id3=r3id, iD3=r3iD,id4=r4id)
                    elif r4iD == r3id:
                        message = 'Ya se ha seleccionado previamente el id (' + r3id + ') en la tercera ronda'
                        return render_template('main_memo.html',message=message,id=id,iD=iD,id2=r2id,iD2=r2iD, id3=r3id, iD3=r3iD,id4=r4id)
                    elif r4iD == r3iD:
                        message = 'Ya se ha seleccionado previamente el iD (' + r3iD + ') en la tercera ronda'    
                        return render_template('main_memo.html',message=message,id=id,iD=iD,id2=r2id,iD2=r2iD, id3=r3id, iD3=r3iD,id4=r4id)
                    elif r4iD == r4id:
                        session.pop('r4id')
                        r4PA = 'PUNTAJE ACTUAL ' + session.get('P')
                        message = 'Se ha quitado la seleccion'    
                        return render_template('main_memo.html',message=message,id=id,iD=iD,id2=r2id,iD2=r2iD, id3=r3id, iD3=r3iD, p=r4PA)
                    if r4RF in results:
                        r4rfo = 'CORRECTO ' + r4rf
                        r4p = int(session.get('P'))
                        r4P = str(r4p+1)
                        session['P'] = r4P
                        r4PA = 'PUNTAJE ACTUAL: ' + r4P
                        session['r4iD'] = r4iD
                        return render_template('main_memo.html',id=id,iD=iD,id2=r2id,iD2=r2iD,id3=r3id,iD3=r3iD,id4=r4id,iD4=r4iD,rf=r4rfo,p=r4PA)
                    else:
                        r4rfo = 'NO SE ENCUENTRA EN RESULTADOS | id (' + r4id + ') + iD (' + r4iD + ') = (' + r4rf + ').'
                        session['F'] = 1
                        F = session.get('F')
                        return render_template('main_memo.html',message=r4rfo, id=id,iD=iD,id2=r2id,iD2=r2iD,id3=r3id,iD3=r3iD, F=F)
                else:
                    r4id = request.form.get('id')
                    if r4id== id:
                        message = 'Ya se ha seleccionado previamente el id (' + id + ') en la primer ronda'
                        return render_template('main_memo.html',message=message,id=id,iD=iD,id2=r2id,iD2=r2iD, id3=r3id,iD3=r3iD)
                    elif r4id == iD:
                        message = 'Ya se ha seleccionado previamente el iD (' + iD + ') en la primer ronda'    
                        return render_template('main_memo.html',message=message,id=id,iD=iD,id2=r2id,iD2=r2iD, id3=r3id,iD3=r3iD)
                    elif r4id == r2id:
                        message = 'Ya se ha seleccionado previamente el id (' + r2id + ') en la segunda ronda'
                        return render_template('main_memo.html',message=message,id=id,iD=iD,id2=r2id,iD2=r2iD, id3=r3id,iD3=r3iD)
                    elif r4id == r2iD:
                        message = 'Ya se ha seleccionado previamente el iD (' + r2iD + ') en la segunda ronda'    
                        return render_template('main_memo.html',message=message,id=id,iD=iD,id2=r2id,iD2=r2iD, id3=r3id,iD3=r3iD)
                    elif r4id == r3id:
                        message = 'Ya se ha seleccionado previamente el id (' + r3id + ') en la tercera ronda'
                        return render_template('main_memo.html',message=message,id=id,iD=iD,id2=r2id,iD2=r2iD, id3=r3id,iD3=r3iD)
                    elif r4id == r3iD:
                        message = 'Ya se ha seleccionado previamente el iD (' + r3iD + ') en la tercera ronda'    
                        return render_template('main_memo.html',message=message,id=id,iD=iD,id2=r2id,iD2=r2iD, id3=r3id,iD3=r3iD)
                    session['r4id'] = r4id
                    message = '(' + r4id + ') id en sesión4.'            
                    return render_template('main_memo.html', id=id,iD=iD,id2=r2id,iD2=r2iD,id3=r3id,iD3=r3iD,id4=r4id,message=message)
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
        message = 'Bienvenido al memorama. ¿Deseas comenzar?'
        start = 1
        session['start'] = start
        return render_template('main_memo.html',message=message,start=start)
    return app

app = create_app()