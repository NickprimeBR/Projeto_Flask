from dao.db_cofig import get_connection

class TurmaDAO:
    sqlSelect="select turma.id,turma.semestre,curso.nome_curso,professor.nome,professor.disciplina from turma join curso on curso.id=turma.curso_id join professor on professor.id=turma.professor_id"
    
    def listar(self):
        conn = get_connection()
            
        cursor = conn.cursor()
        cursor.execute(self.sqlSelect)
            
        lista = cursor.fetchall()
        
        return lista

