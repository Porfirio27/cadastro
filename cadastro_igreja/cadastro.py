from PyQt5 import uic,QtWidgets
import mysql.connector
from reportlab.pdfgen import canvas
import sqlite3

numero_id = 0

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="igreja_ad"
)
       
def editar_dados():
    global numero_id

    linha = segunda_tela.tableWidget.currentRow()
    
    cursor = banco.cursor()
    cursor.execute("SELECT id FROM cadastro_ad")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("SELECT * FROM cadastro_ad WHERE id="+ str(valor_id))
    membro = cursor.fetchall()
    menu_editar.show()
    
    menu_editar.lineEdit.setText(str(membro[0][0]))
    menu_editar.lineEdit_2.setText(str(membro[0][1]))
    menu_editar.lineEdit_3.setText(str(membro[0][2]))
    menu_editar.lineEdit_4.setText(str(membro[0][3]))
    menu_editar.lineEdit_5.setText(str(membro[0][4]))
    menu_editar.lineEdit_6.setText(str(membro[0][5]))
    menu_editar.lineEdit_7.setText(str(membro[0][6]))
    menu_editar.lineEdit_8.setText(str(membro[0][7]))
    menu_editar.lineEdit_9.setText(str(membro[0][8]))
    menu_editar.lineEdit_10.setText(str(membro[0][9]))
    numero_id = valor_id


def salvar_valor_editado():
    global numero_id

    # ler dados do lineEdit
    matricula = menu_editar.lineEdit_2.text()
    nome = menu_editar.lineEdit_3.text()
    nascimento = menu_editar.lineEdit_4.text()
    batismo = menu_editar.lineEdit_5.text()
    cpf = menu_editar.lineEdit_6.text()
    endereço = menu_editar.lineEdit_7.text()
    telefone = menu_editar.lineEdit_8.text()
    email = menu_editar.lineEdit_9.text()
    departamento = menu_editar.lineEdit_10.text()
    # atualizar os dados no banco
    cursor = banco.cursor()
    cursor.execute("UPDATE cadastro_ad SET matricula = '{}', nome = '{}', nascimento ='{}', batismo = '{}', cpf = '{}', endereço ='{}', telefone = '{}', email ='{}', departamento = '{}'  WHERE id = {}".format(matricula,nome,nascimento,batismo,cpf,endereço,telefone,email,departamento,numero_id))
    banco.commit()
    #atualizar as janelas
    menu_editar.close()
    segunda_tela.close()
    tela_dados()
    



def excluir_dados():
    linha = segunda_tela.tableWidget.currentRow()
    segunda_tela.tableWidget.removeRow(linha)

    cursor = banco.cursor()
    cursor.execute("SELECT id FROM cadastro_ad")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("DELETE FROM cadastro_ad WHERE id="+ str(valor_id))


def gerar_pdf():
     cursor = banco.cursor()
     comando_SQL = "SELECT * FROM cadastro_ad"
     cursor.execute(comando_SQL)
     dados_lidos = cursor.fetchall()
     y = 0
     pdf = canvas.Canvas("cadastro_Membros.pdf")
     pdf.setFont("Times-Bold", 25)
     pdf.drawString(200,800, "Membros Cadastrados:")
     pdf.setFont("Times-Bold", 18)

     pdf.drawString(10,750, "ID")
     pdf.drawString(110,750, "MATRICULA")
     pdf.drawString(210,750, "NOME")
     pdf.drawString(310,750, "NASCIMENTO")
     pdf.drawString(410,750, "BATISMO")
     pdf.drawString(510,750, "CPF")
     pdf.drawString(610,750, "ENDEREÇO")
     pdf.drawString(710,750, "TELEFONE")
     pdf.drawString(810,750, "EMAIL")
     pdf.drawString(910,750, "DEPARTAMENTO")

     for i in range(0, len(dados_lidos)):
          y = y + 50
          pdf.drawString(10,750 - y, str(dados_lidos[i][0]))
          pdf.drawString(110,750 - y, str(dados_lidos[i][1]))
          pdf.drawString(210,750 - y, str(dados_lidos[i][2]))
          pdf.drawString(310,750 - y, str(dados_lidos[i][3]))
          pdf.drawString(410,750 - y, str(dados_lidos[i][4]))
          pdf.drawString(510,750 - y, str(dados_lidos[i][5]))
          pdf.drawString(610,750 - y, str(dados_lidos[i][6]))
          pdf.drawString(710,750 - y, str(dados_lidos[i][7]))
          pdf.drawString(810,750 - y, str(dados_lidos[i][8]))
          pdf.drawString(910,750 - y, str(dados_lidos[i][9]))
     
     pdf.save()
     print("PDF FOI GERADO COM SUCESSO!!!")
    

