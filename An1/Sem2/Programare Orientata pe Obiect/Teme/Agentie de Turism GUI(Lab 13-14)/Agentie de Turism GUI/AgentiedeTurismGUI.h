#pragma once

#include <QtWidgets/QMainWindow>
#include "ui_AgentiedeTurismGUI.h"

class AgentiedeTurismGUI : public QMainWindow
{
    Q_OBJECT

public:
    AgentiedeTurismGUI(QWidget *parent = Q_NULLPTR);

private:
    Ui::AgentiedeTurismGUIClass ui;
};
