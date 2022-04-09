import QtQuick 2.0
import QtQuick.Layouts 1.11
import QtQuick.Controls 2.1
import QtQuick.Window 2.1
import QtQuick.Controls.Material 2.1

import io.qt.textproperties 1.0


ApplicationWindow {
    id: page
    width: 600
    height: 400
    visible: true
    Material.theme: Material.Dark
    Material.accent: Material.Green

    Bridge {
        id: bridge
    }

    ColumnLayout {
        anchors.fill: parent
        anchors.margins: 3

        Text {
            id: title
            text: "RAINBOW DRINKING"
            font.family: "Helvetica"
            font.pointSize: 24
            color: "chartreuse"
            Layout.alignment: Qt.AlignHCenter
        }

        GridLayout {
            id: grid
            rows: 6
            columnSpacing: 20
            flow: GridLayout.TopToBottom
            
            Text {
                text: "Player Names:"
                color: "steelblue"
                font.bold: true
                font.family: "Helvetica"
                font.pointSize: 18
                horizontalAlignment: Qt.AlignHCenter
                Layout.fillWidth: true
            }
            TextField {
                id: player1
                font.family: "Helvetica"
                font.pointSize: 16
                horizontalAlignment: Qt.AlignHCenter
                Layout.fillWidth: true
                placeholderText: "Player Name"
            }
            TextField {
                id: player2
                font.family: "Helvetica"
                font.pointSize: 16
                horizontalAlignment: Qt.AlignHCenter
                Layout.fillWidth: true
                placeholderText: "Player Name"
            }
            TextField {
                id: player3
                font.family: "Helvetica"
                font.pointSize: 16
                horizontalAlignment: Qt.AlignHCenter
                Layout.fillWidth: true
                placeholderText: "Player Name"
            }
            TextField {
                id: player4
                font.family: "Helvetica"
                font.pointSize: 16
                horizontalAlignment: Qt.AlignHCenter
                Layout.fillWidth: true
                placeholderText: "Player Name"
            }
            TextField {
                id: player5
                font.family: "Helvetica"
                font.pointSize: 16
                horizontalAlignment: Qt.AlignHCenter
                Layout.fillWidth: true
                placeholderText: "Player Name"
            }

            Text {
                text: "SIPS:"
                color: "steelblue"
                font.bold: true
                font.family: "Helvetica"
                font.pointSize: 18
                horizontalAlignment: Qt.AlignHCenter
                Layout.fillWidth: true
            }
            RowLayout {
                Button {
                    Layout.alignment: Qt.AlignHCenter
                    text: "+"
                    highlighted: true
                    Material.accent: Material.Green
                    onClicked: {
                        sip1.text = bridge.plus(sip1.text)
                    }
                }
                Button {
                    Layout.alignment: Qt.AlignHCenter
                    text: "-"
                    highlighted: true
                    Material.accent: Material.Red
                    onClicked: {
                        sip1.text = bridge.minus(sip1.text)
                       }
                }
                Text {
                    id: sip1
                    text: "0"
                    font.family: "Helvetica"
                    font.pointSize: 16
                    horizontalAlignment: Qt.AlignHCenter
                    Layout.fillWidth: true
                }
            }
            RowLayout {
                Button {
                    Layout.alignment: Qt.AlignHCenter
                    text: "+"
                    highlighted: true
                    Material.accent: Material.Green
                    onClicked: {
                        sip2.text = bridge.plus(sip2.text)
                    }
                }
                Button {
                    Layout.alignment: Qt.AlignHCenter
                    text: "-"
                    highlighted: true
                    Material.accent: Material.Red
                    onClicked: {
                        sip2.text = bridge.minus(sip2.text)
                       }
                }
                Text {
                    id: sip2
                    text: "0"
                    font.family: "Helvetica"
                    font.pointSize: 16
                    horizontalAlignment: Qt.AlignHCenter
                    Layout.fillWidth: true
                }
            }
            RowLayout {
                Button {
                    Layout.alignment: Qt.AlignHCenter
                    text: "+"
                    highlighted: true
                    Material.accent: Material.Green
                    onClicked: {
                        sip3.text = bridge.plus(sip3.text)
                    }
                }
                Button {
                    Layout.alignment: Qt.AlignHCenter
                    text: "-"
                    highlighted: true
                    Material.accent: Material.Red
                    onClicked: {
                        sip3.text = bridge.minus(sip3.text)
                       }
                }
                Text {
                    id: sip3
                    text: "0"
                    font.family: "Helvetica"
                    font.pointSize: 16
                    horizontalAlignment: Qt.AlignHCenter
                    Layout.fillWidth: true
                }
            }
            RowLayout {
                Button {
                    Layout.alignment: Qt.AlignHCenter
                    text: "+"
                    highlighted: true
                    Material.accent: Material.Green
                    onClicked: {
                        sip4.text = bridge.plus(sip4.text)
                    }
                }
                Button {
                    Layout.alignment: Qt.AlignHCenter
                    text: "-"
                    highlighted: true
                    Material.accent: Material.Red
                    onClicked: {
                        sip4.text = bridge.minus(sip4.text)
                       }
                }
                Text {
                    id: sip4
                    text: "0"
                    font.family: "Helvetica"
                    font.pointSize: 16
                    horizontalAlignment: Qt.AlignHCenter
                    Layout.fillWidth: true
                }
            }
            RowLayout {
                Button {
                    Layout.alignment: Qt.AlignHCenter
                    text: "+"
                    highlighted: true
                    Material.accent: Material.Green
                    onClicked: {
                        sip5.text = bridge.plus(sip5.text)
                    }
                }
                Button {
                    Layout.alignment: Qt.AlignHCenter
                    text: "-"
                    highlighted: true
                    Material.accent: Material.Red
                    onClicked: {
                        sip5.text = bridge.minus(sip5.text)
                       }
                }
                Text {
                    id: sip5
                    text: "0"
                    font.family: "Helvetica"
                    font.pointSize: 16
                    horizontalAlignment: Qt.AlignHCenter
                    Layout.fillWidth: true
                }
            }

            Text {
                text: "SHOTS:"
                color: "steelblue"
                font.bold: true
                font.family: "Helvetica"
                font.pointSize: 18
                horizontalAlignment: Qt.AlignHCenter
                Layout.fillWidth: true
            }
            RowLayout {
                Button {
                    Layout.alignment: Qt.AlignHCenter
                    text: "+"
                    highlighted: true
                    Material.accent: Material.Green
                    onClicked: {
                        shot1.text = bridge.plus(shot1.text)
                    }
                }
                Button {
                    Layout.alignment: Qt.AlignHCenter
                    text: "-"
                    highlighted: true
                    Material.accent: Material.Red
                    onClicked: {
                        shot1.text = bridge.minus(shot1.text)
                       }
                }
                Text {
                    id: shot1
                    text: "0"
                    font.family: "Helvetica"
                    font.pointSize: 16
                    horizontalAlignment: Qt.AlignHCenter
                    Layout.fillWidth: true
                }
            }
            RowLayout {
                Button {
                    Layout.alignment: Qt.AlignHCenter
                    text: "+"
                    highlighted: true
                    Material.accent: Material.Green
                    onClicked: {
                        shot2.text = bridge.plus(shot2.text)
                    }
                }
                Button {
                    Layout.alignment: Qt.AlignHCenter
                    text: "-"
                    highlighted: true
                    Material.accent: Material.Red
                    onClicked: {
                        shot2.text = bridge.minus(shot2.text)
                       }
                }
                Text {
                    id: shot2
                    text: "0"
                    font.family: "Helvetica"
                    font.pointSize: 16
                    horizontalAlignment: Qt.AlignHCenter
                    Layout.fillWidth: true

                }
            }
            RowLayout {
                Button {
                    Layout.alignment: Qt.AlignHCenter
                    text: "+"
                    highlighted: true
                    Material.accent: Material.Green
                    onClicked: {
                        shot3.text = bridge.plus(shot3.text)
                    }
                }
                Button {
                    Layout.alignment: Qt.AlignHCenter
                    text: "-"
                    highlighted: true
                    Material.accent: Material.Red
                    onClicked: {
                        shot3.text = bridge.minus(shot3.text)
                       }
                }
                Text {
                    id: shot3
                    text: "0"
                    font.family: "Helvetica"
                    font.pointSize: 16
                    horizontalAlignment: Qt.AlignHCenter
                    Layout.fillWidth: true

                }
            }
            RowLayout {
                Button {
                    Layout.alignment: Qt.AlignHCenter
                    text: "+"
                    highlighted: true
                    Material.accent: Material.Green
                    onClicked: {
                        shot4.text = bridge.plus(shot4.text)
                    }
                }
                Button {
                    Layout.alignment: Qt.AlignHCenter
                    text: "-"
                    highlighted: true
                    Material.accent: Material.Red
                    onClicked: {
                        shot4.text = bridge.minus(shot4.text)
                       }
                }
                Text {
                    id: shot4
                    text: "0"
                    font.family: "Helvetica"
                    font.pointSize: 16
                    horizontalAlignment: Qt.AlignHCenter
                    Layout.fillWidth: true
                }
            }
            RowLayout {
                Button {
                    Layout.alignment: Qt.AlignHCenter
                    text: "+"
                    highlighted: true
                    Material.accent: Material.Green
                    onClicked: {
                        shot5.text = bridge.plus(shot5.text)
                    }
                }
                Button {
                    Layout.alignment: Qt.AlignHCenter
                    text: "-"
                    highlighted: true
                    Material.accent: Material.Red
                    onClicked: {
                        shot5.text = bridge.minus(shot5.text)
                       }
                }
                Text {
                    id: shot5
                    text: "0"
                    font.family: "Helvetica"
                    font.pointSize: 16
                    horizontalAlignment: Qt.AlignHCenter
                    Layout.fillWidth: true
                }
            } 
        }
        RowLayout{
            Layout.alignment: Qt.AlignHCenter
            Button {
                Layout.alignment: Qt.AlignHCenter
                text: "Result"
                padding: 20
                highlighted: true
                Material.accent: Material.Blue
                onClicked: {
                    bridge.create_result(
                        [player1.text, player2.text, player3.text, player4.text, player5.text],
                        [sip1.text, sip2.text, sip3.text, sip4.text, sip5.text],
                        [shot1.text, shot2.text, shot3.text, shot4.text, shot5.text]
                    )
                }
            }
            Button {
                Layout.alignment: Qt.AlignHCenter
                text: "Reset"
                padding: 20
                highlighted: true
                Material.accent: Material.Blue
                onClicked: {
                        player1.text = ""
                        player2.text = ""
                        player3.text = ""
                        player4.text = ""
                        player5.text = ""
                        sip1.text = "0"
                        sip2.text = "0"
                        sip3.text = "0"
                        sip4.text = "0"
                        sip5.text = "0"
                        shot1.text = "0"
                        shot2.text = "0"
                        shot3.text = "0"
                        shot4.text = "0" 
                        shot5.text = "0"
                }
            }
        }
    }    
}
