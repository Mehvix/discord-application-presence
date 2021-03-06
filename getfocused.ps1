$code = @'
    [DllImport("user32.dll")]
     public static extern IntPtr GetForegroundWindow();
'@
Add-Type $code -Name Utils -Namespace Win32
$hwnd = [Win32.Utils]::GetForegroundWindow()
Get-Process |
    Where-Object { $_.mainWindowHandle -eq $hwnd } |
    Select-Object ProcessName, MainWindowTitle
