# 🏥 Roteador de Hospitais com Dijkstra, Mapas e Visualização Gráfica

Este projeto utiliza o algoritmo de Dijkstra para encontrar a rota mais rápida entre o hospital Che Guevara no município de Maricá para outros hospitais do estado do Rio de Janeiro, otimizando o transporte de órgãos para transplantes.

Ele exibe o caminho em um grafo visual com o NetworkX e em um mapa interativo com o Folium, utilizando dados reais de localização e tempo estimado de percurso via OpenRouteService API.

---

## 🛠️ Tecnologias Utilizadas

- Python 3.10+**
- [NetworkX](https://networkx.org/)  
- [Matplotlib](https://matplotlib.org/)  
- [Folium](https://python-visualization.github.io/folium/)  
- [OpenRouteService API](https://openrouteservice.org/)  
- Algoritmo de Dijkstra com heapq (fila de prioridade)

---

## 📁 Estrutura dos Arquivos

```
projeto/
│
├── dijkstra.py               # Implementação do algoritmo de Dijkstra
├── exibir_grafo.py           # Visualização do grafo com a rota
├── exibir_mapa.py            # Geração do mapa com a rota
├── grafos.py                 # Definição do grafo e coordenadas dos hospitais
├── main.py                   # Script principal de execução do programa
```

---

## 📦 Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/LogicWay.git
cd LogicWay
```

2. Crie um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

## ▶️ Como Executar

Basta rodar o script principal:

```bash
python main.py
```

1. O programa listará os hospitais disponíveis.
2. Você escolhe o destino.
3. O programa mostrará o melhor caminho, o tempo estimado, e abrirá um mapa.

---

## 📌 Contribuidores

Projeto desenvolvido por:

**Guilherme Mello** - @GuiMell0
**Ana Carolina** - @anacgsx
**Lucas Valença** - @Lucas-valenca
