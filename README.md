# 🎮 Pokoio - Jogos para Crianças

Um site divertido com vários jogos de ação para crianças se divertirem!

## 🚀 Funcionalidades

- 🐦 **Flappy Bird** - Desvie dos obstáculos
- 🐍 **Snake** - Coma e cresça
- 🧱 **Breakout** - Quebre todos os tijolos
- 🧠 **Memória** - Encontre os pares

## 📋 Requisitos

- Python 3.7+
- Flask 2.3.0

## 🔧 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/ratodacueca-ops/Pokoio.git
cd Pokoio
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## ▶️ Como Rodar

```bash
python app.py
```

Acesse: `http://localhost:5000`

## 🎯 Como Jogar

1. **Digite seu nome** no campo de entrada
2. **Clique em um jogo** para começar
3. **Use espaço ou clique** para controlar seu personagem
4. **Acumule pontos** e apareça no ranking!

## 📊 Ranking

Todas as pontuações são salvas e você pode acompanhar o ranking de cada jogo na página inicial.

## 🛠️ Estrutura do Projeto

```
Pokoio/
├── app.py              # Aplicação Flask principal
├── requirements.txt    # Dependências Python
├── scores.json         # Arquivo de pontuações
├── templates/
│   ├── index.html      # Página inicial
│   ├── flappy.html     # Jogo Flappy Bird
│   ├── snake.html      # Jogo Snake (em desenvolvimento)
│   ├── breakout.html   # Jogo Breakout (em desenvolvimento)
│   └── memory.html     # Jogo Memória (em desenvolvimento)
└── static/
    ├── style.css       # Estilos gerais
    ├── main.js         # JavaScript da página inicial
    ├── flappy.js       # Lógica do Flappy Bird
    ├── snake.js        # Lógica do Snake (em desenvolvimento)
    ├── breakout.js     # Lógica do Breakout (em desenvolvimento)
    └── memory.js       # Lógica da Memória (em desenvolvimento)
```

## 🎨 Tecnologias Utilizadas

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Armazenamento**: JSON
- **Canvas**: HTML5 Canvas para renderização dos jogos

## 🚧 Próximas Funcionalidades

- [ ] Jogo Snake completo
- [ ] Jogo Breakout completo
- [ ] Jogo Memória completo
- [ ] Sistema de login
- [ ] Multiplicador de pontos por dificuldade
- [ ] Som e efeitos visuais
- [ ] Temas diferentes

## 📝 Licença

Este projeto é de código aberto e disponível para uso educacional.

---

**Desenvolvido com ❤️ para crianças** 🎮✨