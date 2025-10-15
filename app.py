from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_aqui'  # Cambia esto por una clave secreta real

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
    """Página principal"""
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

@app.route('/admin')
def admin():
    """Página de administración para ver los contactos (opcional)"""
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM contactos ORDER BY fecha DESC')
        contactos = cursor.fetchall()
        conn.close()
        
        return render_template('admin.html', contactos=contactos)
    except Exception as e:
        flash('Error al cargar los contactos.', 'error')
        return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0', port=5000)
