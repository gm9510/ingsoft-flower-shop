# Product Backlog - Floristería Online

# Objetivos del Proyecto
- Permitir la venta de arreglos florales en línea con entrega programada.
- Gestionar inventario de flores y arreglos.
- Facilitar la logística de entregas y guías para repartidores.
- Integrar pasarela de pago y facturación automática.
- Permitir devoluciones, reembolsos y calificación de productos.
- Proveer dashboard para reservas y reportes de inventario.
- Imprimir etiquetas para entregas y limitar reservas diarias.
- hola eduard y hola gustavo

---

## Historias de Usuario

| Prioridad | Código | Actor | Historia | Esfuerzo | Tipo |
|-----------|-------|-------|----------|----------|------|
| Alta      | HU1   | Cliente | Como cliente, quiero comprar arreglos florales en línea con entrega programada | 8 | Funcional |
| Alta      | HU2   | Cliente | Como cliente, quiero pagar en línea con múltiples métodos de pago | 8 | Funcional |
| Alta      | HU3   | Cliente | Como cliente, quiero registrar una cuenta para agilizar mis compras | 5 | Funcional |
| Alta      | HU4   | Cliente | Como cliente, quiero recibir una factura para verificar el cobro | 5 | Funcional |
| Alta      | HU5   | Cliente | Como cliente, quiero poder calificar el producto | 3 | Funcional |
| Alta      | HU6   | Cliente | Como cliente, quiero solicitar un reembolso en caso de error | 5 | Funcional |
| Alta      | HU7   | Cliente | Como cliente, quiero recibir notificaciones sobre el estado de mi entrega | 5 | Funcional |
| Media     | HU8   | Admin   | Como administrador, quiero gestionar el inventario de flores y arreglos | 8 | Técnica |
| Media     | HU9   | Admin   | Como administrador, quiero generar reportes de inventario para cualquier rango de fechas | 5 | Técnica |
| Media     | HU10  | Admin   | Como administrador, quiero actualizar precios para promociones o cambios de costo | 5 | Técnica |
| Media     | HU11  | Admin   | Como administrador, quiero tener un dashboard para manejo de reservas | 8 | Técnica |
| Media     | HU12  | Admin   | Como administrador, quiero poner límites a las reservas diarias (máx. 10,000 flores/día) | 5 | Técnica |
| Media     | HU13  | Admin   | Como administrador, quiero imprimir etiquetas para entregas | 3 | Técnica |
| Media     | HU14  | Admin   | Como administrador, quiero gestionar devoluciones con trazabilidad | 5 | Técnica |
| Baja      | HU15  | Admin   | Como administrador, quiero categorizar productos por tipo de arreglo y motivo | 3 | Técnica |
| Baja      | HU16  | Admin   | Como administrador, quiero gestionar entregas tercerizadas dentro de la ciudad | 5 | Técnica |
| Baja      | HU17  | Admin   | Como administrador, quiero inventario de clientes para marketing | 3 | Técnica |
| Baja      | HU18  | Admin   | Como administrador, quiero reportes contables básicos | 5 | Técnica |
| Baja      | HU19  | Cliente | Como cliente, quiero una interfaz visualmente atractiva para ver arreglos | 5 | Funcional |
| Media     | HU20  | Repartidor | Como repartidor, quiero ver el listado de entregas del día | 5 | Funcional |
| Media     | HU21    | Admin   | Como administrador de inventario deseo registrar todos los ingresos de insumos para llevar control de la disponibilidad de insumos | 5 | Técnica |
| Media     | HU22    | Admin   | Como administrador de inventario deseo saber cuántas flores se han reservado en pedidos para evitar sobrevender flores | 5 | Técnica |
| Media     | HU23    | Admin   | Como administrador de inventario deseo poder generar un reporte de ingresos y egresos de materiales | 5 | Técnica |
| Alta      | HU24    | Cliente | Como cliente quiero un carrito de compras para agregar los ítems que quiero adquirir | 5 | Funcional |

---

## Definition of Done y Definition of Ready por Historia

