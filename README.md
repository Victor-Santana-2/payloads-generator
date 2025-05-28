# **Gerador de Payloads para Pentest**

Este projeto é um **gerador de payloads** para testes de penetração, desenvolvido em Python com interface gráfica (GUI) usando `tkinter`. Ele permite gerar payloads comuns como **reverse shells, XSS, SQL Injection, SSTI e Command Injection**.

---

## **📌 Visão Geral**
- **Linguagem**: Python 3.x
- **Bibliotecas**: `tkinter` (GUI padrão), `json` (para exportação)
- **Finalidade**: Auxiliar pentesters e pesquisadores de segurança a gerar payloads rapidamente.

---

## **⚙️ Funcionalidades**
| Feature               | Descrição                                                                 |
|-----------------------|---------------------------------------------------------------------------|
| **Reverse Shell**     | Gera payloads para Bash, Python, Netcat e PowerShell.                     |
| **XSS**               | Gera payloads para Cross-Site Scripting (refletido, armazenado, DOM).     |
| **SQL Injection**     | Gera payloads para ataques SQLi (UNION-based, error-based, blind).        |
| **SSTI**              | Gera payloads para Server-Side Template Injection (Jinja2, Twig, etc.).  |
| **Command Injection** | Gera payloads para injeção de comandos (Bash, Windows).                  |
| **Exportação**        | Salva payloads em `.txt` ou `.json`.                                      |

---

## **📦 Estrutura do Projeto**
```plaintext
payload-generator/
│
├── main.py                # Script principal (GUI e lógica)
├── payloads/              # Módulos de payloads
│   ├── reverse_shells.py  # Payloads de reverse shell
│   ├── xss.py            # Payloads de XSS
│   ├── sql_injection.py  # Payloads de SQLi
│   ├── ssti.py           # Payloads de SSTI
│   └── command_injection.py  # Payloads de command injection
│
├── utils.py               # Funções auxiliares (salvar arquivos)
└── README.md             # Documentação (este arquivo)
```

---

## **🚀 Como Usar**
### **Pré-requisitos**
- Python 3.x
- Biblioteca `tkinter` (já incluída na instalação padrão do Python)

### **Instalação**
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/payload-generator.git
   cd payload-generator
   ```

2. Execute o script:
   ```bash
   python main.py
   ```

### **Capturas de Tela**
![Interface](https://github.com/user-attachments/assets/6661d9b4-0ae3-4d94-b534-45f6974c6a96)
)  

---

## **🛠️ Exemplos de Uso**
### **1. Gerar Reverse Shell**
```bash
python main.py -t reverse_shell --lhost 192.168.1.100 --lport 4444
```

### **2. Gerar XSS e Salvar em Arquivo**
```bash
python main.py -t xss -o xss_payloads.txt
```

### **3. Gerar SQL Injection em JSON**
```bash
python main.py -t sqli -o sqli_payloads.json
```

---

## **📝 Documentação dos Módulos**
### **1. `reverse_shells.py`**
```python
class ReverseShellPayloads:
    def generate(lhost: str, lport: int) -> list[str]:
        """
        Gera payloads de reverse shell.
        
        Args:
            lhost (str): IP de escuta.
            lport (int): Porta de escuta.
        
        Returns:
            list[str]: Lista de payloads.
        """
```

### **2. `utils.py`**
```python
def save_to_file(payloads: list, filename: str) -> None:
    """
    Salva payloads em um arquivo (TXT/JSON).
    
    Args:
        payloads (list): Lista de payloads.
        filename (str): Nome do arquivo (.txt ou .json).
    """
```

---

## **🔧 Contribuição**
1. Faça um fork do projeto.
2. Crie uma branch (`git checkout -b feature/nova-funcionalidade`).
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`).
4. Push para a branch (`git push origin feature/nova-funcionalidade`).
5. Abra um **Pull Request**.

---

## **📜 Licença**
MIT License. Consulte o arquivo [LICENSE](LICENSE) para detalhes.

---

## **📌 Contato**
- **Autor**: [Victor Santana](https://github.com/Victor-Santana-2)
- **Email**: victor.santana_2@hotmail.com

---
