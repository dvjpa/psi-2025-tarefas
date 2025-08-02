from django.shortcuts import render

def index(request):
    return render(request, 'app/index.html')

def usuarios(request):
    usuarios = [
        {'nome': 'João Silva', 'matricula': '2025001', 'idade': 17, 'cidade': 'Natal'},
        {'nome': 'Maria Souza', 'matricula': '2025002', 'idade': 18, 'cidade': 'Mossoró'},
        {'nome': 'Pedro Lima', 'matricula': '2025003', 'idade': 19, 'cidade': 'Caicó'},
        {'nome': 'Ana Beatriz', 'matricula': '2025004', 'idade': 17, 'cidade': 'Parnamirim'},
        {'nome': 'Lucas Araújo', 'matricula': '2025005', 'idade': 20, 'cidade': 'Currais Novos'},
    ]
    return render(request, 'app/usuarios.html', {'usuarios': usuarios})