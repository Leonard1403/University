/********************************************************************************
** Form generated from reading UI file 'AgentiedeTurismGUI.ui'
**
** Created by: Qt User Interface Compiler version 6.2.4
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_AGENTIEDETURISMGUI_H
#define UI_AGENTIEDETURISMGUI_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_AgentiedeTurismGUIClass
{
public:
    QMenuBar *menuBar;
    QToolBar *mainToolBar;
    QWidget *centralWidget;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *AgentiedeTurismGUIClass)
    {
        if (AgentiedeTurismGUIClass->objectName().isEmpty())
            AgentiedeTurismGUIClass->setObjectName(QString::fromUtf8("AgentiedeTurismGUIClass"));
        AgentiedeTurismGUIClass->resize(600, 400);
        menuBar = new QMenuBar(AgentiedeTurismGUIClass);
        menuBar->setObjectName(QString::fromUtf8("menuBar"));
        AgentiedeTurismGUIClass->setMenuBar(menuBar);
        mainToolBar = new QToolBar(AgentiedeTurismGUIClass);
        mainToolBar->setObjectName(QString::fromUtf8("mainToolBar"));
        AgentiedeTurismGUIClass->addToolBar(mainToolBar);
        centralWidget = new QWidget(AgentiedeTurismGUIClass);
        centralWidget->setObjectName(QString::fromUtf8("centralWidget"));
        AgentiedeTurismGUIClass->setCentralWidget(centralWidget);
        statusBar = new QStatusBar(AgentiedeTurismGUIClass);
        statusBar->setObjectName(QString::fromUtf8("statusBar"));
        AgentiedeTurismGUIClass->setStatusBar(statusBar);

        retranslateUi(AgentiedeTurismGUIClass);

        QMetaObject::connectSlotsByName(AgentiedeTurismGUIClass);
    } // setupUi

    void retranslateUi(QMainWindow *AgentiedeTurismGUIClass)
    {
        AgentiedeTurismGUIClass->setWindowTitle(QCoreApplication::translate("AgentiedeTurismGUIClass", "AgentiedeTurismGUI", nullptr));
    } // retranslateUi

};

namespace Ui {
    class AgentiedeTurismGUIClass: public Ui_AgentiedeTurismGUIClass {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_AGENTIEDETURISMGUI_H
