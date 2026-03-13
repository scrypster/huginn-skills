        ---
        name: powershell-expert
        version: 1.0.0
        author: community
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/powershell-expert/SKILL.md
        description: Write robust PowerShell scripts with error handling and module patterns.
        ---

        You write robust, maintainable PowerShell.

## Script Header
```powershell
#Requires -Version 7.0
[CmdletBinding(SupportsShouldProcess)]
param(
    [Parameter(Mandatory)][string]$Name,
    [switch]$Force
)
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
```

## Error Handling
```powershell
try {
    $result = Invoke-RestMethod -Uri $url -Method Post -Body $body
} catch [System.Net.WebException] {
    Write-Error "HTTP error: $($_.Exception.Message)"
    throw
} finally {
    # cleanup
}
```

## Rules
- Use approved verbs (Get-, Set-, New-, Remove-, Invoke-) for function names.
- Use `ShouldProcess` for destructive operations — enables -WhatIf.
- Use `Write-Verbose` for debug info, not `Write-Host`.
- Module functions in separate files, exported in `.psd1` manifest.
