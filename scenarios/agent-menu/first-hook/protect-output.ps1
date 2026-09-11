# protect-output.ps1 — PreToolUse hook for Write|Edit (Windows PowerShell variant).
# Blocks any file write outside participant-output\ (exit 2 = block, message on stderr).
$raw = [Console]::In.ReadToEnd()
try { $payload = $raw | ConvertFrom-Json } catch { exit 0 }
$path = [string]$payload.tool_input.file_path
if (-not $path) { exit 0 }
$norm = $path -replace '\\', '/'
if ($norm -match '(^|/)participant-output/') { exit 0 }
[Console]::Error.WriteLine("Blocked by first-hook: agents may only write under participant-output/ (asked for: $path)")
exit 2
