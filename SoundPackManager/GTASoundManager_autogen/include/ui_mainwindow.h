/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 6.8.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QListWidget>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralwidget;
    QLineEdit *gtaFolderInput;
    QPushButton *browseButton;
    QListWidget *soundPackList;
    QPushButton *addPackButton;
    QPushButton *removePackButton;
    QPushButton *setSelectedButton;
    QPushButton *backupOriginalButton;
    QPushButton *restoreOriginalButton;
    QListWidget *publicPackList;
    QPushButton *previewButton;
    QPushButton *downloadButton;
    QLabel *label;
    QLabel *label_2;
    QMenuBar *menubar;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName("MainWindow");
        MainWindow->resize(810, 431);
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName("centralwidget");
        gtaFolderInput = new QLineEdit(centralwidget);
        gtaFolderInput->setObjectName("gtaFolderInput");
        gtaFolderInput->setGeometry(QRect(70, 20, 501, 21));
        browseButton = new QPushButton(centralwidget);
        browseButton->setObjectName("browseButton");
        browseButton->setGeometry(QRect(580, 20, 80, 21));
        soundPackList = new QListWidget(centralwidget);
        soundPackList->setObjectName("soundPackList");
        soundPackList->setGeometry(QRect(70, 100, 291, 192));
        addPackButton = new QPushButton(centralwidget);
        addPackButton->setObjectName("addPackButton");
        addPackButton->setGeometry(QRect(70, 300, 91, 31));
        removePackButton = new QPushButton(centralwidget);
        removePackButton->setObjectName("removePackButton");
        removePackButton->setGeometry(QRect(170, 300, 91, 31));
        setSelectedButton = new QPushButton(centralwidget);
        setSelectedButton->setObjectName("setSelectedButton");
        setSelectedButton->setGeometry(QRect(270, 300, 91, 31));
        setSelectedButton->setAutoFillBackground(false);
        backupOriginalButton = new QPushButton(centralwidget);
        backupOriginalButton->setObjectName("backupOriginalButton");
        backupOriginalButton->setGeometry(QRect(70, 340, 121, 31));
        restoreOriginalButton = new QPushButton(centralwidget);
        restoreOriginalButton->setObjectName("restoreOriginalButton");
        restoreOriginalButton->setGeometry(QRect(240, 340, 121, 31));
        publicPackList = new QListWidget(centralwidget);
        publicPackList->setObjectName("publicPackList");
        publicPackList->setGeometry(QRect(460, 100, 281, 192));
        previewButton = new QPushButton(centralwidget);
        previewButton->setObjectName("previewButton");
        previewButton->setGeometry(QRect(500, 300, 91, 31));
        downloadButton = new QPushButton(centralwidget);
        downloadButton->setObjectName("downloadButton");
        downloadButton->setGeometry(QRect(610, 300, 91, 31));
        label = new QLabel(centralwidget);
        label->setObjectName("label");
        label->setGeometry(QRect(170, 70, 111, 16));
        QFont font;
        font.setFamilies({QString::fromUtf8("Impact")});
        font.setPointSize(12);
        label->setFont(font);
        label_2 = new QLabel(centralwidget);
        label_2->setObjectName("label_2");
        label_2->setGeometry(QRect(560, 70, 111, 20));
        label_2->setFont(font);
        MainWindow->setCentralWidget(centralwidget);
        menubar = new QMenuBar(MainWindow);
        menubar->setObjectName("menubar");
        menubar->setGeometry(QRect(0, 0, 810, 21));
        MainWindow->setMenuBar(menubar);
        statusbar = new QStatusBar(MainWindow);
        statusbar->setObjectName("statusbar");
        MainWindow->setStatusBar(statusbar);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QCoreApplication::translate("MainWindow", "MainWindow", nullptr));
        gtaFolderInput->setText(QCoreApplication::translate("MainWindow", "Locate GTA 5 SFX Directory", nullptr));
        browseButton->setText(QCoreApplication::translate("MainWindow", "Browse", nullptr));
#if QT_CONFIG(tooltip)
        soundPackList->setToolTip(QCoreApplication::translate("MainWindow", "<html><head/><body><p><br/></p></body></html>", nullptr));
#endif // QT_CONFIG(tooltip)
        addPackButton->setText(QCoreApplication::translate("MainWindow", "\342\236\225 Add ", nullptr));
        removePackButton->setText(QCoreApplication::translate("MainWindow", "\342\236\226 Remove ", nullptr));
        setSelectedButton->setText(QCoreApplication::translate("MainWindow", "\342\234\205 Set Pack", nullptr));
        backupOriginalButton->setText(QCoreApplication::translate("MainWindow", "\360\237\222\276 Backup Default", nullptr));
        restoreOriginalButton->setText(QCoreApplication::translate("MainWindow", "\360\237\223\251 Return To Default", nullptr));
        previewButton->setText(QCoreApplication::translate("MainWindow", "\360\237\216\247Preview", nullptr));
        downloadButton->setText(QCoreApplication::translate("MainWindow", "\360\237\222\275 Download", nullptr));
        label->setText(QCoreApplication::translate("MainWindow", "\360\237\216\265 Your Packs", nullptr));
        label_2->setText(QCoreApplication::translate("MainWindow", " Public Packs \360\237\214\215", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
