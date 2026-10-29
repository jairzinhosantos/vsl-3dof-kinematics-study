# Study map

El estudio conecta la lectura con una pregunta, una prueba y una decisión. Los productos académicos se construyen desde evidencia revisada.

```mermaid
flowchart LR
    S[Consigna y rúbrica] --> A[Alcance y preguntas]
    P[Paper y lectura crítica] --> M[Modelo nominal compartido]
    A --> M
    M --> F[Directa: Josemanuel]
    F --> I[Inversa: Melissa]
    F --> J[Diferencial: Jairzinho]
    J --> G[Singularidades: Renzo]
    J --> C[Control: Kenny]
    I --> E[Experimentos reproducibles]
    G --> E
    C --> E
    E --> R[Review del equipo]
    R --> D[Informe y exposición]
```

## Flujo de evidencia

```mermaid
flowchart TD
    A[Parámetros publicados y convenciones] --> B[Modelo Python]
    Q[Escenario y configuración] --> B
    B --> T[Tests numéricos y simbólicos]
    B --> N[Movimiento sintético con procedencia]
    N --> V[Gráficas y visor 3D]
    N --> BL[Escena Blender]
    N --> X[Fixture dummy con ruido declarado]
    T --> R[Resultado y limitaciones]
    V --> R
    BL --> R
    X --> R
    R --> H[Revisión humana]
```

El movimiento sintético, el sensor dummy y las mediciones reales son categorías diferentes. Un resultado visualmente correcto puede seguir teniendo un modelo equivocado; por eso las pruebas se conservan junto a las figuras.
