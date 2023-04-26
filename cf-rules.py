import json
from sys import exit # Código de salida: https://linuxhint.com/python-exit-codes/
import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
    "-f",
    "--file-name",
    dest="file",
    required=True,
    help="Archivo template en formato json"
)

def main():
    args = parser.parse_args()
    fileVariables = args.file
    
    # Abrimos el archivo JSON
    with open(fileVariables) as contenido:
        # Lo transformamos a diccionario 
        const, dic = 0, json.load(contenido)
        # Itermos en sus recursos,
        for item in dic['Resources'].keys():
            # "Type" => AWS::Serverless::Function, 
            if dic['Resources'][item]['Type'] == 'AWS::Serverless::Function':
                name = dic['Resources'][item]['Properties']['FunctionName']['Fn::Sub'].replace('${EnvName}', '')
                numCaract = 64 - 7
            # "Type" => AWS::Serverless::Function, 
            elif dic['Resources'][item]['Type'] == 'AWS::S3::Bucket':
                name = dic['Resources'][item]['Properties']['BucketName']['Fn::Sub'].replace('${EnvName}', '')
                numCaract = 63 - 7
            # "Type" => AWS::Events::Rule, 
            elif dic['Resources'][item]['Type'] == 'AWS::Events::Rule':
                name = dic['Resources'][item]['Properties']['EventBusName']['Fn::Sub'].replace('${EnvName}', '')
                numCaract = 64 - 7

            # REGLAS:
            try:
                # (1) Validamos caracteres
                if len(name) <= numCaract:
                    print(f'-> Para "{item}" el nombre: "{name}", esta en la longitud correcta. [✅]')
                else:
                    print(f'-> Para "{item}" el nombre: "{name}", es demaciado largo. [❌]')
                    const += 1
                # (2) Validamos que no exista otro "${"
                if name.find("${") != -1 : const += 1 
            # En caso de no haber problemas, ignoramos
            except:
                pass
        # Si al menos una regla no se cumple, se levanta un error:
        if const != 0 : exit("Error en la longitud de los caracteres permitidos.")

if __name__ == '__main__':
    main()