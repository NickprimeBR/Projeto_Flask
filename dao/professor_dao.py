from dao.db_cofig import get_connection

class ProfessorDAO:
    sqlSelect="SELECT id, nome, disciplina FROM professor"
    
    def listar(self):
        conn = get_connection()
            
        cursor = conn.cursor()
        cursor.execute(self.sqlSelect)
            
        lista = cursor.fetchall()
        
        return lista

