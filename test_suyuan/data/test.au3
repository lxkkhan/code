send("v")
Sleep(1000)
ControlFocus("另存为","","Edit1")
WinWait("[CLASS:#32770]","",10)
ControlSetText("另存为","", "Edit1", "D:\gitCode\code\test_suyuan\data\picture\ST.png")
Sleep(2000)
ControlClick("另存为","","Button2")
Sleep(2000)
ControlFocus("确认另存为","","")
ControlClick("确认另存为","","Button1")
Sleep(2000)