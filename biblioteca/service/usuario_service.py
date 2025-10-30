from dados.database import conectar

def salvar_usuario(usuario):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (cpf, nome) VALUES (?, ?)", (usuario.cpf, usuario.nome))
    conn.commit()
    conn.close()
    
def listar_usuarios():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT cpf, nome FROM usuarios")
    usuarios = cursor.fetchall()
    conn.close()
    return usuarios