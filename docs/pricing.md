# Costos de operacion mensual (COM)

$ COM = SED + CHP + RE $

__SED:__ Salario de desarrolladores

| Dev | Salario |
|-----|------|
| Dev Fullstack 1 | $ 5.000.000 |
| Dev Fullstack 2 | $ 5.000.000 |
| Product Leader  | $ 5.000.000 |

__CHP:__ Costos de Herramientas y plataformas

| Herramientas | Costo Mensual |
|-----|------|
| Dev 1 Github Copilot | $ 60.000 |
| Dev 2 Github Copilot | $ 60.000 |
| AWS Lightsail dev Instance | $ 30.000 |

__RE:__ Recursos externos

No se que recursos externos poner

## Cálculos del Proyecto

### Definiciones

- **TPP (Total Project Points)**: Suma de la columna "Esfuerzo" de HU.csv.
- **COM (Monthly Operational Cost)**: Suma de costos de MONTHLY.csv (analizados removiendo $ y .).
- **V (Velocity)**: 16 puntos por sprint.
- **CEPHU**: COM / V
- **CEP (Total Cost)**: TPP * CEPHU
- **Total Time**: (TPP / V) * 15 días

### Resultados de Cálculo de Costo del Proyecto

| Métrica | Valor |
|---------|-------|
| **Total Project Points (TPP)** | 124 |
| **Monthly Operational Cost (COM)** | $15,150,000 |
| **Sprint Velocity (V)** | 16 points/sprint |
| **Cost per Effort Hour Unit (CEPHU)** | $946,875.00 |
| **Total Project Cost (CEP)** | $117,412,500.00 |
| **Total Time Required** | 116.25 days |

