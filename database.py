import certifi
from motor.motor_asyncio import AsyncIOMotorClient
# URL de conexion a mogobd
MONGO_URL = "mongodb+srv://carrytecphd_db_user:7D66c19UuTnOpyg1@cluster0.ectokuj.mongodb.net/"


# Conexión al cliente
client = AsyncIOMotorClient(MONGO_URL,
tlsCAFile=certifi.where())  

# Selección a nuestra base de datos
database = client.mibasededatos 

# Selección de una colección
collection = database.get_collection("micoleccion")
