from PyQt5 import QtWidgets, uic
import sqlite3


def salvar_bd():
    nome = tela1.lineEdit.text()
    codigo = tela1.lineEdit_2.text()
    preco = tela1.lineEdit_3.text()
    quantidade = tela1.lineEdit_4.text()

    if tela1.radioButton.isChecked():
        categoria = 'Hardware'
    else:
        categoria = 'Software'

    try:
        banco = sqlite3.connect('bancocadastro01.db')
        cursor = banco.cursor()
        cursor.execute("INSERT INTO dados (nome, codigo, preco, quantidade, categoria) VALUES (?,?,?,?,?)",
                       (nome, codigo,
                        preco,
                        quantidade,
                        categoria))

        # cursor.execute("DELETE FROM dados")
        banco.commit()
        tela1.lineEdit.setText("")
        tela1.lineEdit_2.setText("")
        tela1.lineEdit_3.setText("")
        tela1.lineEdit_4.setText("")
        print('Os dados foram inseridos com sucesso!!!')
        banco.close()

    except sqlite3.Error as erro:
        print('Erro ao inserir:', erro)


def visualizar_bd():
    tela2.show()
    banco = sqlite3.connect('bancocadastro01.db')
    cursor = banco.cursor()

    cursor.execute("SELECT * FROM dados")
    dados_lidos = cursor.fetchall()

    tela2.tableWidget.setRowCount(len(dados_lidos))
    tela2.tableWidget.setColumnCount(5)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 5):
            tela2.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


def sair():
    tela1.close()
    tela2.close()


def voltartela1():
    tela2.close()


app = QtWidgets.QApplication([])
tela1 = uic.loadUi('Bd_qtdesigner.ui')
tela2 = uic.loadUi('listartabela.ui')
tela1.pushButton_3.clicked.connect(sair)
tela1.pushButton_2.clicked.connect(visualizar_bd)
tela1.pushButton.clicked.connect(salvar_bd)
tela2.pushButton.clicked.connect(voltartela1)
tela2.pushButton_2.clicked.connect(sair)

tela1.show()
app.exec()