def funcao_principal():
    linha1 = cadastro_membros.lineEdit_1.text()
    linha2 = cadastro_membros.lineEdit_2.text()
    linha3 = cadastro_membros.lineEdit_3.text()
    linha4 = cadastro_membros.lineEdit_4.text()
    linha5 = cadastro_membros.lineEdit_5.text()
    linha6 = cadastro_membros.lineEdit_6.text()
    linha7 = cadastro_membros.lineEdit_7.text()
    linha8 = cadastro_membros.lineEdit.text()
    
    departamento = ""

    if cadastro_membros.radioButton_1.isChecked() :
         print("Criança Foi Selecionada")
         departamento = "Criança"
    elif cadastro_membros.radioButton_2.isChecked() :
          print("Adolescente Foi Selecionada")
          departamento = "Adolescente"
    elif cadastro_membros.radioButton_3.isChecked() :
          print("Jovem Foi selecionado")
          departamento = "Jovem"
    elif cadastro_membros.radioButton_4.isChecked() :
          print("Irmã Foi Selecionado")
          departamento = "Irmã" 
    else  :
          print("Varão Foi Selecionado")
          departamento = "Varão"

   
    print("Nome", linha1)
    print("Endereço", linha2)
    print("Email", linha3)
    print("Telefone", linha4)
    print("Batismo", linha5)
    print("CPF", linha6)
    print("Nascimento", linha7)
    print("Matricula", linha8)
    

    cursor = banco.cursor()
    comando_SQL = "INSERT INTO cadastro_ad (Nome, Endereço, Email, Telefone, Batismo, CPF, Nascimento, Matricula, departamento) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    dados = (str(linha1),str(linha2),str(linha3),str(linha4),str(linha5),str(linha6),str(linha7),str(linha8),departamento)
    cursor.execute(comando_SQL,dados)
    banco.commit()
    cadastro_membros.lineEdit_1.setText("")
    cadastro_membros.lineEdit_2.setText("")
    cadastro_membros.lineEdit_3.setText("")
    cadastro_membros.lineEdit_4.setText("")
    cadastro_membros.lineEdit_5.setText("")
    cadastro_membros.lineEdit_6.setText("")
    cadastro_membros.lineEdit_7.setText("")
    cadastro_membros.lineEdit.setText("")


def chama_segunda_tela():
    tela.label_4.setText("")
    nome_usuario = tela.lineEdit.text()
    senha = tela.lineEdit_2.text()
    
    if nome_usuario ==  "vinicius12" or "mariana" and senha == "1202" or "2709":
        tela.close()
        cadastro_membros.show()
   
    else:
        tela.label_5.setText(" Dados de login incorretos! ") 

def tela_dados():
    segunda_tela.show()

    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM cadastro_ad"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()

    segunda_tela.tableWidget.setRowCount(len(dados_lidos))
    segunda_tela.tableWidget.setColumnCount(10)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 10):
           segunda_tela.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j]))) 

def tela_login():
    tela_cadastro.show()

def cadastrar():
    nome = tela_cadastro.lineEdit.text()
    login = tela_cadastro.lineEdit_2.text()
    senha = tela_cadastro.lineEdit_3.text()
    c_senha = tela_cadastro.lineEdit_4.text()

    if (senha == c_senha):
        try:
            cursor = banco.cursor()
            cursor.execute("INSERT INTO login_ad VALUES ('"+nome+"','"+login+"','"+senha+"')")
            
            banco.commit() 
            banco.close()
            tela_cadastro.label.setText("Usuario cadastrado com sucesso")

        except :
            print("Erro ao inserir os dados: ")
    else:
        tela_cadastro.label.setText("As senhas digitadas estão diferentes")


app=QtWidgets.QApplication([])
tela=uic.loadUi("tela_login.ui")
cadastro_membros=uic.loadUi("cadastro_membros.ui")
segunda_tela=uic.loadUi("listar_dados.ui")
tela_cadastro=uic.loadUi("cadastro_usuario.ui")
menu_editar=uic.loadUi("tela_editor.ui")
tela.pushButton.clicked.connect(chama_segunda_tela)
tela.pushButton_2.clicked.connect(tela_login)
cadastro_membros.pushButton.clicked.connect(funcao_principal)
cadastro_membros.pushButton_2.clicked.connect(tela_dados)
segunda_tela.pushButton_2.clicked.connect(gerar_pdf)
segunda_tela.pushButton_3.clicked.connect(excluir_dados)
segunda_tela.pushButton.clicked.connect(editar_dados)
menu_editar.pushButton.clicked.connect(salvar_valor_editado)
tela_cadastro.pushButton.clicked.connect(cadastrar)

tela.show()
app.exec()