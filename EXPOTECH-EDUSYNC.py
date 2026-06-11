import mysql.connector
import getpass
import tabulate
import os

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='edusync02'
    )
cursor= conexao.cursor()


while True:
    print('='*60)
    print('📚 Sistema de Gestão e Consulta Escolar Edusync 📚'.center(60))
    print('='*60)
    print('                                 ')
    print('1 - Acessar Gestão')
    print('2 - Acessar Professor')
    print('3 - Acessar Aluno')
    print('4-  Sair')
    opcao = input('Selecione uma opção: ')
    if opcao == '1':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('                                 ')
        print('='*60)
        print('📚 Sistema da Gestão 📚'.center(60))
        print('='*60)
        usu=input('👤 Digite seu usuário: ').strip()
        senha=getpass.getpass('🔒 Digite sua senha: ').strip()
        comando= 'select * from gestao where gestao_usu = %s and gestao_senha = %s'
        if usu == '' or senha == '':
            print('Nenhuma inserção de dados pode ficar vázio')
            input('Pressione enter para voltar ao menu de opções...')
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            cursor.execute(comando, (usu, senha))

            resultado = cursor.fetchone()
            if resultado:
                while True:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    largura = os.get_terminal_size().columns
                    print('='*largura)
                    print('                                 ')
                    print('Acesso Concedido✅')
                    print('                                 ')
                    print('='*60)
                    print('Selecione uma Opção'.center(60))
                    print('='*60)
                    print('                                 ')
                    print('--OPÇÕES GESTÃO--')
                    print('1-Consultar Membros da Gestão')
                    print('2-Adicionar Membros da Gestão')
                    print('3-Alterar Dados da Gestão')
                    print('4-Deletar Dados da Gestão')
                    print('                                 ')
                    print('--OPÇÕES ALUNO--')
                    print('5-Consultar Alunos')
                    print('6-Consultar Turma dos Alunos')
                    print('7-Consultar Nota dos Alunos')
                    print('8-Adicionar Aluno')
                    print('9-Alterar Dados dos Alunos')
                    print('10-Deletar Dados dos Alunos')
                    print('                                 ')
                    print('--OPÇÕES DISCIPLINAS/TURMAS--')
                    print('11-Consultar Diciplinas')
                    print('12-Consultar Turmas')
                    print('                                 ')
                    print('--OPÇÕES PROFESSOR--')
                    print('13-Consultar Professores')
                    print('14-Consultar Atribuição de matérias dos professores')
                    print('15-Consultar Turma dos Professores ')
                    print('16-Adicionar Professores')
                    print('17-Atribuir Matérias ao Professor')
                    print('18-Atribuir Turma ao Professor')
                    print('19-Alterar Dados dos Professores')
                    print('20-Deletar Dados dos Professores')
                    print('21-Deletar Matería Atribuida ao Professor')
                    print('22-Deletar Atribuição de Turma do professor')
                    print('                                 ')
                    print('--SAIR--')
                    print('23-Sair para o menu principal')
                    print('                                 ')
                    op= input('Opção: ')
                    if op == '1':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        from tabulate import tabulate
                        largura = os.get_terminal_size().columns
                        print('='*largura)
                        print('                                 ')
                        cursor.execute("SELECT * FROM gestao;")
                        resultados = cursor.fetchall()
                        cabecalhos = ('ID', 'NOME', 'USUÁRIO', 'SENHA', 'EMAIL', 'CARGO', 'STATUS')
                        print('                                 ')
                        print(tabulate(resultados, headers=cabecalhos, tablefmt='grid'))
                        print('                                 ')
                        input('Pressione enter para voltar ao menu de opções...')
                        os.system('cls' if os.name == 'nt' else 'clear')
                    elif op == '2':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        largura = os.get_terminal_size().columns
                        print('='*largura)
                        print('                                 ')
                        print('--Adicionar Membro da Gestão--')
                        print('                                 ')
                        gestao_nome = input('Entre com o Nome do Membro:').strip()
                        gestao_usu = input('Entre com o Usuário do Membro:').strip()
                        gestao_senha = input('Entre com a Senha do Membro:').strip()
                        gestao_email = input('Entre com o Email do Membro:').strip()
                        gestao_cargo = input('Entre com o Cargo do Membro:').strip()
                        gestao_status = input('Entre com o Status do Membro:').strip()
                        if gestao_nome == '' or gestao_usu == '' or gestao_senha == '' or gestao_email == '' or gestao_cargo == '' or gestao_status == '':
                            print('Nenhuma inserção de dados pode ficar vázio')
                            input('Pressione enter para voltar ao menu de opções...')
                            os.system('cls' if os.name == 'nt' else 'clear')
                        else:    
                            comando = 'insert into gestao (gestao_nome, gestao_usu, gestao_senha, gestao_email, gestao_cargo, gestao_status ) values (%s, %s, %s, %s, %s, %s)'
                            valores = (gestao_nome, gestao_usu, gestao_senha, gestao_email, gestao_cargo, gestao_status)
                            cursor.execute(comando, valores)
                            conexao.commit()
                            print('                                 ')
                            print(f'Novo Membro',gestao_nome,'inserido com sucesso!')
                            print('                                 ')
                            input('Pressione enter para voltar ao menu de opções...')
                            os.system('cls' if os.name == 'nt' else 'clear')
                    elif op =='3':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        from tabulate import tabulate
                        largura = os.get_terminal_size().columns
                        print('='*largura)
                        print('                                 ')
                        print ('--Consultar Membro da Gestão--')
                        print('                                 ')
                        cursor.execute("SELECT * FROM gestao;")
                        resultados = cursor.fetchall()
                        cabecalhos = ('ID', 'NOME', 'USUÁRIO', 'SENHA', 'EMAIL', 'CARGO', 'STATUS')
                        print('                                 ')
                        print(tabulate(resultados, headers=cabecalhos, tablefmt='grid'))
                        print('                                 ')
                        gestao_id = input('Digite o ID do membro que vai ser alterada: ')
                        if gestao_id.isdigit():
                            gestao_id = int(gestao_id)
                            cursor.execute('SELECT COUNT(*) FROM gestao WHERE gestao_id = %s',(gestao_id,))
                            existe =cursor.fetchone()[0]
                            if existe > 0:
                                print('                                 ')
                                print('--Selecione qual dado irá sofrer alteração--')
                                print('                                 ')
                                print('1-Nome')
                                print('2-Usuário')
                                print('3-Senha')
                                print('4-Email')
                                print('5-Cargo')
                                print('6-Status')
                                print('                                 ')
                                opc = input('Opção: ')
                                if opc.isdigit():
                                    opc = int(opc)
                                    if opc == 1:
                                        gestao_nome = input('Novo nome: ')
                                        up = 'update gestao set gestao_nome = %s where gestao_id = %s'
                                        valores = (gestao_nome, gestao_id)
                                        cursor.execute(up, valores)
                                        conexao.commit()
                                        print('                                 ')
                                        print(f'Nome do Membro',gestao_nome,'Alterado com sucesso!')
                                        print('                                 ')
                                        input('Pressione enter para voltar ao menu de opções...')
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                    elif opc ==2:
                                        gestao_usu = input('Novo Usuário: ')
                                        up = 'update gestao set gestao_usu = %s where gestao_id = %s'
                                        valores = (gestao_usu, gestao_id)
                                        cursor.execute(up, valores)
                                        conexao.commit()
                                        print('                                 ')
                                        print(f'Usuário do Membro',gestao_usu,'Alterado com sucesso!')
                                        print('                                 ')
                                        input('Pressione enter para voltar ao menu de opções...')
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                    elif opc == 3:
                                        gestao_senha = input('Nova Senha: ')
                                        up = 'update gestao set gestao_senha = %s where gestao_id = %s'
                                        valores = (gestao_senha, gestao_id)
                                        cursor.execute(up, valores)
                                        conexao.commit()
                                        print('                                 ')
                                        print(f'Senha do Membro',gestao_senha,'Alterado com sucesso!')
                                        print('                                 ')
                                        input('Pressione enter para voltar ao menu de opções...')
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                    elif opc == 4:
                                        gestao_email = input('Novo Email: ')
                                        up = 'update gestao set gestao_email = %s where gestao_id = %s'
                                        valores = (gestao_email, gestao_id)
                                        cursor.execute(up, valores)
                                        conexao.commit()
                                        print('                                 ')
                                        print(f'Email do Membro',gestao_email,'Alterado com sucesso!')
                                        print('                                 ')
                                        input('Pressione enter para voltar ao menu de opções...')
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                    elif opc == 5:
                                        gestao_cargo = input('Novo Cargo: ')
                                        up = 'update gestao set gestao_cargo = %s where gestao_id = %s'
                                        valores = (gestao_cargo, gestao_id)
                                        cursor.execute(up, valores)
                                        conexao.commit()
                                        print('                                 ')
                                        print(f'Cargo do Membro',gestao_cargo,'Alterado com sucesso!')
                                        print('                                 ')
                                        input('Pressione enter para voltar ao menu de opções...')
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                    elif opc == 6:
                                        gestao_status = input('Novo Status: ')
                                        up = 'update gestao set gestao_status = %s where gestao_id = %s'
                                        valores = (gestao_status, gestao_id)
                                        cursor.execute(up, valores)
                                        conexao.commit()
                                        print('                                 ')
                                        print(f'Status do Membro',gestao_status,'Alterado com sucesso!')
                                        print('                                 ')
                                        input('Pressione enter para voltar ao menu de opções...')
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                    else:
                                        print('Nenhuma Opção Selecionada')
                                        input('Clique enter para voltar ao menu... ')
                                        os.system('cls' if os.name == 'nt' else 'clear')
                            else:
                                print('                                 ')
                                print('Esse Id não existe')
                                input('Pressione enter para voltar ao menu de opções...')
                                os.system('cls' if os.name == 'nt' else 'clear')
                        else:
                            print('                                 ')
                            print('Caractere invalido ou Nenhuma Opção selecionada')
                            print('                                 ')
                            input('Pressione enter para voltar ao menu de opções...')
                            os.system('cls' if os.name == 'nt' else 'clear')
                    elif op == '4':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        from tabulate import tabulate
                        largura = os.get_terminal_size().columns
                        print('='*largura)
                        print('                                 ')
                        print ('--Consultar Membro da Gestão--')
                        print('                                 ')
                        cursor.execute("SELECT * FROM gestao;")
                        resultados = cursor.fetchall()
                        cabecalhos = ('ID', 'NOME', 'USUÁRIO', 'SENHA', 'EMAIL', 'CARGO', 'STATUS')
                        print('                                 ')
                        print(tabulate(resultados, headers=cabecalhos, tablefmt='grid'))
                        print('                                 ')
                        gestao_id = input('Digite o ID do membro que vai ser deletado: ')
                        if gestao_id.isdigit():
                            gestao_id = int(gestao_id)
                            cursor.execute('SELECT COUNT(*) FROM gestao WHERE gestao_id = %s',(gestao_id,))
                            existe =cursor.fetchone()[0]
                            if existe > 0:
                                dele = 'delete from gestao where gestao_id = %s '
                                valores = (gestao_id,)
                                cursor.execute(dele, valores)
                                conexao.commit()
                                print('Membro Deletado com Sucesso!')
                                print('                                 ')
                            else:
                                print('Esse ID não existe')
                                input('Pressione enter para voltar ao menu de opções...')
                                os.system('cls' if os.name == 'nt' else 'clear')
                        else:
                            print('                                 ')
                            print('Caractere invalido')
                            print('                                 ')
                            input('Pressione enter para voltar ao menu de opções...')
                            os.system('cls' if os.name == 'nt' else 'clear')
                    elif op == '5':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        from tabulate import tabulate
                        largura = os.get_terminal_size().columns
                        print('='*largura)
                        print('                                 ')
                        cursor.execute("SELECT * FROM aluno;")
                        resultados = cursor.fetchall()
                        cabecalhos=('RA', 'NOME', 'USUÁRIO', 'SENHA', 'NASCIMENTO', 'EMAIL', 'TELEFONE', 'STATUS', 'ID TURMA')
                        print('                                 ')
                        print(tabulate(resultados, headers=cabecalhos, tablefmt='grid'))
                        print('                                 ')
                        input('Pressione enter para voltar ao menu de opções...')
                        os.system('cls' if os.name == 'nt' else 'clear')
                    elif op == '6':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        from tabulate import tabulate
                        largura = os.get_terminal_size().columns
                        print('='*largura)
                        print('                                 ')
                        cursor.execute('SELECT aluno_ra, aluno_nome, turma_id, turma_sala, turma_periodo, disciplina_nome from aluno inner join turma on turma_id = turma_iid inner join disciplina on disciplina_iid = disciplina_id')
                        resultados = cursor.fetchall()
                        cabecalhos= ('RA', 'NOME', 'ID TURMA', 'SALA', 'PERÍODO', 'MATÉRIA')
                        print('                                 ')
                        print(tabulate(resultados, headers=cabecalhos, tablefmt='grid'))
                        print('                                 ')
                        input('Pressione enter para voltar ao menu de opções...')
                        os.system('cls' if os.name == 'nt' else 'clear')
                    elif op == '7':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        from tabulate import tabulate
                        largura = os.get_terminal_size().columns
                        print('='*largura)
                        print('                                 ')
                        cursor.execute('select aluno_ra, aluno_nome, nota_valor, nota_frequencia, disciplina_nome from nota left join aluno on nota_rra = aluno_ra left join disciplina on disciplina_iid = disciplina_id')
                        resultados = cursor.fetchall()
                        cabecalhos=('RA ALUNO', 'NOME ALUNO', 'NOTA', 'FREQUÊNCIA', 'DISCIPLINA',)
                        print(tabulate (resultados, headers=cabecalhos, tablefmt='grid'))
                        print('                                 ')
                        input('Pressione enter para voltar ao menu de opções...')
                        os.system('cls' if os.name == 'nt' else 'clear')
                    elif op == '8':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        from tabulate import tabulate
                        largura = os.get_terminal_size().columns
                        print('='*largura)
                        print('                                 ')
                        print('--Adicionar novo aluno--')
                        print('                                 ')
                        aluno_nome = input('Entre com o Nome do Aluno:').strip()
                        aluno_usu = input('Entre com o Usuário do Aluno:').strip()
                        aluno_senha = input('Entre com a Senha do Aluno:').strip()
                        data_nascimento = input('Entre com a Data de Nascimento do Aluno: ').strip()
                        aluno_email = input('Entre com o Email do Aluno:').strip()
                        aluno_telefone = input('Entre com o Telefone do Aluno:').strip()
                        aluno_status = input('Entre com o Status do Aluno:').strip()
                        if aluno_nome == '' or aluno_usu == '' or aluno_senha == '' or data_nascimento == '' or aluno_email == '' or aluno_telefone == '' or aluno_status == '':
                            print('Nenhuma inserção de dados pode ficar vázio')
                            input('Pressione enter para voltar ao menu de opções...')
                            os.system('cls' if os.name == 'nt' else 'clear')
                        else:    
                            cursor.execute("SELECT turma_id, turma_sala, turma_periodo, disciplina_nome from turma inner join disciplina on disciplina_id = disciplina_iid")
                            resultados = cursor.fetchall()
                            cabecalhos=('ID', 'PERÍODO', 'SALA', 'STATUS', 'DISCIPLINA')
                            print('                                 ')
                            print(tabulate(resultados, headers=cabecalhos, tablefmt='grid'))
                            print('                                 ')
                            turma_iid = input('Entre com a turma do aluno: ')
                            if turma_iid.isdigit():
                                turma_iid = int(turma_iid)
                                cursor.execute('SELECT COUNT(*) FROM turma WHERE turma_id = %s',(turma_iid,))
                                existe =cursor.fetchone()[0]
                                if existe > 0:
                                    inse = 'insert into aluno (aluno_nome, aluno_usu, aluno_senha, data_nascimento, aluno_email, aluno_status, turma_iid) values (%s, %s, %s, %s, %s, %s, %s)'
                                    valores = (aluno_nome, aluno_usu, aluno_senha, data_nascimento, aluno_email, aluno_status, turma_iid)
                                    cursor.execute(inse, valores)
                                    conexao.commit()
                                    print('                                 ')
                                    print(f'Novo Aluno',aluno_nome,'inserido com sucesso!')
                                    print('                                 ')
                                    input('Pressione enter para voltar ao menu de opções...')
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                else:
                                    print('Esse ID não existe')
                                    input('Pressione enter para voltar ao menu de opções...')
                                    os.system('cls' if os.name == 'nt' else 'clear')
                            else:
                                print('                                 ')
                                print('Caractere invalido')
                                print('                                 ')
                                input('Pressione enter para voltar ao menu de opções...')
                                os.system('cls' if os.name == 'nt' else 'clear')
                    elif op =='9':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        from tabulate import tabulate
                        largura = os.get_terminal_size().columns
                        print('='*largura)
                        print('                                 ')
                        print ('--Consultar Alunos para alteração--')
                        print('                                 ')
                        cursor.execute("SELECT * FROM aluno;")
                        resultados = cursor.fetchall()
                        cabecalhos=('RA', 'NOME', 'USUÁRIO', 'SENHA', 'DATA DE NASCIMENTO', 'EMAIL', 'TELEFONE', 'STATUS', 'ID DA TURMA')
                        print('                                 ')
                        print(tabulate(resultados, headers=cabecalhos, tablefmt='grid'))
                        print('                                 ')
                        aluno_ra = input('Digite o RA do aluno que vai ser alterada: ')
                        if aluno_ra.isdigit():
                            aluno_ra = int(aluno_ra)
                            cursor.execute('SELECT COUNT(*) FROM aluno WHERE aluno_ra = %s',(aluno_ra,))
                            existe =cursor.fetchone()[0]
                            if existe > 0:
                                print('                                 ')
                                print('--Selecione qual dado irá sofrer alteração--')
                                print('                                 ')
                                print('1-Nome')
                                print('2-Usuário')
                                print('3-Senha')
                                print('4-Data de Nascimento')
                                print('5-Email')
                                print('6-telefone')
                                print('7-Status')
                                print('8-Turma')
                                print('                                 ')
                                opc = input('Opção: ')
                                if opc.isdigit():
                                    opc = int(opc)
                                    if opc == 1:
                                        aluno_nome = input('Novo nome: ')
                                        up = 'update aluno set aluno_nome = %s where aluno_ra = %s'
                                        valores = (aluno_nome, aluno_ra)
                                        cursor.execute(up, valores)
                                        conexao.commit()
                                        print('                                 ')
                                        print(f'Nome do Aluno',aluno_nome,'Alterado com sucesso!')
                                        print('                                 ')
                                        input('Pressione enter para voltar ao menu de opções...')
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                    elif opc ==2:
                                        aluno_usu = input('Novo Usuário: ')
                                        up = 'update aluno set aluno_usu = %s where aluno_ra = %s'
                                        valores = (aluno_usu, aluno_ra)
                                        cursor.execute(up, valores)
                                        conexao.commit()
                                        print('                                 ')
                                        print(f'Usuário do Aluno',aluno_usu,'Alterado com sucesso!')
                                        print('                                 ')
                                        input('Pressione enter para voltar ao menu de opções...')
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                    elif opc == 3:
                                        aluno_senha = input('Nova Senha: ')
                                        up = 'update aluno set aluno_senha = %s where aluno_ra = %s'
                                        valores = (aluno_senha, aluno_ra)
                                        cursor.execute(up, valores)
                                        conexao.commit()
                                        print('                                 ')
                                        print(f'Senha do Aluno',aluno_senha,'Alterada com sucesso!')
                                        print('                                 ')
                                        input('Pressione enter para voltar ao menu de opções...')
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                    elif opc == 4:
                                        data_nascimento = input('Nova Data de Nascimento: ')
                                        up = 'update aluno set data_nascimento = %s where aluno_ra = %s'
                                        valores = (data_nascimento, aluno_ra)
                                        cursor.execute(up, valores)
                                        conexao.commit()
                                        print('                                 ')
                                        print(f'Data de Nascimento do Aluno',data_nascimento,'Alterada com sucesso!')
                                        print('                                 ')
                                        input('Pressione enter para voltar ao menu de opções...')
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                    elif opc == 5:
                                        aluno_email = input('Novo email: ')
                                        up = 'update aluno set aluno_email = %s where aluno_ra = %s'
                                        valores = (aluno_email, aluno_ra)
                                        cursor.execute(up, valores)
                                        conexao.commit()
                                        print('                                 ')
                                        print(f'Email do Aluno',aluno_email,'Alterado com sucesso!')
                                        input('Pressione enter para voltar ao menu de opções...')
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                    elif opc == 6:
                                        aluno_telefone = input('Novo Telefone: ')
                                        up = 'update aluno set aluno_telefone = %s where aluno_ra = %s'
                                        valores = (aluno_telefone, aluno_ra)
                                        cursor.execute(up, valores)
                                        conexao.commit()
                                        print('                                 ')
                                        print(f'Telefone do Aluno',aluno_telefone,'Alterado com sucesso!')
                                        print('                                 ')
                                        input('Pressione enter para voltar ao menu de opções...')
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                    elif opc == 7:
                                        aluno_status = input('Novo Status: ')
                                        up = 'update aluno set aluno_status =%s where aluno_ra = %s'
                                        valores = (aluno_status, aluno_ra)
                                        cursor.execute(up, valores)
                                        conexao.commit()
                                        print('                                 ')
                                        print(f'Status do aluno',aluno_status,'Alterado com sucesso!')
                                        print('                                 ')
                                        input('Pressione enter para voltar ao menu de opções...')
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                    elif opc == 8:
                                        print('--Consultar Turmas--')
                                        print('                                 ')
                                        cursor.execute('select turma_id, turma_sala, turma_periodo, disciplina_nome from turma inner join disciplina on disciplina_iid = disciplina_id')
                                        resultado = cursor.fetchall()
                                        cabecalhos=('ID TURMA', 'SALA', 'TURNO', 'MATÉRIA')
                                        print('                                  ')
                                        print(tabulate(resultado, headers=cabecalhos, tablefmt='grid'))
                                        print('                                  ')
                                        turma_iid = input('ID da nova turma: ')
                                        up = 'update aluno set turma_iid = %s where aluno_ra = %s'
                                        valores = (turma_iid, aluno_ra)
                                        cursor.execute(up, valores)
                                        conexao.commit()
                                        print('                                 ')
                                        print(f'Turma do aluno',turma_iid,'Alterada com sucesso')
                                        print('                                 ')
                                        input('Pressione enter para voltar ao menu de opções...')
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                    else:
                                        print('Caractere invalido ou Nenhuma Opção selecionada')
                                        input('Pressione enter para voltar ao menu de opções...')
                                        os.system('cls' if os.name == 'nt' else 'clear')
                            else:
                                print('Esse RA não existe')
                                input('Pressione enter para voltar ao menu de opções...')
                                os.system('cls' if os.name == 'nt' else 'clear')
                        else:
                            print('Caractere invalido ou Nenhuma Opção selecionada')
                            print('                                 ')
                            input('Pressione enter para voltar ao menu de opções...')
                            os.system('cls' if os.name == 'nt' else 'clear')
                    elif op =='10':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        from tabulate import tabulate
                        largura = os.get_terminal_size().columns
                        print('='*largura)
                        print('                                 ')
                        print ('--Consultar Alunos para Deletar--')
                        print('                                 ')
                        cursor.execute("SELECT * FROM aluno;")
                        resultados = cursor.fetchall()
                        cabecalhos=('RA', 'NOME', 'USUÁRIO', 'SENHA', 'DATA DE NASCIMENTO', 'EMAIL', 'TELEFONE', 'STATUS', 'ID DA TURMA')
                        print('                                 ')
                        print(tabulate(resultados, headers=cabecalhos, tablefmt='grid'))
                        print('                                 ')
                        aluno_ra = input('Digite o RA do Aluno que vai ser deletado: ')
                        if aluno_ra.isdigit():
                            aluno_ra = int(aluno_ra)
                            cursor.execute('SELECT COUNT(*) FROM aluno WHERE aluno_ra = %s',(aluno_ra,))
                            existe =cursor.fetchone()[0]
                            if existe >0:
                                dele = 'delete from aluno where aluno_ra = %s '
                                valores = (aluno_ra,)
                                cursor.execute(dele, valores)
                                conexao.commit()
                                print('Aluno Deletado com Sucesso!')
                                print('                                 ')
                                input('Pressione enter para voltar ao menu de opções...')
                                os.system('cls' if os.name == 'nt' else 'clear')
                            else:
                                print('Esse ID não existe')
                                input('Pressione enter para voltar ao menu de opções...')
                                os.system('cls' if os.name == 'nt' else 'clear')
                        else:
                            print('                                 ')
                            print('Caractere invalido')
                            print('                                 ')
                            input('Pressione enter para voltar ao menu de opções...')
                            os.system('cls' if os.name == 'nt' else 'clear')
                    elif op == '11':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        from tabulate import tabulate
                        largura = os.get_terminal_size().columns
                        print('='*largura)
                        print('                                 ')
                        cursor.execute("SELECT * FROM disciplina;")
                        resultados = cursor.fetchall()
                        cabecalhos=('ID', 'NOME', 'CARGA HORÁRIA')
                        print('                                 ')
                        print(tabulate(resultados, headers=cabecalhos, tablefmt='grid'))
                        print('                                 ')
                        input('Pressione enter para voltar ao menu de opções...')
                        os.system('cls' if os.name == 'nt' else 'clear')
                    elif op == '12':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        from tabulate import tabulate
                        largura = os.get_terminal_size().columns
                        print('='*largura)
                        print('                                 ')
                        cursor.execute("SELECT * FROM turma;")
                        resultados = cursor.fetchall()
                        cabecalhos=('ID', 'PERÍODO', 'SALA', 'STATUS', 'DISCIPLINA ID')
                        print('                                 ')
                        print(tabulate(resultados, headers=cabecalhos, tablefmt='grid'))
                        print('                                 ')
                        input('Pressione enter para voltar ao menu de opções...')
                        os.system('cls' if os.name == 'nt' else 'clear')
                    elif op == '13':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        from tabulate import tabulate
                        largura = os.get_terminal_size().columns
                        print('='*largura)
                        print('                                 ')
                        cursor.execute("SELECT * from professor;")
                        resultados = cursor.fetchall()
                        cabecalhos=('ID', 'NOME', 'USUÁRIO', 'SENHA', 'EMAIL')
                        print('                                 ')
                        print(tabulate(resultados, headers=cabecalhos, tablefmt='grid'))
                        print('                                 ')
                        input('Pressione enter para voltar ao menu de opções...')
                        os.system('cls' if os.name == 'nt' else 'clear')
                    elif op == '14':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        from tabulate import tabulate
                        largura = os.get_terminal_size().columns
                        print('='*largura)
                        print('                                 ')
                        cursor.execute('SELECT professor_nome, atribuicao_nome FROM professor left JOIN professor_atribuicao ON professor_id = professor_iid left JOIN atribuicao ON atribuicao_id = atribuicao_iid')
                        resultados = cursor.fetchall()
                        cabecalhos =('Professor Nome', 'Atribuição de Matéria')
                        print('                                 ')
                        print(tabulate(resultados, headers=cabecalhos, tablefmt='grid'))
                        print('                                 ')
                        input('Pressione enter para voltar ao menu de opções...')
                        os.system('cls' if os.name == 'nt' else 'clear')
                    elif op == '15':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        from tabulate import tabulate
                        largura = os.get_terminal_size().columns
                        print('='*largura)
                        print('                                 ')
                        cursor.execute('SELECT professor_id, professor_nome, turma_id, turma_sala, turma_periodo, disciplina_nome from professor left join professor_turma on professor_id = professor_iid left join turma on turma_id = turma_iid left join disciplina on disciplina_iid = disciplina_id')
                        resultados = cursor.fetchall()
                        cabecalhos= ('RA', 'NOME', 'ID TURMA', 'SALA', 'PERÍODO', 'MATÉRIA')
                        print('                                 ')
                        print(tabulate(resultados, headers=cabecalhos, tablefmt='grid'))
                        print('                                 ')
                        input('Pressione enter para voltar ao menu de opções...')
                        os.system('cls' if os.name == 'nt' else 'clear')
                    elif op == '16':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        largura = os.get_terminal_size().columns
                        print('='*largura)
                        print('                                 ')
                        print('--Adicionar novo professor--')
                        print('                                 ')
                        professor_nome = input('Entre com o Nome do Professor:').strip()
                        professor_usu = input('Entre com o Usuário do Professor:').strip()
                        professor_senha = input('Entre com a Senha do Professor:').strip()
                        professor_email = input('Entre com o Email do Professor:').strip()
                        if professor_nome == '' or professor_usu == '' or professor_senha == '' or professor_email == '' :
                            print('Nenhuma inserção de dados pode ficar vázio')
                            input('Pressione enter para voltar ao menu de opções...')
                            os.system('cls' if os.name == 'nt' else 'clear')
                        else:
                            comando = 'insert into professor (professor_nome, professor_usu, professor_senha, professor_email) values (%s, %s, %s, %s)'
                            valores = (professor_nome, professor_usu, professor_senha, professor_email)
                            cursor.execute(comando, valores)
                            conexao.commit()
                            print('                                 ')
                            print(f'Membro',professor_nome,'inserido com sucesso!')
                            print('                                 ')
                            input('Pressione enter para voltar ao menu de opções...')
                            os.system('cls' if os.name == 'nt' else 'clear')
                    elif op =='17':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        from tabulate import tabulate
                        largura = os.get_terminal_size().columns
                        print('='*largura)
                        print('                                 ')
                        print('--Consultar Professor e Matérias--')
                        print('                                 ')
                        cursor.execute('select professor_id, professor_nome, atribuicao_id, atribuicao_nome from professor left join professor_atribuicao on professor_id = professor_iid left join atribuicao on atribuicao_iid = atribuicao_id')
                        resultado = cursor.fetchall()
                        cabecalhos=('ID PROFESSOR', 'NOME PROFESSOR', 'ID MATÉRIA', 'NOME MATÉRIA')
                        print('                                  ')
                        print(tabulate(resultado, headers=cabecalhos, tablefmt='grid'))
                        print('                                  ')
                        professor_id = input('Digite o ID do professor que vai ser atribuido uma matéria: ')
                        if professor_id.isdigit():
                            professor_id = int(professor_id)
                            cursor.execute('SELECT COUNT(*) FROM professor WHERE professor_id = %s',(professor_id,))
                            existe =cursor.fetchone()[0]
                            if existe >0:
                                print('                                  ')
                                print('--Selecione a Matéria--')
                                print('1-Português')
                                print('2-História')
                                print('3-Matemática')
                                print('4-Literatura')
                                print('5-Física')
                                print('6-Sociologia')
                                print('7-Filosofia')
                                print('8-Geografia')
                                print('9-Biologia')
                                print('10-Química')
                                print('11-Inglês')
                                print('12-Espanhol')
                                print('13-Geopolítica')
                                opc = input('Opção: ')
                                if opc == '1':
                                    up = 'insert ignore into professor_atribuicao (professor_iid, atribuicao_iid) values (%s, %s)'
                                    valores = (professor_id, 1)
                                    cursor.execute(up, valores)
                                    conexao.commit()
                                    if cursor.rowcount > 0:
                                        print('Atribuição concluída: Português')
                                        print('                                  ')
                                        input('Pressione enter para voltar ao menu de opções...')
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                    else:
                                        print('Esse professor já está atribuído a Português')
                                        print('                                  ')
                                        input('Pressione enter para voltar ao menu de opções...')
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                elif opc == '2':
                                    up = 'insert ignore into professor_atribuicao (professor_iid, atribuicao_iid) values (%s, %s)'
                                    valores = (professor_id, 2)
                                    cursor.execute(up, valores)
                                    conexao.commit()
                                    if cursor.rowcount > 0:
                                        print('Atribuição concluída: História')
                                        print('                                  ')
                                        input('Pressione enter para voltar ao menu de opções...')
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                    else:
                                        print('Esse professor já está atribuído a História')
                                        print('                                  ')
                                        input('Pressione enter para voltar ao menu de opções...')
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                elif opc == '3':
                                    up = 'insert ignore into professor_atribuicao (professor_iid, atribuicao_iid) values (%s, %s)'
                                    valores = (professor_id, 3)
                                    cursor.execute(up, valores)
                                    conexao.commit()
                                    if cursor.rowcount > 0:
                                        print('Atribuição concluída: Matemática')
                                        print('                                  ')
                                        input('Pressione enter para voltar ao menu de opções...')
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                    else:
                                        print('Esse professor já está atribuído a Matemática')
                                        print('                                  ')
                                        input('Pressione enter para voltar ao menu de opções...')
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                elif opc == '4':
                                    up = 'insert ignore into professor_atribuicao (professor_iid, atribuicao_iid) values (%s, %s)'
                                    valores = (professor_id, 4)
                                    cursor.execute(up, valores)
                                    conexao.commit()
                                    if cursor.rowcount > 0:
                                        print('Atribuição concluída: Literatura')
                                        print('                                  ')
                                        input('Pressione enter para voltar ao menu de opções...')
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                    else:
                                        print('Esse professor já está atribuído a Literatura')
                                        print('                                  ')
                                        input('Pressione enter para voltar ao menu de opções...')
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                elif opc == '5':
                                    up = 'insert ignore into professor_atribuicao (professor_iid, atribuicao_iid) values (%s, %s)'
                                    valores = (professor_id, 5)
                                    cursor.execute(up, valores)
                                    conexao.commit()
                                    if cursor.rowcount > 0:
                                        print('Atribuição concluída: Física')
                                        print('                                  ')
                                        input('Pressione enter para voltar ao menu de opções...')
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                    else:
                                        print('Esse professor já está atribuído a Física')
                                        print('                                  ')
                                        input('Pressione enter para voltar ao menu de opções...')
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                elif opc == '6':
                                    up = 'insert ignore into professor_atribuicao (professor_iid, atribuicao_iid) values (%s, %s)'
                                    valores = (professor_id, 6)
                                    cursor.execute(up, valores)
                                    conexao.commit()
                                    if cursor.rowcount > 0:
                                        print('Atribuição concluída: Sociologia')
                                        print('                                  ')
                                        input('Pressione enter para voltar ao menu de opções...')
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                    else:
                                        print('Esse professor já está atribuído a Sociologia')
                                        print('                                  ')
                                        input('Pressione enter para voltar ao menu de opções...')
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                elif opc == '7':
                                    up = 'insert ignore into professor_atribuicao (professor_iid, atribuicao_iid) values (%s, %s)'
                                    valores = (professor_id, 7)
                                    cursor.execute(up, valores)
                                    conexao.commit()
                                    if cursor.rowcount > 0:
                                        print('Atribuição concluída: Filosofia')
                                        print('                                  ')
                                        input('Pressione enter para voltar ao menu de opções...')
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                    else:
                                        print('Esse professor já está atribuído a Filosofia')
                                        print('                                  ')
                                        input('Pressione enter para voltar ao menu de opções...')
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                elif opc == '8':
                                    up = 'insert ignore into professor_atribuicao (professor_iid, atribuicao_iid) values (%s, %s)'
                                    valores = (professor_id, 8)
                                    cursor.execute(up, valores)
                                    conexao.commit()
                                    if cursor.rowcount > 0:
                                        print('Atribuição concluída: Geografia')
                                        print('                                  ')
                                        input('Pressione enter para voltar ao menu de opções...')
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                    else:
                                        print('Esse professor já está atribuído a Geografia')
                                        print('                                  ')
                                        input('Pressione enter para voltar ao menu de opções...')
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                elif opc == '9':
                                    up = 'insert ignore into professor_atribuicao (professor_iid, atribuicao_iid) values (%s, %s)'
                                    valores = (professor_id, 9)
                                    cursor.execute(up, valores)
                                    conexao.commit()
                                    if cursor.rowcount > 0:
                                        print('Atribuição concluída: Biologia')
                                        print('                                  ')
                                        input('Pressione enter para voltar ao menu de opções...')
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                    else:
                                        print('Esse professor já está atribuído a Biologia')
                                        print('                                  ')
                                        input('Pressione enter para voltar ao menu de opções...')
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                elif opc == '10':
                                    up = 'insert ignore into professor_atribuicao (professor_iid, atribuicao_iid) values (%s, %s)'
                                    valores = (professor_id, 10)
                                    cursor.execute(up, valores)
                                    conexao.commit()
                                    if cursor.rowcount > 0:
                                        print('Atribuição concluída: Química')
                                        print('                                  ')
                                        input('Pressione enter para voltar ao menu de opções...')
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                    else:
                                        print('Esse professor já está atribuído a Química')
                                        print('                                  ')
                                        input('Pressione enter para voltar ao menu de opções...')
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                elif opc == '11':
                                    up = 'insert ignore into professor_atribuicao (professor_iid, atribuicao_iid) values (%s, %s)'
                                    valores = (professor_id, 11)
                                    cursor.execute(up, valores)
                                    conexao.commit()
                                    if cursor.rowcount > 0:
                                        print('Atribuição concluída: Inglês')
                                        print('                                  ')
                                        input('Pressione enter para voltar ao menu de opções...')
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                    else:
                                        print('Esse professor já está atribuído a Inglês')
                                        print('                                  ')
                                        input('Pressione enter para voltar ao menu de opções...')
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                elif opc == '12':
                                    up = 'insert ignore into professor_atribuicao (professor_iid, atribuicao_iid) values (%s, %s)'
                                    valores = (professor_id, 12)
                                    cursor.execute(up, valores)
                                    conexao.commit()
                                    if cursor.rowcount > 0:
                                        print('Atribuição concluída: Espanhol')
                                        print('                                  ')
                                        input('Pressione enter para voltar ao menu de opções...')
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                    else:
                                        print('Esse professor já está atribuído a Espanhol')
                                        print('                                  ')
                                        input('Pressione enter para voltar ao menu de opções...')
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                elif opc == '13':
                                    up = 'insert ignore into professor_atribuicao (professor_iid, atribuicao_iid) values (%s, %s)'
                                    valores = (professor_id, 13)
                                    cursor.execute(up, valores)
                                    conexao.commit()
                                    if cursor.rowcount > 0:
                                        print('Atribuição concluída: Geopolítica')
                                        print('                                  ')
                                        input('Pressione enter para voltar ao menu de opções...')
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                    else:
                                        print('Esse professor já está atribuído a Geopolítica')
                                        print('                                  ')
                                        input('Pressione enter para voltar ao menu de opções...')
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                else:
                                    print('Nenhuma Opção Selecionada')
                                    input('Clique enter para voltar ao menu... ')
                                    os.system('cls' if os.name == 'nt' else 'clear')
                            else:
                                print('Esse ID não existe')
                                input('Pressione enter para voltar ao menu de opções...')  
                                os.system('cls' if os.name == 'nt' else 'clear')         
                        else:
                            print('Caractere invalido')
                            print('                                 ')
                            input('Pressione enter para voltar ao menu de opções...')
                            os.system('cls' if os.name == 'nt' else 'clear')
                    elif op == '18':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        from tabulate import tabulate
                        largura = os.get_terminal_size().columns
                        print('='*largura)
                        print('                                 ')
                        print('--Consultar Professor e Turmas que já estão Atribuidos--')
                        print('                                 ')
                        cursor.execute('select professor_id, professor_nome, turma_id, turma_sala, turma_periodo, disciplina_nome from professor left join professor_turma on professor_id = professor_iid left join turma on turma_iid = turma_id left join disciplina on disciplina_iid = disciplina_id')
                        resultado = cursor.fetchall()
                        cabecalhos=('ID PROFESSOR', 'NOME PROFESSOR', 'ID TURMA', 'SALA', 'TURNO', 'MATÉRIA')
                        print('                                  ')
                        print(tabulate(resultado, headers=cabecalhos, tablefmt='grid'))
                        print('                                  ')
                        print('--Consultar Professor--')
                        print('                                 ')
                        cursor.execute('select professor_id, professor_nome, atribuicao_nome from professor left join professor_atribuicao on professor_id = professor_iid left join atribuicao on atribuicao_id = atribuicao_iid')
                        resultado = cursor.fetchall()
                        cabecalhos=('ID PROFESSOR', 'NOME PROFESSOR', 'MATÉRIA')
                        print('                                  ')
                        print(tabulate(resultado, headers=cabecalhos, tablefmt='grid'))
                        print('                                  ')
                        print('--Consultar Turmas--')
                        print('                                 ')
                        cursor.execute('select turma_id, turma_sala, turma_periodo, disciplina_nome from turma inner join disciplina on disciplina_iid = disciplina_id')
                        resultado = cursor.fetchall()
                        cabecalhos=('ID TURMA', 'SALA', 'TURNO', 'MATÉRIA')
                        print('                                  ')
                        print(tabulate(resultado, headers=cabecalhos, tablefmt='grid'))
                        print('                                  ')
                        professor_id = input('Digite o ID do professor que vai ser atribuido uma matéria: ')
                        if professor_id.isdigit():
                            professor_id = int(professor_id)
                            cursor.execute('SELECT COUNT(*) FROM professor WHERE professor_id = %s',(professor_id,))
                            existe =cursor.fetchone()[0]
                            if existe >0:
                                print('                                  ')
                                print('--Selecione a Matéria--')
                                print('1-Estudos Avançados de Língua Portuguesa')
                                print('2-Fundamentos de História Geral')
                                print('3-Tópicos de Matemática Aplicada')
                                print('4-Análise Literária e Produção Textual')
                                print('5-Princípios de Física Experimental')
                                print('6-Teorias Sociológicas Contemporâneas')
                                print('7-Introdução ao Pensamento Filosófico')
                                print('8-Estudos Geográficos e Ambientais')
                                print('9-Biologia Geral e Aplicada')
                                print('10-Fundamentos de Química Experimental')
                                print('11-Comunicação e Estruturas da Língua Inglesa')
                                opc = input('Opção: ')
                                if opc.isdigit():
                                    opc = int(opc)
                                    if opc == 1:
                                        up = 'insert ignore into professor_turma (professor_iid, turma_iid) values (%s, %s)'
                                        valores = (professor_id, 1)
                                        cursor.execute(up, valores)
                                        conexao.commit()
                                        if cursor.rowcount > 0:
                                            print('Atribuição concluída: Estudos Avançados de Língua Portuguesa')
                                            print('                                  ')
                                            input('Pressione enter para voltar ao menu de opções...')
                                            os.system('cls' if os.name == 'nt' else 'clear')
                                        else:
                                            print('Esse professor já está atribuído a Estudos Avançados de Língua Portuguesa')
                                            print('                                  ')
                                            input('Pressione enter para voltar ao menu de opções...')
                                            os.system('cls' if os.name == 'nt' else 'clear')
                                    elif opc == 2:
                                        up = 'insert ignore into professor_turma (professor_iid, turma_iid) values (%s, %s)'
                                        valores = (professor_id, 2)
                                        cursor.execute(up, valores)
                                        conexao.commit()
                                        if cursor.rowcount > 0:
                                            print('Atribuição concluída: Fundamentos de História Geral')
                                            print('                                  ')
                                            input('Pressione enter para voltar ao menu de opções...')
                                            os.system('cls' if os.name == 'nt' else 'clear')
                                        else:
                                            print('Esse professor já está atribuído a Fundamentos de História Geral')
                                            print('                                  ')
                                            input('Pressione enter para voltar ao menu de opções...')
                                            os.system('cls' if os.name == 'nt' else 'clear')
                                    elif opc == 3:
                                        up = 'insert ignore into professor_turma (professor_iid, turma_iid) values (%s, %s)'
                                        valores = (professor_id, 3)
                                        cursor.execute(up, valores)
                                        conexao.commit()
                                        if cursor.rowcount > 0:
                                            print('Atribuição concluída: Tópicos de Matemática Aplicada')
                                            print('                                  ')
                                            input('Pressione enter para voltar ao menu de opções...')
                                            os.system('cls' if os.name == 'nt' else 'clear')
                                        else:
                                            print('Esse professor já está atribuído a Tópicos de Matemática Aplicada')
                                            print('                                  ')
                                            input('Pressione enter para voltar ao menu de opções...')
                                            os.system('cls' if os.name == 'nt' else 'clear')
                                    elif opc == 4:
                                        up = 'insert ignore into professor_turma (professor_iid, turma_iid) values (%s, %s)'
                                        valores = (professor_id, 4)
                                        cursor.execute(up, valores)
                                        conexao.commit()
                                        if cursor.rowcount > 0:
                                            print('Atribuição concluída: Análise Literária e Produção Textual')
                                            print('                                  ')
                                            input('Pressione enter para voltar ao menu de opções...')
                                            os.system('cls' if os.name == 'nt' else 'clear')
                                        else:
                                            print('Esse professor já está atribuído a Análise Literária e Produção Textual')
                                            print('                                  ')
                                            input('Pressione enter para voltar ao menu de opções...')
                                            os.system('cls' if os.name == 'nt' else 'clear')
                                    elif opc == 5:
                                        up = 'insert ignore into professor_turma (professor_iid, turma_iid) values (%s, %s)'
                                        valores = (professor_id, 5)
                                        cursor.execute(up, valores)
                                        conexao.commit()
                                        if cursor.rowcount > 0:
                                            print('Atribuição concluída: Princípios de Física Experimental')
                                            print('                                  ')
                                            input('Pressione enter para voltar ao menu de opções...')
                                            os.system('cls' if os.name == 'nt' else 'clear')
                                        else:
                                            print('Esse professor já está atribuído a Princípios de Física Experimental')
                                            print('                                  ')
                                            input('Pressione enter para voltar ao menu de opções...')
                                            os.system('cls' if os.name == 'nt' else 'clear')
                                    elif opc == 6:
                                        up = 'insert ignore into professor_turma (professor_iid, turma_iid) values (%s, %s)'
                                        valores = (professor_id, 6)
                                        cursor.execute(up, valores)
                                        conexao.commit()
                                        if cursor.rowcount > 0:
                                            print('Atribuição concluída: Teorias Sociológicas Contemporâneas')
                                            print('                                  ')
                                            input('Pressione enter para voltar ao menu de opções...')
                                            os.system('cls' if os.name == 'nt' else 'clear')
                                        else:
                                            print('Esse professor já está atribuído a Teorias Sociológicas Contemporâneas')
                                            print('                                  ')
                                            input('Pressione enter para voltar ao menu de opções...')
                                            os.system('cls' if os.name == 'nt' else 'clear')
                                    elif opc == 7:
                                        up = 'insert ignore into professor_turma (professor_iid, turma_iid) values (%s, %s)'
                                        valores = (professor_id, 7)
                                        cursor.execute(up, valores)
                                        conexao.commit()
                                        if cursor.rowcount > 0:
                                            print('Atribuição concluída: Introdução ao Pensamento Filosófico')
                                            print('                                  ')
                                            input('Pressione enter para voltar ao menu de opções...')
                                            os.system('cls' if os.name == 'nt' else 'clear')
                                        else:
                                            print('Esse professor já está atribuído a Introdução ao Pensamento Filosófico')
                                            print('                                  ')
                                            input('Pressione enter para voltar ao menu de opções...')
                                            os.system('cls' if os.name == 'nt' else 'clear')
                                    elif opc == 8:
                                        up = 'insert ignore into professor_turma (professor_iid, turma_iid) values (%s, %s)'
                                        valores = (professor_id, 8)
                                        cursor.execute(up, valores)
                                        conexao.commit()
                                        if cursor.rowcount > 0:
                                            print('Atribuição concluída: Estudos Geográficos e Ambientais')
                                            print('                                  ')
                                            input('Pressione enter para voltar ao menu de opções...')
                                            os.system('cls' if os.name == 'nt' else 'clear')
                                        else:
                                            print('Esse professor já está atribuído a Estudos Geográficos e Ambientais')
                                            print('                                  ')
                                            input('Pressione enter para voltar ao menu de opções...')
                                            os.system('cls' if os.name == 'nt' else 'clear')
                                    elif opc == 9:
                                        up = 'insert ignore into professor_turma (professor_iid, turma_iid) values (%s, %s)'
                                        valores = (professor_id, 9)
                                        cursor.execute(up, valores)
                                        conexao.commit()
                                        if cursor.rowcount > 0:
                                            print('Atribuição concluída: Biologia Geral e Aplicada')
                                            print('                                  ')
                                            input('Pressione enter para voltar ao menu de opções...')
                                            os.system('cls' if os.name == 'nt' else 'clear')
                                        else:
                                            print('Esse professor já está atribuído a Biologia Geral e Aplicada')
                                            print('                                  ')
                                            input('Pressione enter para voltar ao menu de opções...')
                                            os.system('cls' if os.name == 'nt' else 'clear')
                                    elif opc == 10:
                                        up = 'insert ignore into professor_turma (professor_iid, turma_iid) values (%s, %s)'
                                        valores = (professor_id, 10)
                                        cursor.execute(up, valores)
                                        conexao.commit()
                                        if cursor.rowcount > 0:
                                            print('Atribuição concluída: Fundamentos de Química Experimental')
                                            print('                                  ')
                                            input('Pressione enter para voltar ao menu de opções...')
                                            os.system('cls' if os.name == 'nt' else 'clear')
                                        else:
                                            print('Esse professor já está atribuído a Fundamentos de Química Experimental')
                                            print('                                  ')
                                            input('Pressione enter para voltar ao menu de opções...')
                                            os.system('cls' if os.name == 'nt' else 'clear')
                                    elif opc == 11:
                                        up = 'insert ignore into professor_turma (professor_iid, turma_iid) values (%s, %s)'
                                        valores = (professor_id, 11)
                                        cursor.execute(up, valores)
                                        conexao.commit()
                                        if cursor.rowcount > 0:
                                            print('Atribuição concluída: Comunicação e Estruturas da Língua Inglesa')
                                            print('                                  ')
                                            input('Pressione enter para voltar ao menu de opções...')
                                            os.system('cls' if os.name == 'nt' else 'clear')
                                        else:
                                            print('Esse professor já está atribuído a Comunicação e Estruturas da Língua Inglesa')
                                            print('                                  ')
                                            input('Pressione enter para voltar ao menu de opções...')
                                            os.system('cls' if os.name == 'nt' else 'clear')
                            else:
                                print('Esse ID não existe')
                                input('Pressione enter para voltar ao menu de opções...')
                                os.system('cls' if os.name == 'nt' else 'clear')
                        else:
                            print('                                 ')
                            print('Caractere Invalido. Digite apenas numeros')
                            input('Pressione enter para voltar ao menu de opções...')
                            os.system('cls' if os.name == 'nt' else 'clear')               
                    elif op == '19':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        from tabulate import tabulate
                        largura = os.get_terminal_size().columns
                        print('='*largura)
                        print('                                 ')
                        print ('--Consultar Professores para alteração--')
                        print('                                 ')
                        cursor.execute("SELECT * from professor;")
                        resultados = cursor.fetchall()
                        cabecalhos=('ID', 'NOME', 'USUÁRIO', 'SENHA', 'EMAIL')
                        print('                                 ')
                        print(tabulate(resultados, headers=cabecalhos, tablefmt='grid'))
                        print('                                 ')
                        professor_id = input('Digite o ID do professor que vai ser alterada: ')
                        if professor_id.isdigit():
                            professor_id = int(professor_id)
                            cursor.execute('SELECT COUNT(*) FROM professor WHERE professor_id = %s',(professor_id,))
                            existe =cursor.fetchone()[0]
                            if existe >0:
                                print('                                 ')
                                print('--Selecione qual dado irá sofrer alteração--')
                                print('                                 ')
                                print('1-Nome')
                                print('2-Usuário')
                                print('3-Senha')
                                print('4-Email')
                                print('                                 ')
                                opc = input('Opção: ')
                                if opc.isdigit():
                                    opc = int(opc)
                                    if opc == 1:
                                        professor_nome = input('Novo nome: ')
                                        up = 'update professor set professor_nome = %s where professor_id = %s'
                                        valores = (professor_nome, professor_id)
                                        cursor.execute(up, valores)
                                        conexao.commit()
                                        print('                                 ')
                                        print(f'Nome do Professor',professor_nome,'Alterado com sucesso!')
                                        print('                                 ')
                                        input('Pressione enter para voltar ao menu de opções...')
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                    elif opc ==2:
                                        professor_usu = input('Novo Usuário: ')
                                        up = 'update professor set professor_usu = %s where professor_id = %s'
                                        valores = (professor_usu, professor_id)
                                        cursor.execute(up, valores)
                                        conexao.commit()
                                        print('                                 ')
                                        print(f'Usuário do Professor',professor_usu,'Alterado com sucesso!')
                                        print('                                 ')
                                        input('Pressione enter para voltar ao menu de opções...')
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                    elif opc == 3:
                                        professor_senha = input('Nova Senha: ')
                                        up = 'update professor set professor_senha = %s where professor_id = %s'
                                        valores = (professor_senha, professor_id)
                                        cursor.execute(up, valores)
                                        conexao.commit()
                                        print('                                 ')
                                        print(f'Senha do Professor',professor_senha,'Alterada com sucesso!')
                                        print('                                 ')
                                        input('Pressione enter para voltar ao menu de opções...')
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                    elif opc == 4:
                                        professor_email = input('Novo Email: ')
                                        up = 'update professor set professor_email = %s where professor_id = %s'
                                        valores = (professor_email, professor_id)
                                        cursor.execute(up, valores)
                                        conexao.commit()
                                        print('                                 ')
                                        print(f'Email do Professor',professor_email,'Alterado com sucesso!')
                                        print('                                 ')
                                        input('Pressione enter para voltar ao menu de opções...')
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                else:
                                    print('                                 ')
                                    print('Nenhuma Opção selecionada')
                                    print('                                 ')
                                    input('Pressione enter para voltar ao menu de opções...')
                                    os.system('cls' if os.name == 'nt' else 'clear')
                            else:
                                print('Esse ID não existe')
                                input('Pressione enter para voltar ao menu de opções...')
                                os.system('cls' if os.name == 'nt' else 'clear')
                        else:
                            print('                                 ')
                            print('Caractere Invalido. Digite apenas numeros')
                            input('Pressione enter para voltar ao menu de opções...')
                            os.system('cls' if os.name == 'nt' else 'clear')
                    elif op == '20':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        from tabulate import tabulate
                        largura = os.get_terminal_size().columns
                        print('='*largura)
                        print('                                 ')
                        print ('--Consultar Professor--')
                        print('                                 ')
                        cursor.execute('select professor_nome, professor_id from professor;')
                        resultados = cursor.fetchall()
                        cabecalhos=('NOME', 'ID')
                        print('                                 ')
                        print(tabulate(resultados, headers=cabecalhos, tablefmt='grid'))
                        print('                                 ')
                        professor_id = input('Digite o ID do professor que vai ser deletado: ')
                        if professor_id.isdigit():
                            professor_id = int(professor_id)
                            cursor.execute('SELECT COUNT(*) FROM professor WHERE professor_id = %s',(professor_id,))
                            existe =cursor.fetchone()[0]
                            if existe > 0:
                                dele = 'delete from professor where professor_id = %s '
                                valores = (professor_id,)
                                cursor.execute(dele, valores)
                                conexao.commit()
                                print('Professor Deletado com Sucessso!')
                                print('                                 ')
                                input('Pressione enter para voltar ao menu de opções...')
                                os.system('cls' if os.name == 'nt' else 'clear')
                            else:
                                print('Esse ID não existe')
                                input('Pressione enter para voltar ao menu de opções...')
                                os.system('cls' if os.name == 'nt' else 'clear')
                        else:
                            print('                                 ')
                            print('Caractere invalido')
                            print('                                 ')
                            input('Pressione enter para voltar ao menu de opções...')
                            os.system('cls' if os.name == 'nt' else 'clear')
                    elif op =='21':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        from tabulate import tabulate
                        largura = os.get_terminal_size().columns
                        print('='*largura)
                        print('                                 ')
                        print ('--Consultar Atribuição de Matérias dos Professores--')
                        print('                                 ')
                        cursor.execute('select professor_id, professor_nome, atribuicao_id, atribuicao_nome from professor left join professor_atribuicao on professor_id = professor_iid left join atribuicao on atribuicao_iid = atribuicao_id')
                        resultados = cursor.fetchall()
                        cabecalhos=('ID PROFESSOR', 'NOME PROFESSOR', 'ID MATÉRIA', 'NOME MATÉRIA')
                        print('                                 ')
                        print(tabulate(resultados, headers=cabecalhos, tablefmt='grid'))
                        print('                                 ')
                        professor_id = input('Digite o ID do professor que terá a matéria deletada: ')
                        atribuicao_id = input('Digite o ID da matéria que vc quer deletar: ')
                        if professor_id.isdigit() and atribuicao_id.isdigit():
                            professor_id = int(professor_id)
                            atribuicao_id = int(atribuicao_id)
                            cursor.execute('SELECT COUNT(*) FROM professor WHERE professor_id = %s',(professor_id,))
                            existe_professor = cursor.fetchone()[0]
                            cursor.execute('SELECT COUNT(*) FROM atribuicao WHERE atribuicao_id = %s',(atribuicao_id,))
                            existe_atribuicao = cursor.fetchone()[0]
                            cursor.execute('SELECT COUNT(*) FROM professor_atribuicao WHERE professor_iid = %s and atribuicao_iid = %s',(professor_id,atribuicao_id,))
                            existe_relacao = cursor.fetchone()[0]
                            if existe_professor >0 and existe_atribuicao >0 and existe_relacao >0:
                                dele = 'delete from professor_atribuicao where professor_iid = %s and atribuicao_iid = %s'
                                valores = (professor_id, atribuicao_id,)
                                cursor.execute(dele, valores)
                                conexao.commit()
                                print('Atribuição Deletada com Sucessso!')
                                print('                                 ')
                                input('Pressione enter para voltar ao menu de opções...')
                                os.system('cls' if os.name == 'nt' else 'clear')
                            else:
                                print('Professor, Matéria ou Relação não existe')
                                input('Pressione enter para voltar ao menu de opções...')
                                os.system('cls' if os.name == 'nt' else 'clear')
                        else:
                            print('                                 ')
                            print('Caractere invalido')
                            print('                                 ')
                            input('Pressione enter para voltar ao menu de opções...')
                            os.system('cls' if os.name == 'nt' else 'clear')
                    elif op == '22':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        from tabulate import tabulate
                        largura = os.get_terminal_size().columns
                        print('='*largura)
                        print('                                 ')
                        print ('--Consultar Atribuição de Turma dos Professores--')
                        print('                                 ')
                        cursor.execute('select professor_id, professor_nome, turma_id, turma_sala, disciplina_nome from professor left join professor_turma on professor_id = professor_iid left join turma on turma_iid = turma_id left join disciplina on disciplina_iid = disciplina_id ')
                        resultados = cursor.fetchall()
                        cabecalhos=('ID PROFESSOR', 'NOME PROFESSOR', 'ID TURMA', 'TURMA SALA', 'MATÉRIA')
                        print('                                 ')
                        print(tabulate(resultados, headers=cabecalhos, tablefmt='grid'))
                        print('                                 ')
                        professor_id = input('Digite o ID do Professor que terá a atribuição deletada: ')
                        turma_id = input('Digite o ID da Turma que vc quer deletar: ')
                        if professor_id.isdigit() and turma_id.isdigit():
                            professor_id = int(professor_id)
                            turma_id = int(turma_id)
                            cursor.execute('SELECT COUNT(*) FROM professor WHERE professor_id = %s',(professor_id,))
                            existe_professor = cursor.fetchone()[0]
                            cursor.execute('SELECT COUNT(*) FROM turma WHERE turma_id = %s',(turma_id,))
                            existe_turma = cursor.fetchone()[0]
                            cursor.execute('SELECT COUNT(*) FROM professor_turma WHERE professor_iid = %s and turma_iid = %s',(professor_id,turma_id,))
                            existe_relacao = cursor.fetchone()[0]
                            if existe_professor >0 and existe_turma >0 and existe_relacao >0:
                                dele = 'delete from professor_turma where professor_iid = %s and turma_iid = %s'
                                valores = (professor_id, turma_id,)
                                cursor.execute(dele, valores)
                                conexao.commit()
                                print('Atribuição de Turma Deletada com Sucessso!')
                                print('                                 ')
                                input('Pressione enter para voltar ao menu de opções...')
                                os.system('cls' if os.name == 'nt' else 'clear')
                            else:
                                print('Professor, Turma ou Relação não existe')
                                input('Pressione enter para voltar ao menu de opções...')
                                os.system('cls' if os.name == 'nt' else 'clear')
                        else:
                            print('                                 ')
                            print('Caractere invalido')
                            print('                                 ')
                            input('Pressione enter para voltar ao menu de opções...')
                            os.system('cls' if os.name == 'nt' else 'clear')
                    elif op == '23':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        largura = os.get_terminal_size().columns
                        print('='*largura)
                        print('                                 ')
                        input('Clique enter para voltar ao menu...')
                        os.system('cls' if os.name == 'nt' else 'clear')
                        break
                    else:
                        largura = os.get_terminal_size().columns
                        print('='*largura)
                        print('                                 ')
                        print('Nenhuma Opção Selecionada')
                        input('Clique enter para voltar ao menu... ')
                        os.system('cls' if os.name == 'nt' else 'clear')
            else:
                largura = os.get_terminal_size().columns
                print('='*largura)
                print('                                 ')
                print('Acesso Negado')
                input('Pressione enter para voltar ao menu...')
                os.system('cls' if os.name == 'nt' else 'clear')
    elif opcao == '2':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('='*60)
        print('--Sistema do Professor--'.center(60))
        print('='*60)
        print('                                 ')
        professor_usu= input('👤 Digite seu Usuário: ').strip()
        professor_senha=getpass.getpass('🔒 Digite sua senha: ').strip()

        comando= 'select * from professor where professor_usu = %s and professor_senha = %s'
        if professor_usu == '' or professor_senha == '':
            print('Nenhuma inserção de dados pode ficar vázio')
            input('Pressione enter para voltar ao menu de opções...')
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            cursor.execute(comando, (professor_usu, professor_senha))

            resultado = cursor.fetchone()

            if resultado:
                    while True:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        largura = os.get_terminal_size().columns
                        print('='*largura)
                        print('                                 ')
                        print('Acesso Concedido✅')
                        print('                                 ')
                        print('='*60)
                        print('--Selecione uma Opção--')
                        print('='*60)
                        print('                                 ')
                        print('1-Consultar Minha Turma')
                        print('2-Consultar Minha Disciplina')
                        print('3-Consultar Alunos da Minha Turma')
                        print('4-Consultar Nota dos Alunos')
                        print('5-Adiconar Nota')
                        print('6-Sair')
                        print('                                 ')
                        op = input('Opção: ')
                        if op == '1':
                            os.system('cls' if os.name == 'nt' else 'clear')
                            from tabulate import tabulate
                            largura = os.get_terminal_size().columns
                            print('='*largura)
                            print('                                 ')
                            cursor.execute('select professor_id, professor_nome, turma_iid, turma_periodo, turma_sala, disciplina_nome from professor left join professor_turma on professor_id = professor_iid left join turma on turma_iid = turma_id left join disciplina on disciplina_iid = disciplina_id where professor_usu = %s',(professor_usu,))
                            resultados = cursor.fetchall()
                            cabecalhos = ('ID PROFESSOR', 'NOME', 'ID DA TURMA', 'PERIODO', 'SALA', 'MATÉRIA')
                            print(tabulate (resultados, headers=cabecalhos, tablefmt='grid'))
                            print('                                 ')
                            input('Pressione enter para voltar ao menu de opções...')
                            os.system('cls' if os.name == 'nt' else 'clear')
                        elif op == '2':
                            os.system('cls' if os.name == 'nt' else 'clear')
                            from tabulate import tabulate
                            largura = os.get_terminal_size().columns
                            print('='*largura)
                            print('                                 ')
                            cursor.execute('select professor_nome, atribuicao_nome from professor left join professor_atribuicao on professor_iid = professor_id left join atribuicao on atribuicao_iid = atribuicao_id where professor_usu = %s',(professor_usu,))
                            resultados = cursor.fetchall()
                            cabecalhos=('NOME','DISCIPLINA',)
                            print(tabulate (resultados, headers=cabecalhos, tablefmt='grid'))
                            print('                                 ')
                            input('Pressione enter para voltar ao menu de opções...')
                            os.system('cls' if os.name == 'nt' else 'clear')
                        elif op == '3':
                            os.system('cls' if os.name == 'nt' else 'clear')
                            from tabulate import tabulate
                            largura = os.get_terminal_size().columns
                            print('='*largura)
                            print('                                 ')
                            cursor.execute('select aluno_ra, aluno_nome, turma_id, turma_sala, turma_periodo, disciplina_nome from professor inner join professor_turma on professor.professor_id = professor_turma.professor_iid inner join turma on professor_turma.turma_iid = turma.turma_id inner join aluno on aluno.turma_iid = turma.turma_id inner join disciplina on turma.disciplina_iid = disciplina.disciplina_id where professor_usu = %s',(professor_usu,))
                            resultados = cursor.fetchall()
                            cabecalhos=('RA ALUNO','NOME ALUNO','ID SALA','SALA','TURNO','DISCIPLINA',)
                            print(tabulate (resultados, headers=cabecalhos, tablefmt='grid'))
                            print('                                 ')
                            input('Pressione enter para voltar ao menu de opções...')
                            os.system('cls' if os.name == 'nt' else 'clear')
                        elif op =='4':
                            os.system('cls' if os.name == 'nt' else 'clear')
                            from tabulate import tabulate
                            largura = os.get_terminal_size().columns
                            print('='*largura)
                            print('                                 ')
                            print('--Consulta da Nota dos alunos--')
                            print('')
                            cursor.execute('select aluno_ra, aluno_nome, nota_valor, nota_frequencia from professor left join professor_turma on professor.professor_id = professor_turma.professor_iid left join turma on professor_turma.turma_iid = turma.turma_id left join aluno on aluno.turma_iid = turma.turma_id left join nota on nota_rra = aluno_ra where professor_usu = %s',(professor_usu,))
                            cabecalhos=('RA ALUNO','NOME ALUNO','NOTA','FREQUÊNCIA',)
                            resultados = cursor.fetchall()
                            print(tabulate (resultados, headers=cabecalhos, tablefmt='grid'))
                            print('                                 ')
                            input('Pressione enter para voltar ao menu de opções...')
                            os.system('cls' if os.name == 'nt' else 'clear')
                        elif op =='5':
                            os.system('cls' if os.name == 'nt' else 'clear')
                            from tabulate import tabulate
                            largura = os.get_terminal_size().columns
                            print('='*largura)
                            print('                                 ')
                            print('--Consulta dos alunos--')
                            print('')
                            cursor.execute('select aluno_ra, aluno_nome from professor left join professor_turma on professor.professor_id = professor_turma.professor_iid left join turma on professor_turma.turma_iid = turma.turma_id left join aluno on aluno.turma_iid = turma.turma_id where professor_usu = %s',(professor_usu,))
                            resultados = cursor.fetchall()
                            cabecalhos=('RA ALUNO','NOME ALUNO',)
                            print(tabulate (resultados, headers=cabecalhos, tablefmt='grid'))
                            print('                                 ')
                            nota_rra = input('Digite o RA do aluno que vai ser Adcionada/Alterada a nota e sua Frequência: ')
                            if nota_rra.isdigit():
                                nota_rra = int(nota_rra)
                                cursor.execute('select 1 from aluno inner join turma on aluno.turma_iid = turma.turma_id inner join professor_turma on turma.turma_id = professor_turma.turma_iid where professor_turma.professor_iid = (select professor_id from professor where professor_usu = %s) and aluno_ra = %s',(professor_usu, nota_rra))
                                permitido = cursor.fetchone()
                                if not permitido:
                                    print("Acesso negado: aluno não pertence à sua turma")
                                    input('Pressione enter para voltar ao menu de opções...')
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                else:
                                    cursor.execute('SELECT COUNT(*) FROM nota WHERE nota_rra = %s',(nota_rra,))
                                    existe = cursor.fetchone()[0]
                                    if existe >0:
                                        print('                                 ')
                                        nota1 = input("Digite a primeira nota: ")
                                        nota2 = input("Digite a segunda nota: ")
                                        nota3 = input("Digite a terceira nota: ")
                                        nota4 = input("Digite a quarta nota: ")
                                        frequencia = input("Digite sua frequência (0 a 100): ")
                                        if nota1 == '' or nota2 == '' or nota3 == '' or nota4 == '' or frequencia == '':
                                            print('Nenhuma inserção de dados pode ficar vázio')
                                            input('Pressione enter para voltar ao menu de opções...')
                                        elif not nota1.replace('.','',1).isdigit() or not nota2.replace('.','',1).isdigit() or not nota3.replace('.','',1).isdigit() or not nota4.replace('.','',1).isdigit() or not frequencia.isdigit() :
                                            print('As Notas devem conter apenas números (1 a 10)')
                                            input('Pressione enter para voltar ao menu...')
                                            os.system('cls' if os.name == 'nt' else 'clear')
                                        else:
                                            nota1 = float(nota1) 
                                            nota2 = float(nota2)
                                            nota3 = float(nota3)
                                            nota4 = float(nota4)
                                            frequencia = int(frequencia)
                                            if 0<= nota1 <=10 and 0<= nota2 <=10 and 0<= nota3 <=10 and 0<= nota4 <=10 and 0<= frequencia <=100:
                                                media = (nota1 + nota2 + nota3 + nota4) / 4
                                                print('                                 ')
                                                print (f"A média final é:", media)
                                                print('                                 ')
                                                print('Coloque a Média para alterar a nota ')
                                                nota_valor= input('Nota: ')
                                                if nota_valor == '':
                                                    print('Nenhuma inserção de dados pode ficar vázio')
                                                    input('Pressione enter para voltar ao menu de opções...')
                                                    os.system('cls' if os.name == 'nt' else 'clear')
                                                elif not nota_valor.replace('.','',1).isdigit():
                                                    print('A Nota deve conter apenas números (1 a 10)')
                                                    input('Pressione enter para voltar ao menu...')
                                                    os.system('cls' if os.name == 'nt' else 'clear')
                                                else:
                                                    nota_valor = float(nota_valor)
                                                    if 0<= nota_valor <=10:
                                                        up = 'update nota set nota_valor = %s  where nota_rra = %s'
                                                        valores = (nota_valor, nota_rra)
                                                        cursor.execute(up, valores)
                                                        conexao.commit()
                                                        print('                                 ')
                                                        print(f'Nota do Aluno',nota_valor,'Alterado/Adicionada com sucesso!')
                                                        print('                                 ')
                                                        print('Coloque o valor da frequência para: ')
                                                        nota_frequencia= input('Valor: ')
                                                        up = 'update nota set nota_frequencia = %s  where nota_rra = %s'
                                                        valores = (nota_frequencia, nota_rra)
                                                        cursor.execute(up, valores)
                                                        conexao.commit()
                                                        print(f'Frequência',nota_frequencia,'Alterado/Adicionada com sucesso!')
                                                        print('                                 ')
                                                        input('Pressione enter para voltar ao menu de opções...')
                                                        os.system('cls' if os.name == 'nt' else 'clear')
                                                    else:
                                                        print('Nota deve estar entre 0 e 10')
                                                        input('Pressione enter para voltar ao menu de opções...')
                                                        os.system('cls' if os.name == 'nt' else 'clear')
                                            else:
                                                print('Nota deve estar entre 0 e 10')
                                                print('Frequência deve estar entre 0 a 100')
                                                input('Pressione enter para voltar ao menu de opções...')
                                                os.system('cls' if os.name == 'nt' else 'clear')
                                    else:
                                        print('Esse ID não existe')
                                        input('Pressione enter para voltar ao menu de opções...')
                                        os.system('cls' if os.name == 'nt' else 'clear')
                            else:
                                print('                                 ')
                                print('Caractere Invalido. Digite apenas numeros')
                                input('Pressione enter para voltar ao menu de opções...')
                                os.system('cls' if os.name == 'nt' else 'clear')
                        elif op == '6':
                            os.system('cls' if os.name == 'nt' else 'clear')
                            largura = os.get_terminal_size().columns
                            print('='*largura)
                            print('                                 ')
                            input('Clique enter para voltar ao menu...')
                            os.system('cls' if os.name == 'nt' else 'clear')
                            break
                        else:
                            largura = os.get_terminal_size().columns
                            print('='*largura)
                            print('                                 ')
                            print('Nenhuma Opção Selecionada')
                            input('Clique enter para voltar ao menu... ')
                            os.system('cls' if os.name == 'nt' else 'clear')
            else:
                largura = os.get_terminal_size().columns
                print('='*largura)
                print('                                 ')
                print('Acesso Negado')
                input('Pressione enter para voltar ao menu...')
                os.system('cls' if os.name == 'nt' else 'clear')

    elif opcao =='3':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('='*60)
        print('--Sistema do Aluno--'.center(60))
        print('='*60)
        aluno_ra= input('👤 Digite seu RA: ').strip()
        aluno_senha=getpass.getpass('🔒 Digite sua senha: ').strip()

        comando= 'select * from aluno where aluno_ra = %s and aluno_senha = %s'
        if aluno_ra == '' or aluno_senha == '':
            print('Nenhuma inserção de dados pode ficar vázio')
            input('Pressione enter para voltar ao menu de opções...')
            os.system('cls' if os.name == 'nt' else 'clear')
        elif not aluno_ra.isdigit():
            print('O RA deve conter apenas números')
            input('Pressione enter para voltar ao menu...')
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            aluno_ra = int(aluno_ra)
            cursor.execute(comando, (aluno_ra, aluno_senha))
            resultado = cursor.fetchone()
            if resultado:
                while True:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    largura = os.get_terminal_size().columns
                    print('='*largura)
                    print('                                 ')
                    print('Acesso Concedido✅')
                    print('                                 ')
                    print('='*60)
                    print('--Selecione uma Opção--'.center(60))
                    print('='*60)
                    print('                                 ')
                    print('1-Consultar Minha Turma')
                    print('2-Consultar Minha Disciplina')
                    print('3-Consultar Minha Nota')
                    print('4-Sair')
                    print('                                 ')
                    op = input('Opção: ')
                    if op == '1':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        from tabulate import tabulate
                        largura = os.get_terminal_size().columns
                        print('='*largura)
                        print('                                 ')
                        cursor.execute('select aluno_ra, aluno_nome, turma_iid, turma_periodo, turma_sala from aluno inner join turma on turma_iid = turma_id where aluno_ra = %s',(aluno_ra,))
                        resultados = cursor.fetchall()
                        cabecalhos = ('ALUNO RA', 'NOME', 'ID DA TURMA', 'PERIODO', 'SALA')
                        print(tabulate (resultados, headers=cabecalhos, tablefmt='grid'))
                        print('                                 ')
                        input('Pressione enter para voltar ao menu de opções...')
                        os.system('cls' if os.name == 'nt' else 'clear')
                    elif op == '2':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        from tabulate import tabulate
                        largura = os.get_terminal_size().columns
                        print('='*largura)
                        print('                                 ')
                        cursor.execute('select disciplina_nome from turma left join disciplina on disciplina_iid = disciplina_id left join aluno on turma_iid = turma_id where aluno_ra = %s',(aluno_ra,))
                        resultados = cursor.fetchall()
                        cabecalhos=('DISCIPLINA',)
                        print(tabulate (resultados, headers=cabecalhos, tablefmt='grid'))
                        print('                                 ')
                        input('Pressione enter para voltar ao menu de opções...')
                        os.system('cls' if os.name == 'nt' else 'clear')
                    elif op == '3':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        from tabulate import tabulate
                        largura = os.get_terminal_size().columns
                        print('='*largura)
                        print('                                 ')
                        cursor.execute('select aluno_ra, aluno_nome, nota_valor, nota_frequencia, disciplina_nome from nota left join aluno on nota_rra = aluno_ra left join disciplina on disciplina_iid = disciplina_id where aluno_ra = %s',(aluno_ra,))
                        resultados = cursor.fetchall()
                        cabecalhos=('RA ALUNO', 'NOME ALUNO', 'NOTA', 'FREQUÊNCIA', 'DISCIPLINA',)
                        print(tabulate (resultados, headers=cabecalhos, tablefmt='grid'))
                        print('                                 ')
                        input('Pressione enter para voltar ao menu de opções...')
                        os.system('cls' if os.name == 'nt' else 'clear')
                    elif op == '4':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        largura = os.get_terminal_size().columns
                        print('='*largura)
                        print('                                 ')
                        input('Clique enter para voltar ao menu...')
                        os.system('cls' if os.name == 'nt' else 'clear')
                        break
                    else:
                        largura = os.get_terminal_size().columns
                        print('='*largura)
                        print('                                 ')
                        print('Nenhuma Opção Selecionada')
                        input('Clique enter para voltar ao menu... ')
                        os.system('cls' if os.name == 'nt' else 'clear')
            else:
                largura = os.get_terminal_size().columns
                print('='*largura)
                print('                                 ')
                print('Acesso Negado')
                input('Pressione enter para voltar ao menu...')
                os.system('cls' if os.name == 'nt' else 'clear')
    elif opcao == '4':
        os.system('cls' if os.name == 'nt' else 'clear')
        largura = os.get_terminal_size().columns
        print('='*largura)
        print('                                 ')
        input('Clique enter para encerrar...')
        os.system('cls' if os.name == 'nt' else 'clear')
        break
    else:
        largura = os.get_terminal_size().columns
        print('='*largura)
        print('                                 ')
        print('Opção Invalida')
        input('Clique enter para voltar ao menu...')
        os.system('cls' if os.name == 'nt' else 'clear')

cursor.close()
conexao.close()