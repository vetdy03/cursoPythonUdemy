def get_product(**datos):
    print(datos["id"], datos["name"])
    
get_product(id="id",
            name="android",
            desc= "este es un android")