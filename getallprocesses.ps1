Get-Process |where { $_.mainWindowTItle } | format-table name, mainwindowtitle