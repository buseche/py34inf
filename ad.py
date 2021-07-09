#agregamos la librera os para usar los comandos shell
import os
#Verificamos que tipo de usuario ejecuta el script
user = os.popen("echo $USER").read()
#Obtenemos el nombre del host
hostname = os.popen("hostname").read()
#Obtenemos el nombre del servidor de AD, y lo ponemos en mayusculas porsia
servername = input("Introduzca el nombre del servidor: ").upper()
#Obtenemos la direccion ip del servidor
addrIp = input("Introduzca la direccion ip del servidor: ")
#Obtenemos el nombre del dominio
domain = input("Introduzca el nombre del dominio: ").lower()
#Imprimimos los datos antes de continuar
print("Los siguientes datos fueron introducidos: \n")
print("Usuario: ", user)
print("Host   : ", servername)
print("IP     : ", addrIp)
print("Dominio: ", domain)
args = input("Es correcto?[S/n]: ")
if args == 'n' or args == 'N' or len(args) == 0:
    print("Corrija los datos y vuelva a correr el script")
else:
    print("Se continuara la instalacion")
    #Empezamos a modificar los archivos que necesitamos
    #Modificamos el archivo /etc/hosts
    command = ["echo '","%s    %s      %s.%s" % (addrIp, servername, servername, domain),"'>> /etc/hosts"]
    cmd = ''
    print(os.popen(cmd.join(command)).read())
    

    
        
        
    