| Código | Definition of Done (DoD) | Definition of Ready (DoR) |
|--------|--------------------------|---------------------------|
| HU1 | La funcionalidad permite seleccionar arreglos, programar fecha de entrega, y realizar la compra; pruebas unitarias y de integración aprobadas; validación en ambiente de pruebas; documentación actualizada. | Criterios de aceptación definidos; diseño de interfaz aprobado; datos de productos y fechas disponibles; dependencias identificadas. |
| HU2 | El sistema acepta múltiples métodos de pago, procesa transacciones correctamente, y muestra confirmación; pruebas de pago realizadas; integración con pasarela validada. | Métodos de pago definidos; integración con proveedor de pagos disponible; criterios de aceptación claros. |
| HU3 | El cliente puede crear, editar y eliminar su cuenta; validación de datos; pruebas de registro y login exitosas; documentación actualizada. | Campos requeridos definidos; flujo de registro diseñado; dependencias técnicas identificadas. |
| HU4 | El cliente recibe factura automática tras la compra; formato fiscal correcto; pruebas de generación y envío de factura; documentación actualizada. | Requisitos fiscales definidos; integración con sistema de facturación disponible; criterios de aceptación claros. |
| HU5 | El cliente puede calificar el producto tras la entrega; calificación visible en el sistema; pruebas de interfaz y almacenamiento; documentación actualizada. | Diseño de sistema de calificación aprobado; criterios de aceptación definidos; dependencias identificadas. |
| HU6 | El cliente puede solicitar reembolso; proceso automatizado y notificación enviada; pruebas de flujo de reembolso; documentación actualizada. | Políticas de reembolso definidas; integración con pagos disponible; criterios de aceptación claros. |
| HU7 | El cliente recibe notificaciones sobre el estado de su entrega; pruebas de envío y recepción de notificaciones; documentación actualizada. | Tipos de notificación definidos; integración con sistema de mensajería disponible; criterios de aceptación claros. |
| HU8 | El administrador puede gestionar inventario de flores y arreglos; operaciones CRUD funcionales; pruebas de inventario; documentación actualizada. | Estructura de inventario definida; dependencias técnicas identificadas; criterios de aceptación claros. |
| HU9 | El administrador puede generar reportes de inventario por rango de fechas; reportes exportables; pruebas de generación; documentación actualizada. | Requerimientos de reporte definidos; acceso a datos disponible; criterios de aceptación claros. |
| HU10 | El administrador puede actualizar precios; cambios reflejados en el sistema; pruebas de actualización; documentación actualizada. | Políticas de precios definidas; interfaz de actualización diseñada; criterios de aceptación claros. |
| HU11 | El dashboard muestra reservas actuales y futuras; visualización clara; pruebas de datos y gráficos; documentación actualizada. | Requerimientos de dashboard definidos; datos de reservas disponibles; criterios de aceptación claros. |
| HU12 | El sistema limita reservas a 10,000 flores/día; validación en frontend y backend; pruebas de límite; documentación actualizada. | Límite definido; dependencias técnicas identificadas; criterios de aceptación claros. |
| HU13 | El administrador puede imprimir etiquetas para entregas; formato correcto; pruebas de impresión; documentación actualizada. | Requerimientos de etiqueta definidos; integración con impresora disponible; criterios de aceptación claros. |
| HU14 | El administrador gestiona devoluciones con trazabilidad; historial completo disponible; pruebas de flujo; documentación actualizada. | Políticas de devolución definidas; sistema de trazabilidad diseñado; criterios de aceptación claros. |
| HU15 | El administrador categoriza productos por tipo y motivo; categorías visibles en el sistema; pruebas de clasificación; documentación actualizada. | Tipos y motivos definidos; interfaz de categorización diseñada; criterios de aceptación claros. |
| HU16 | El administrador gestiona entregas tercerizadas; integración con proveedores; pruebas de asignación; documentación actualizada. | Proveedores definidos; integración técnica disponible; criterios de aceptación claros. |
| HU17 | El administrador accede a inventario de clientes para marketing; datos exportables; pruebas de acceso; documentación actualizada. | Requerimientos de marketing definidos; acceso a datos disponible; criterios de aceptación claros. |
| HU18 | El administrador genera reportes contables básicos; reportes exportables; pruebas de generación; documentación actualizada. | Requerimientos contables definidos; acceso a datos disponible; criterios de aceptación claros. |
| HU19 | El cliente ve una interfaz atractiva para arreglos; diseño aprobado; pruebas de usabilidad; documentación actualizada. | Diseño de interfaz aprobado; criterios de aceptación definidos; dependencias identificadas. |
| HU20 | El repartidor ve el listado de entregas del día; listado actualizado y accesible; pruebas de visualización; documentación actualizada. | Requerimientos de entrega definidos; datos de entregas disponibles; criterios de aceptación claros. |
| HU21 | El administrador registra ingresos de insumos; registros visibles y editables; pruebas de ingreso; documentación actualizada. | Tipos de insumos definidos; interfaz de registro diseñada; criterios de aceptación claros. |
| HU22 | El administrador ve reservas de flores en pedidos; sistema evita sobrevender; pruebas de validación; documentación actualizada. | Lógica de reserva definida; acceso a datos de pedidos disponible; criterios de aceptación claros. |
| HU23 | El administrador genera reporte de ingresos y egresos de materiales; reportes exportables; pruebas de generación; documentación actualizada. | Requerimientos de reporte definidos; acceso a datos disponible; criterios de aceptación claros. |
| HU24 | El cliente tiene un carrito de compras funcional; puede agregar, editar y eliminar ítems; pruebas de flujo de compra; documentación actualizada. | Diseño de carrito aprobado; criterios de aceptación definidos; dependencias identificadas. |

---

## Notas
- La estimación de esfuerzo es orientativa y puede ajustarse en refinamiento.
- La prioridad puede cambiar según el valor de negocio y dependencias técnicas.
- Las historias técnicas son necesarias para el funcionamiento interno y la escalabilidad.
