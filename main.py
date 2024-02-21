from fastapi import FastAPI, HTTPException 
from pydantic import BaseModel
import mysql.connector

app = FastAPI()

db = mysql.connector.connect(
    host = 'monorail.proxy.rlwy.net',
    port = 26677,
    user = 'root',
    password = 'FbFce1-A2gFDg1BD25EC36DhahBC1c6-',
    database = 'railway'
)

cursor = db.cursor()

class Time(BaseModel):
    id: int
    clube: str
    cidade: str
    uf: str
    estadio: str
    competicao: str

@app.get('/times')
def get_items():
    try :
        cursor.execute('SELECT * FROM times ORDER BY clube')
        times = [{'id': row[0], 'clube': row[1], 'cidade': row[2], 'uf': row[3], 'estadio': row[4], 'competicao': row[5]} for row in cursor.fetchall()]
        return times
    except:
        raise HTTPException(status_code=500, detail='Database error')