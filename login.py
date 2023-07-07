from PySimpleGUI import PySimpleGUI as sg





sg.theme('Reddit')

senhas = []
usuarios = []



layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario')],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*')],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')],
    [sg.Button('Cadastrar')]
    
]

layout_cadastro = [
    [sg.Text('Usuário Cadastrado')],
    

]

layout2 = [
    [sg.Text('BEM VINDO USUARIO')]
]

layout3 = [
    [sg.Text('Usuario invalido')]
]


janela = sg.Window('Tela de Login', layout)
janela2 = sg.Window('Bem vindo(a)', layout2)
janela3 = sg.Window('Acesso negado', layout3)
janela_cadastro = sg.Window('Cadastro', layout_cadastro)


while True:
    eventos, valores = janela.read()
    if eventos ==sg.WINDOW_CLOSED:
        break
    
        
    if eventos == 'Entrar':
        if valores['usuario'] in usuarios and valores['senha'] in senhas:
            janela.close()
            janela2.read()
        else:
            janela.close()
            janela3.read()
    elif eventos =='Cadastrar':
        usuarios.append(valores['usuario'])
        senhas.append(valores['senha'])
        janela_cadastro.read()
        
        
        
        

        
