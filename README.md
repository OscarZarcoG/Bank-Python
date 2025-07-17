# 🏦 Banco Zarco - Sistema Bancario

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)]()
[![GitHub](https://img.shields.io/badge/GitHub-Repository-black.svg)](https://github.com/OscarZarcoG/Bank-Python)

## 📋 Descripción

Sistema bancario simulado desarrollado en Python que permite gestionar operaciones bancarias básicas con una interfaz de línea de comandos moderna y profesional. El sistema incluye validaciones robustas, historial de transacciones persistente y una experiencia de usuario optimizada.

## ✨ Características

### 🔐 Gestión de Cuentas
- Creación de cuentas con validación de datos
- Validación de nombres (solo letras y espacios, mínimo 2 caracteres)
- Validación de números de cuenta (6-12 dígitos)
- Manejo preciso de decimales para operaciones monetarias

### 💰 Operaciones Bancarias
- **Depósitos**: Agregar fondos a la cuenta
- **Retiros**: Retirar fondos con validación de saldo suficiente
- **Consulta de saldo**: Visualización en tiempo real
- **Historial de transacciones**: Registro completo y persistente

### 🎨 Interfaz de Usuario
- Diseño inspirado en iOS con colores y bordes elegantes
- Limpieza automática de pantalla para mejor experiencia
- Mensajes de confirmación con pausas suaves
- Separadores visuales y headers profesionales

### 📊 Sistema de Historial
- Registro automático de todas las transacciones
- Timestamps precisos para cada operación
- Persistencia en archivo de texto
- Consulta de historial desde el menú principal

## 🛠️ Instalación

### Prerrequisitos

- Python 3.7 o superior
- Sistema operativo: Windows, macOS, o Linux

### Verificar instalación de Python

```bash
python --version
```

### Clonar o descargar el proyecto

```bash
# Opción 1: Clonar repositorio desde GitHub
git clone https://github.com/OscarZarcoG/Bank-Python.git
cd Bank-Python

# Opción 2: Descargar archivos directamente
# Descargar desde: https://github.com/OscarZarcoG/Bank-Python
```

### Dependencias

El proyecto utiliza únicamente librerías estándar de Python:
- `os` - Operaciones del sistema
- `re` - Expresiones regulares
- `time` - Manejo de tiempo
- `decimal` - Aritmética decimal precisa
- `datetime` - Manejo de fechas y horas

**No se requieren instalaciones adicionales.**

## 🚀 Ejecución

### Ejecutar el programa

```bash
# Navegar al directorio del proyecto
cd ruta/al/proyecto

# Ejecutar el simulador bancario
python banco_simulador.py
```

### Flujo de uso

1. **Inicio**: El programa solicita datos del cliente
2. **Menú principal**: Seleccionar operación deseada
3. **Operaciones**: Realizar depósitos, retiros o consultar historial
4. **Salida**: Finalizar sesión con resumen

## 📁 Estructura del Proyecto

```
Bank-Python/
│
├── banco_simulador.py      # Archivo principal del programa
├── historial_bancario.txt  # Archivo de historial (generado automáticamente)
└── README.md              # Documentación del proyecto
```

### Descripción de archivos

| Archivo | Descripción |
|---------|-------------|
| `banco_simulador.py` | Código fuente principal con toda la lógica del sistema |
| `historial_bancario.txt` | Archivo de texto que almacena el historial de transacciones |
| `README.md` | Documentación completa del proyecto |

## 🏗️ Arquitectura del Sistema

### Clase Principal: `BancoSimulador`

```python
class BancoSimulador:
    def __init__(self):
        self.apellido = ""
        self.numero_cuenta = ""
        self.nombre_cliente = ""
        self.balance = Decimal('0')
        self.historial_archivo = "historial_bancario.txt"
```

### Métodos Principales

| Método | Funcionalidad |
|--------|---------------|
| `solicitar_datos_iniciales()` | Recopila y valida información del cliente |
| `mostrar_menu()` | Presenta opciones disponibles |
| `procesar_deposito()` | Maneja operaciones de depósito |
| `procesar_retiro()` | Maneja operaciones de retiro |
| `mostrar_historial()` | Muestra historial de transacciones |
| `escribir_historial()` | Registra transacciones en archivo |

### Sistema de Validaciones

- **Apellido**: Solo letras y espacios, mínimo 2 caracteres
- **Número de cuenta**: Solo dígitos, entre 6 y 12 caracteres
- **Nombre**: Solo letras y espacios, mínimo 2 caracteres
- **Montos**: Números decimales válidos, mayor a cero, máximo $1,000,000

## 🎯 Funcionalidades Detalladas

### 💳 Gestión de Depósitos
- Validación de montos positivos
- Actualización automática del balance
- Registro en historial con timestamp
- Confirmación visual con pausa suave

### 💸 Gestión de Retiros
- Verificación de fondos suficientes
- Validación de montos
- Manejo de errores por fondos insuficientes
- Registro de intentos fallidos

### 📈 Sistema de Historial
- Formato: `[YYYY-MM-DD HH:MM:SS] OPERACION - Detalles`
- Tipos de registro:
  - Creación de cuenta
  - Depósitos exitosos
  - Retiros exitosos
  - Retiros fallidos
  - Cierre de sesión

## 🎨 Interfaz de Usuario

### Esquema de Colores
- **Azul**: Headers y títulos principales
- **Verde**: Operaciones exitosas
- **Rojo**: Errores y advertencias
- **Amarillo**: Información destacada
- **Cian**: Mensajes informativos

### Elementos Visuales
- Bordes con caracteres `=` para headers
- Separadores con caracteres `-`
- Centrado de títulos
- Limpieza automática de pantalla

## 🔧 Configuración

### Personalización

Puedes modificar los siguientes aspectos en el código:

```python
# Límites de validación
MAX_AMOUNT = 1000000  # Monto máximo por transacción
MIN_NAME_LENGTH = 2   # Longitud mínima de nombres
ACCOUNT_MIN_DIGITS = 6  # Mínimo dígitos en número de cuenta
ACCOUNT_MAX_DIGITS = 12 # Máximo dígitos en número de cuenta

# Archivo de historial
HISTORIAL_FILE = "historial_bancario.txt"
```

## 🐛 Solución de Problemas

### Errores Comunes

| Error | Causa | Solución |
|-------|-------|----------|
| `ModuleNotFoundError` | Python no instalado correctamente | Reinstalar Python 3.7+ |
| `PermissionError` | Sin permisos de escritura | Ejecutar desde directorio con permisos |
| `FileNotFoundError` | Archivo movido o eliminado | Verificar ubicación del archivo |

### Validaciones Fallidas

- **Nombre inválido**: Usar solo letras y espacios
- **Cuenta inválida**: Usar solo números (6-12 dígitos)
- **Monto inválido**: Usar números positivos menores a $1,000,000

## 📝 Registro de Cambios

### Versión Actual
- ✅ Sistema de historial persistente
- ✅ Validaciones robustas
- ✅ Mensajes de confirmación
- ✅ Limpieza automática de pantalla
- ✅ Manejo preciso de decimales

## 🤝 Contribuciones

Este es un proyecto educativo. Para mejoras o sugerencias:

1. Fork el repositorio desde [GitHub](https://github.com/OscarZarcoG/Bank-Python)
2. Crear una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -am 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Crear un Pull Request

## 📄 Licencia

Este proyecto es de uso educativo y está disponible bajo la licencia MIT.

## 👨‍💻 Autor

**Oscar Daniel Zarco González**
- GitHub: [@OscarZarcoG](https://github.com/OscarZarcoG)
- Proyecto: Sistema Bancario Simulado
- Tecnología: Python 3.7+
- Enfoque: Programación orientada a objetos y validaciones robustas

## 🔗 Enlaces

- **Repositorio**: [https://github.com/OscarZarcoG/Bank-Python](https://github.com/OscarZarcoG/Bank-Python)
- **Releases**: [Descargar última versión](https://github.com/OscarZarcoG/Bank-Python/releases)
- **Issues**: [Reportar problemas](https://github.com/OscarZarcoG/Bank-Python/issues)

---

**Banco Zarco - Sistema Bancario** | Desarrollado con Python | 2025