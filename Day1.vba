' Day 1 Puzzle Input goes in Column A
' Both solutions print to Immediate Window

Sub Main()
    Application.ScreenUpdating = False
    Application.Calculation = xlCalculationManual
    Calibrate (0)
    Calibrate (1)
    Application.ScreenUpdating = True
    Application.Calculation = xlCalculationAutomatic
    ThisWorkbook.Save
End Sub

Function Calibrate(second_round As Boolean)
    Dim calibrationTotal As Long
    Dim lastRow As Long
    Dim i As Long
    Dim cellValue As String
    lastRow = Cells(Rows.Count, "A").End(xlUp).Row
    For i = 1 To lastRow
        cellValue = Cells(i, 1).Value
        Dim firstDigit As String
        Dim lastDigit As String
        If second_round = True Then
            cellValue = ReplaceTextNumbers(cellValue)
        End If
        firstDigit = GetFirstDigit(cellValue)
        lastDigit = GetLastDigit(cellValue)
        Dim calibrationValue As Integer
        calibrationValue = Val(firstDigit) * 10 + Val(lastDigit)
        calibrationTotal = calibrationTotal + calibrationValue
    Next i
    Debug.Print "Total Calibration Value: " & calibrationTotal
End Function

Function GetFirstDigit(s As String) As String
    Dim i As Integer
    For i = 1 To Len(s)
        If IsNumeric(Mid(s, i, 1)) Then
            GetFirstDigit = Mid(s, i, 1)
            Exit Function
        End If
    Next i
End Function

Function GetLastDigit(s As String) As String
    Dim i As Integer
    For i = Len(s) To 1 Step -1
        If IsNumeric(Mid(s, i, 1)) Then
            GetLastDigit = Mid(s, i, 1)
            Exit Function
        End If
    Next i
End Function

Function ReplaceTextNumbers(s As String) As String
    s = Replace(s, "one", "o1e")
    s = Replace(s, "two", "t2o")
    s = Replace(s, "three", "t3e")
    s = Replace(s, "four", "f4r")
    s = Replace(s, "five", "f5e")
    s = Replace(s, "six", "s6x")
    s = Replace(s, "seven", "s7n")
    s = Replace(s, "eight", "e8t")
    s = Replace(s, "nine", "n9e")
    ReplaceTextNumbers = s
End Function

