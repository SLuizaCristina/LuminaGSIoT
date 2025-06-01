
# 🚨 Lumina – Sistema de Alerta em Apagões

> **Projeto da disciplina Physical Computing / IoT – Global Solution 2025 – 3º Ano de Engenharia de Software – FIAP**

## 🧠 Descrição do Problema

Apagões causados por eventos climáticos extremos, como chuvas fortes, ventanias e enchentes, são cada vez mais frequentes. Durante essas situações, pessoas em vulnerabilidade, como idosos ou pessoas com deficiência visual, podem ficar sem comunicação, sem internet e sem uma forma de pedir ajuda.

A falta de energia não é só um transtorno, mas também um risco à segurança e à vida.

## 💡 Nossa Solução – **Lumina**

O **Lumina** é um sistema desenvolvido em Python que permite que qualquer pessoa peça ajuda durante um apagão, mesmo sem acesso à internet.

Ele utiliza:
- 👋 **Reconhecimento de gestos** (como levantar a mão) para acionar alertas.
- 🎙️ **Reconhecimento de voz**, onde comandos como “**socorro**” ou “**ajuda**” ativam imediatamente um alerta.
- 📴 **Funciona offline**, sendo ideal para situações sem rede elétrica e sem internet.

> ✅ Pensado especialmente para auxiliar **idosos**, **pessoas com deficiência visual**, ou qualquer cidadão em situação de risco durante quedas de energia.

## 🎯 Funcionalidades

- 🔍 Detecção de mão levantada através da webcam.
- 🎧 Detecção de comandos de voz simples (“socorro” ou “ajuda”).
- 🚨 Gera alertas no terminal indicando que um pedido de ajuda foi acionado.
- 🔗 Preparado para futuras integrações via Bluetooth com aplicativos como o **App Lumina**.
- 💻 Sistema leve, roda em qualquer computador com webcam e microfone.

## 🛠️ Tecnologias e Bibliotecas

- 🐍 **Python 3**
- 🎥 **OpenCV** – captura de vídeo
- 🤖 **MediaPipe** – reconhecimento de gestos (mãos)
- 🎙️ **SpeechRecognition** – reconhecimento de voz
- 🎧 **PyAudio** – entrada de áudio (microfone)
- 🔗 *(Opcional)* **PyBluez** – conexão via Bluetooth (futuro)


## 🚀 Como Executar o Projeto

### Pré-requisitos

- Python instalado (versão 3.x)
- Webcam e microfone funcionando

### Instalação das dependências

No terminal, execute:

```bash
pip install -r requirements.txt
```

⚠️ Se der erro no `PyAudio`, baixe o `.whl`.

Depois instale assim:

```bash
pip install nome-do-arquivo.whl
```

### Executando o sistema

Clone o repositório ou baixe os arquivos.

Execute no terminal:

```bash
python lumina_signal.py
```

### Como Usar

- 🎥 Levante a mão na frente da webcam → **Gera alerta por gesto**.
- 🎙️ Fale claramente "**socorro**" ou "**ajuda**" → **Gera alerta por voz**.
- 🛑 Para encerrar, pressione a tecla **ESC** na janela de vídeo.



## 👥 Integrantes

| Nome               | RM         |
| ------------------ | ---------- |
| Luiza Cristina     | 99367      |
| Renato Izumi       | 99242      |
| Pedro Palladino    | 551180      |

## 📜 Licença

Projeto desenvolvido exclusivamente para fins acadêmicos – FIAP – 2025.
