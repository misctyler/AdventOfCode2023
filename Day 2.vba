Sub CalculateAmountAndPower()
    Dim file_path As String
    Dim total_amount As Long, total_amount2 As Long
    Dim game_id As String, line As String, line_parse As String
    Dim sets As Variant, setInfo As Variant
    Dim color As String, num As Integer
    Dim blue_max As Integer, red_max As Integer, green_max As Integer
    Dim impossible As Boolean
    
    file_path = "Day 2 Input.txt"
    
    Open file_path For Input As #1
    
    total_amount = 0
    total_amount2 = 0
    
    Do Until EOF(1)
        Line Input #1, line
        line = Trim(line)
        game_id = Mid(line, 1, InStr(line, ":") - 1)
        game_id = Replace(game_id, "Game", "")
        line_parse = Mid(line, InStr(line, ":") + 1)
        line_parse = Replace(line_parse, ";", ",")
        sets = Split(line_parse, ",")
        impossible = False
        blue_max = 0
        red_max = 0
        green_max = 0
        
        For Each setInfo In sets
            setInfo = Trim(setInfo)
            num = Trim(Left(setInfo, 2))
            color = effThemDigits(Trim(Replace(setInfo, num, "")))
            If color = "blue" Then
                If num > blue_max Then blue_max = num
                If num > 14 Then impossible = True
            ElseIf color = "red" Then
                If num > red_max Then red_max = num
                If num > 12 Then impossible = True
            ElseIf color = "green" Then
                If num > green_max Then green_max = num
                If num > 13 Then impossible = True
            End If
        Next setInfo
        
        If Not impossible Then
            total_amount = total_amount + CInt(game_id)
        End If
        
        total_power = red_max * green_max * blue_max
        ' Debug.Print (total_power)
        total_amount2 = total_amount2 + total_power
    Loop
    
    Close #1
    MsgBox "Total Amount: " & total_amount & vbCrLf & "Total Power: " & total_amount2
End Sub

Function effThemDigits(inputString As String) As String
    Dim i As Integer
    Dim resultString As String
    resultString = ""
    For i = 1 To Len(inputString)
        Dim currentChar As String
        currentChar = Mid(inputString, i, 1)
        If IsNumeric(currentChar) Then
            resultString = resultString & ""
        Else
            resultString = resultString & currentChar
        End If
    Next i

    effThemDigits = resultString
End Function
