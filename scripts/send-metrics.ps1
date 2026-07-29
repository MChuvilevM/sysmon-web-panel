$HostName = "localhost"
$ApiUrl = "http://localhost:8000/api/metrics/"

while ($true) {
    try {
        $cpuSample = Get-Counter '\Processor(_Total)\% Processor Time' -ErrorAction Stop
        $cpu = $cpuSample.CounterSamples.CookedValue
    } catch {
        $cpu = 0
    }

    try {
        $os = Get-CimInstance Win32_OperatingSystem -ErrorAction Stop
        $memory = (($os.TotalVisibleMemorySize - $os.FreePhysicalMemory) / $os.TotalVisibleMemorySize) * 100
    } catch {
        $memory = 0
    }

    try {
        $drive = Get-PSDrive C -ErrorAction Stop
        $used = $drive.Used
        $free = $drive.Free
        $disk = ($used / ($used + $free)) * 100
    } catch {
        $disk = 0
    }

    $body = @{
        host = $HostName
        cpu_usage = [math]::Round([double]$cpu, 2)
        memory_usage = [math]::Round([double]$memory, 2)
        disk_usage = [math]::Round([double]$disk, 2)
    } | ConvertTo-Json

    try {
        Invoke-RestMethod -Uri $ApiUrl -Method Post -Body $body -ContentType "application/json" -ErrorAction Stop
    } catch {
        Write-Warning "Ошибка отправки данных: $_"
    }
    
    Start-Sleep -Seconds 5
}
