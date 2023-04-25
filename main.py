from sys import exit
import json

def main():
    # Abrimos el archivo JSON
    with open('output.json') as contenido:
        # Lo transformamos a diccionario 
        const, dic = 0, json.load(contenido)
        # Itermos en sus recursos: "ApiGatewayApi", "HelloWorldFunction"
        print('\nEvaluación de caracteres para los tipos: "AWS::Serverless::Function."')
        for item in dic['Resources'].keys():
            # Si existe "Type" => AWS::Serverless::Function, Aplicamos la regla
            if dic['Resources'][item]['Type'] == 'AWS::Serverless::Function':
                try:
                    name = dic['Resources'][item]['Properties']['FunctionName']['Fn::Sub']
                    if len(name) <= 10:
                        print(f'-> Para "{item}" el nombre: "{name}", esta en la longitud correcta. [✅]')
                    else:
                        print(f'-> Para "{item}" el nombre: "{name}", es demaciado largo. [❌]')
                        const += 1
                # Si en recurso NO existe "FunctionName", lo ignoramos
                except:
                    print(f'No existe "Properties":"FunctionName" en {item} \n')
            if const != 0: exit("Error en la longitud de los caracteres permitidos.")


if __name__ == '__main__':
    main()