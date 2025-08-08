# kml_export


## Oveview KML

## 🧭 O que é um arquivo KML?

--> KML (Keyhole Markup Language) é um formato de XML usado pelo Google Earth, Google Maps e outros softwares de geolocalização para descrever:
--> Posições (latitude/longitude/altitude)
--> Rotas e trajetos
--> Áreas
--> Marcadores com ícones, textos e links
--> Animações e sobreposições de imagem


## 📌 Estrutura básica de um KML

### Um arquivo KML pode conter:

    1. Placemarks (Marcadores)
        --> Um ponto específico no mapa, com:
        --> Nome, descrição
        --> Coordenadas (latitude, longitude, altitude)
        --> Ícone customizado
        --> Horário (timestamp)
        --> Estilo (cor, tamanho, forma do ícone)`

    2. LineStrings (Rotas)
        --> Conectam uma série de pontos com linhas, úteis para:
        --> Trajetos de veículos
        --> Caminhadas, voos, etc.
        --> Linhas de condução (como em seu caso)

    3. Polygons (Áreas)
        --> Representam regiões delimitadas (ex: uma fazenda, uma zona de segurança, uma área de obra)

    4. Folders e Documentos
        --> Agrupam elementos:
        --> Pasta para cada veículo
        --> Pasta para cada intervalo de tempo
        --> Pasta por tipo de evento

    5. TimeStamp / TimeSpan
        --> Você pode associar tempo:
        --> TimeStamp: momento exato (ideal para logs por segundo)
        --> TimeSpan: intervalo de tempo (ideal para eventos longos, como uma rota de 1 minuto)

### 🔧 O que você pode personalizar (como na imagem que enviou)

#### 📍 Placemarks
--> Ícone (ícone padrão ou imagem personalizada)
--> Tamanho do ícone
--> Nome (visível na interface)
--> Descrição (suporta texto, HTML, links)
--> Estilo: cor do texto, borda, fundo
--> Grounding: se está no solo ou suspenso (útil para drones, por exemplo)
--> Altitude Mode:
    --> clampToGround: fixo ao solo
    --> relativeToGround: altitude relativa ao chão
    --> absolute: usa altitude real (em metros)

#### 📈 LineStrings (Rotas)
--> Espessura da linha
--> Cor da linha (pode ser RGBA com transparência)
--> Nome
--> Tempo associado (para animações)
--> Comportamento de altitude (voo, rota terrestre, etc.)

#### 🧭 Time Control
--> Com uso de TimeStamp ou TimeSpan, o Google Earth ativa um slider temporal que permite:
    --> Ver o que aconteceu em cada segundo
    --> Executar animações (como replay de um trajeto)

#### 🖼️ Overlays (Imagens)
--> Você pode sobrepor imagens (como mapas, plantas, zonas de obras)
--> Elas podem ser georreferenciadas com lat/lon em bordas
--> Ideal para representar:
    --> Mapas internos
    --> Áreas de risco
    --> Plantas de obras

#### 📂 Folders
--> Você pode:
    --> Agrupar por veículo, período, tipo de evento, rota, etc.
    --> Ativar/desativar visualização por grupo
    --> Criar hierarquias com subpastas

#### 💡 Exemplos de uso prático

| Elemento KML    | Exemplo prático para seu caso                      |
| --------------- | -------------------------------------------------- |
| `Placemark`     | Cada ponto GPS com horário (por segundo)           |
| `LineString`    | Uma rota de 1 minuto (conectando todos os pontos)  |
| `Folder`        | Grupo de dados de 1 minuto                         |
| `Document`      | Cada arquivo com 30 minutos de dados               |
| `Style`         | Destacar eventos importantes com ícones diferentes |
| `TimeStamp`     | Mostrar posição exata do veículo em cada segundo   |
| `TimeSpan`      | Mostrar o trajeto entre 10:00 e 10:01, por exemplo |
| `GroundOverlay` | Adicionar um mapa do canteiro ou imagem aérea      |
