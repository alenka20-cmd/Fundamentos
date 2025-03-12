# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades Otavalo, Papallacta, Manta
# Segunda dimensión: Semanas (4 semanas)
# Tercera dimensión: Días de la semana (7 días)
ciudades = [ "Otavalo", " Papallacta", "Manta"]
temperaturas = [
    [   # Ciudad 1: Otavalo
        [   # Semana 1
            {"day": "Lunes", "temp": 16},
            {"day": "Martes", "temp": 17},
            {"day": "Miércoles", "temp": 15},
            {"day": "Jueves", "temp": 18},
            {"day": "Viernes", "temp": 16},
            {"day": "Sábado", "temp": 18},
            {"day": "Domingo", "temp": 19}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 17},
            {"day": "Martes", "temp": 18},
            {"day": "Miércoles", "temp": 17},
            {"day": "Jueves", "temp": 19},
            {"day": "Viernes", "temp": 17},
            {"day": "Sábado", "temp": 18},
            {"day": "Domingo", "temp": 18}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 16},
            {"day": "Martes", "temp": 15},
            {"day": "Miércoles", "temp": 15},
            {"day": "Jueves", "temp": 17},
            {"day": "Viernes", "temp": 16},
            {"day": "Sábado", "temp": 15},
            {"day": "Domingo", "temp": 15}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 16},
            {"day": "Martes", "temp": 15},
            {"day": "Miércoles", "temp": 17},
            {"day": "Jueves", "temp": 18},
            {"day": "Viernes", "temp": 20},
            {"day": "Sábado", "temp": 19},
            {"day": "Domingo", "temp": 18}
        ]
    ],
    [   # Ciudad 2: Papallacta
        [   # Semana 1
            {"day": "Lunes", "temp": 5},
            {"day": "Martes", "temp": 8},
            {"day": "Miércoles", "temp": 7},
            {"day": "Jueves", "temp": 6},
            {"day": "Viernes", "temp": 4},
            {"day": "Sábado", "temp": 5},
            {"day": "Domingo", "temp": 6}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 6},
            {"day": "Martes", "temp": 4},
            {"day": "Miércoles", "temp": 3},
            {"day": "Jueves", "temp": 5},
            {"day": "Viernes", "temp": 5},
            {"day": "Sábado", "temp": 4},
            {"day": "Domingo", "temp": 3}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 5},
            {"day": "Martes", "temp": 5},
            {"day": "Miércoles", "temp": 4},
            {"day": "Jueves", "temp": 6},
            {"day": "Viernes", "temp": 7},
            {"day": "Sábado", "temp": 7},
            {"day": "Domingo", "temp": 5}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 4},
            {"day": "Martes", "temp": 6},
            {"day": "Miércoles", "temp": 5},
            {"day": "Jueves", "temp": 4},
            {"day": "Viernes", "temp": 4},
            {"day": "Sábado", "temp": 4},
            {"day": "Domingo", "temp": 3}
        ]
    ],
    [   # Ciudad 3: Manta
        [   # Semana 1
            {"day": "Lunes", "temp": 26},
            {"day": "Martes", "temp": 27},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 27},
            {"day": "Sábado", "temp": 25},
            {"day": "Domingo", "temp": 25}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 26},
            {"day": "Martes", "temp": 27},
            {"day": "Miércoles", "temp": 26},
            {"day": "Jueves", "temp": 28},
            {"day": "Viernes", "temp": 29},
            {"day": "Sábado", "temp": 30},
            {"day": "Domingo", "temp": 29}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 29},
            {"day": "Martes", "temp": 30},
            {"day": "Miércoles", "temp": 31},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 30},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 29}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 28},
            {"day": "Martes", "temp": 29},
            {"day": "Miércoles", "temp": 29},
            {"day": "Jueves", "temp": 28},
            {"day": "Viernes", "temp": 29},
            {"day": "Sábado", "temp": 27},
            {"day": "Domingo", "temp": 26}
        ]
    ]
]

# Calcular el promedio de temperaturas para cada ciudad y semana
for i, ciudad in enumerate(temperaturas):
    print(f"\nPromedios de temperatura en {ciudades[i]}:")
    for j, semana in enumerate(ciudad):
        suma = sum(dia['temp'] for dia in semana)
        promedio = suma / len(semana)
        print(f"  Semana {j + 1}: {promedio:.0f}°C")