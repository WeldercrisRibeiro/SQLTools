import base64

# Substitua pelo caminho do seu ícone (.ico, por exemplo)
icon_path = 'src/icons/sqlIco.ico'

def icon_to_base64(icon_path):
    with open(icon_path, 'rb') as icon_file:
        icon_bytes = icon_file.read()
        icon_base64 = base64.b64encode(icon_bytes).decode('utf-8')
        return icon_base64

# Chamando a função para converter o ícone para base64
icon_base64 = icon_to_base64(icon_path)

# Exibindo o resultado
print(icon_base64)
