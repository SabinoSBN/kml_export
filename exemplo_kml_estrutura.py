from simplekml import Kml, Color

kml = Kml()

# Adiciona estilo com ID (para ser referenciado corretamente)
estilo_ponto = kml.newstyle()
estilo_ponto.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/shapes/placemark_circle.png'
estilo_ponto.iconstyle.color = Color.red
estilo_ponto.iconstyle.scale = 1

estilo_linha = kml.newstyle()
estilo_linha.linestyle.width = 3
estilo_linha.linestyle.color = Color.blue

# Pasta
folder = kml.newfolder(name="2025-08-07 10:00")

# Adiciona 5 pontos (sem TimeStamp)
for i in range(5):
    p = folder.newpoint(
        name=f"10:00:{i:02d}",
        coords=[(9.941 + i*0.0001, 45.148 + i*0.0001)],
    )
    p.description = f"Posição registrada às 10:00:{i:02d}"
    p.style = estilo_ponto  # Estilo aplicado corretamente

# Rota (sem TimeSpan)
linha = folder.newlinestring(name="Rota 10:00")
linha.coords = [(9.941 + i*0.0001, 45.148 + i*0.0001) for i in range(5)]
linha.description = "Rota completa do minuto 10:00"
linha.style = estilo_linha

# Salvar
kml.save("exemplo_kml_comentado.kml")
