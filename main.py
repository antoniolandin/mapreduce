import os

if __name__ == "__main__":
    
    # Obtener número de peticiones de tipo GET
    
    os.system("cat apache.log | ./m1.py | ./r1.py")