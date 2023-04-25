import os
#from sys import exit
import json

def main():
    # Abrimos el archivo JSON
    with open('output.json') as contenido:
        # Lo transformamos a diccionario 
        dic = json.load(contenido)
        # Itermos en sus recursos: "ApiGatewayApi", "HelloWorldFunction"
        for item in dic['Resources'].keys():
            # Si existe "Type" => AWS::Serverless::Function, Aplicamos la regla
            if dic['Resources'][item]['Type'] == 'AWS::Serverless::Function':
                try:
                    name = dic['Resources'][item]['Properties']['FunctionName']
                    print(f'Sí existe "Properties":"FunctionName" en {item}')
                    if len(name)>= 10:
                        print(f'El nombre {name} es demaciado largo')
                    else:
                        print(f'El nombre {name} esta en la longitud correcta')
                # Si en recurso NO existe "FunctionName", lo ignoramos
                except:
                    print(f'No existe "Properties":"FunctionName" en {item} \n')


if __name__ == '__main__':
    main()