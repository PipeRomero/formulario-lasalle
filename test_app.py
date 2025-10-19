from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_aqui'

# Configuración de la base de datos
DATABASE = 'contactos.db'

def init_db():
    """Inicializa la base de datos con la tabla de contactos"""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contactos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            email TEXT NOT NULL,
            telefono TEXT,
            mensaje TEXT NOT NULL,
            fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    """Formulario de contacto"""
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        telefono = request.form.get('telefono', '')
        mensaje = request.form['mensaje']
        
        # Validación básica
        if not nombre or not email or not mensaje:
            flash('Por favor, completa todos los campos obligatorios.', 'error')
            return render_template('contacto.html')
        
        # Guardar en la base de datos
        try:
            conn = sqlite3.connect(DATABASE)
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO contactos (nombre, email, telefono, mensaje)
                VALUES (?, ?, ?, ?)
            ''', (nombre, email, telefono, mensaje))
            conn.commit()
            conn.close()
            
            flash('¡Mensaje enviado correctamente! Te contactaremos pronto.', 'success')
            return redirect(url_for('index'))
            
        except Exception as e:
            flash('Error al enviar el mensaje. Por favor, inténtalo de nuevo.', 'error')
            return render_template('contacto.html')
    
    return render_template('contacto.html')

if __name__ == '__main__':
    init_db()
    print("Iniciando servidor Flask...")
    print("Ve a: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)
