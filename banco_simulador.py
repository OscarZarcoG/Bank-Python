import os
import re
import time
from decimal import Decimal, InvalidOperation
from datetime import datetime

class Colors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    BG_BLUE = '\033[44m'
    BG_GREEN = '\033[42m'
    BG_RED = '\033[41m'

class BancoSimulador:
    def __init__(self):
        self.apellido = ""
        self.numero_cuenta = ""
        self.nombre_cliente = ""
        self.balance = Decimal('0')
        self.historial_archivo = "historial_bancario.txt"
        
    def limpiar_pantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def escribir_historial(self, mensaje):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.historial_archivo, "a", encoding="utf-8") as archivo:
            archivo.write(f"[{timestamp}] {mensaje}\n")
            
    def mostrar_historial(self):
        try:
            with open(self.historial_archivo, "r", encoding="utf-8") as archivo:
                contenido = archivo.read()
                if contenido:
                    print(f"{Colors.CYAN}HISTORIAL DE TRANSACCIONES:{Colors.END}")
                    print(contenido)
                else:
                    print(f"{Colors.YELLOW}No hay transacciones en el historial.{Colors.END}")
        except FileNotFoundError:
            print(f"{Colors.YELLOW}No hay historial disponible.{Colors.END}")
        
    def mostrar_header(self):
        print(f"{Colors.BG_BLUE}{Colors.WHITE}{Colors.BOLD}" + "=" * 60 + f"{Colors.END}")
        print(f"{Colors.BG_BLUE}{Colors.WHITE}{Colors.BOLD}{'BANCO ZARCO - SISTEMA BANCARIO':^60}{Colors.END}")
        print(f"{Colors.BG_BLUE}{Colors.WHITE}{Colors.BOLD}" + "=" * 60 + f"{Colors.END}")
        print()
        
    def mostrar_separador(self):
        print(f"{Colors.CYAN}" + "-" * 50 + f"{Colors.END}")
        
    def validar_apellido(self, apellido):
        if not apellido or not apellido.strip():
            return False, "El apellido no puede estar vacío"
        if not re.match(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$", apellido.strip()):
            return False, "El apellido solo puede contener letras y espacios"
        if len(apellido.strip()) < 2:
            return False, "El apellido debe tener al menos 2 caracteres"
        return True, ""
        
    def validar_numero_cuenta(self, numero):
        if not numero or not numero.strip():
            return False, "El número de cuenta no puede estar vacío"
        numero = numero.strip()
        if not numero.isdigit():
            return False, "El número de cuenta solo puede contener dígitos"
        if len(numero) < 6 or len(numero) > 12:
            return False, "El número de cuenta debe tener entre 6 y 12 dígitos"
        return True, ""
        
    def validar_nombre(self, nombre):
        if not nombre or not nombre.strip():
            return False, "El nombre no puede estar vacío"
        if not re.match(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$", nombre.strip()):
            return False, "El nombre solo puede contener letras y espacios"
        if len(nombre.strip()) < 2:
            return False, "El nombre debe tener al menos 2 caracteres"
        return True, ""
        
    def validar_monto(self, monto_str):
        if not monto_str or not monto_str.strip():
            return False, "El monto no puede estar vacío", Decimal('0')
        try:
            monto = Decimal(monto_str.strip())
            if monto <= 0:
                return False, "El monto debe ser mayor a cero", Decimal('0')
            if monto > Decimal('1000000'):
                return False, "El monto no puede exceder $1,000,000", Decimal('0')
            return True, "", monto
        except (InvalidOperation, ValueError):
            return False, "Formato de monto inválido. Use números con punto decimal", Decimal('0')
            
    def solicitar_datos_iniciales(self):
        self.limpiar_pantalla()
        self.mostrar_header()
        
        print(f"{Colors.YELLOW}{Colors.BOLD}REGISTRO DE CLIENTE{Colors.END}")
        self.mostrar_separador()
        
        while True:
            apellido = input(f"{Colors.CYAN}Ingrese su apellido: {Colors.WHITE}")
            valido, mensaje = self.validar_apellido(apellido)
            if valido:
                self.apellido = apellido.strip().upper()
                break
            else:
                print(f"{Colors.RED}Error: {mensaje}{Colors.END}")
                
        while True:
            numero = input(f"{Colors.CYAN}Ingrese su numero de cuenta: {Colors.WHITE}")
            valido, mensaje = self.validar_numero_cuenta(numero)
            if valido:
                self.numero_cuenta = numero.strip()
                break
            else:
                print(f"{Colors.RED}Error: {mensaje}{Colors.END}")
                
        while True:
            nombre = input(f"{Colors.CYAN}Ingrese su nombre completo: {Colors.WHITE}")
            valido, mensaje = self.validar_nombre(nombre)
            if valido:
                self.nombre_cliente = nombre.strip().upper()
                break
            else:
                print(f"{Colors.RED}Error: {mensaje}{Colors.END}")
                
        while True:
            balance_str = input(f"{Colors.CYAN}Balance inicial de cuenta {self.numero_cuenta}: ${Colors.WHITE}")
            valido, mensaje, balance = self.validar_monto(balance_str)
            if valido:
                self.balance = balance
                self.escribir_historial(f"CUENTA CREADA - Cliente: {self.nombre_cliente}, Cuenta: {self.numero_cuenta}, Balance inicial: ${self.balance:,.2f}")
                break
            else:
                print(f"{Colors.RED}Error: {mensaje}{Colors.END}")
                
    def mostrar_info_cliente(self):
        print(f"{Colors.GREEN}{Colors.BOLD}INFORMACION DEL CLIENTE{Colors.END}")
        print(f"{Colors.WHITE}Cliente: {Colors.YELLOW}{self.nombre_cliente}{Colors.END}")
        print(f"{Colors.WHITE}Cuenta: {Colors.YELLOW}{self.numero_cuenta}{Colors.END}")
        print(f"{Colors.WHITE}Balance: {Colors.GREEN}${self.balance:,.2f}{Colors.END}")
        
    def mostrar_menu(self):
        self.limpiar_pantalla()
        self.mostrar_header()
        self.mostrar_info_cliente()
        self.mostrar_separador()
        
        print(f"{Colors.PURPLE}{Colors.BOLD}OPCIONES DISPONIBLES{Colors.END}")
        print(f"{Colors.GREEN}[D] Depositar dinero{Colors.END}")
        print(f"{Colors.YELLOW}[R] Retirar dinero{Colors.END}")
        print(f"{Colors.CYAN}[H] Ver historial{Colors.END}")
        print(f"{Colors.RED}[S] Salir del sistema{Colors.END}")
        self.mostrar_separador()
        
    def procesar_deposito(self):
        print(f"{Colors.GREEN}{Colors.BOLD}DEPOSITO DE DINERO{Colors.END}")
        self.mostrar_separador()
        
        while True:
            monto_str = input(f"{Colors.CYAN}Monto a depositar: ${Colors.WHITE}")
            valido, mensaje, monto = self.validar_monto(monto_str)
            if valido:
                balance_anterior = self.balance
                self.balance += monto
                self.escribir_historial(f"DEPOSITO - Monto: ${monto:,.2f}, Balance anterior: ${balance_anterior:,.2f}, Nuevo balance: ${self.balance:,.2f}")
                print(f"\n{Colors.GREEN}{Colors.BOLD}DEPOSITO EXITOSO{Colors.END}")
                print(f"Cliente: {self.nombre_cliente} {self.apellido}")
                print(f"Monto depositado: ${monto:,.2f}")
                print(f"Nuevo balance: ${self.balance:,.2f}")
                print(f"{Colors.CYAN}\nRedirigiendo al menu principal...{Colors.END}")
                time.sleep(2)
                break
            else:
                print(f"{Colors.RED}Error: {mensaje}{Colors.END}")
                
    def procesar_retiro(self):
        print(f"{Colors.YELLOW}{Colors.BOLD}RETIRO DE DINERO{Colors.END}")
        self.mostrar_separador()
        
        while True:
            monto_str = input(f"{Colors.CYAN}Monto a retirar: ${Colors.WHITE}")
            valido, mensaje, monto = self.validar_monto(monto_str)
            if valido:
                if monto <= self.balance:
                    balance_anterior = self.balance
                    self.balance -= monto
                    self.escribir_historial(f"RETIRO - Monto: ${monto:,.2f}, Balance anterior: ${balance_anterior:,.2f}, Nuevo balance: ${self.balance:,.2f}")
                    print(f"\n{Colors.GREEN}{Colors.BOLD}RETIRO EXITOSO{Colors.END}")
                    print(f"Cliente: {self.nombre_cliente} {self.apellido}")
                    print(f"Monto retirado: ${monto:,.2f}")
                    print(f"Nuevo balance: ${self.balance:,.2f}")
                    print(f"{Colors.CYAN}\nRedirigiendo al menu principal...{Colors.END}")
                    time.sleep(2)
                    break
                else:
                    self.escribir_historial(f"RETIRO FALLIDO - Intento de retirar ${monto:,.2f}, Balance disponible: ${self.balance:,.2f}")
                    print(f"\n{Colors.RED}{Colors.BOLD}FONDOS INSUFICIENTES{Colors.END}")
                    print(f"Monto solicitado: ${monto:,.2f}")
                    print(f"Balance disponible: ${self.balance:,.2f}")
                    print(f"{Colors.CYAN}\nRedirigiendo al menu principal...{Colors.END}")
                    time.sleep(2)
            else:
                print(f"{Colors.RED}Error: {mensaje}{Colors.END}")
                
    def mostrar_despedida(self):
        self.limpiar_pantalla()
        self.mostrar_header()
        
        print(f"{Colors.GREEN}{Colors.BOLD}RESUMEN FINAL{Colors.END}")
        self.mostrar_separador()
        print(f"{Colors.WHITE}Cliente: {Colors.YELLOW}{self.nombre_cliente}{Colors.END}")
        print(f"{Colors.WHITE}Cuenta: {Colors.YELLOW}{self.numero_cuenta}{Colors.END}")
        print(f"{Colors.WHITE}Balance final: {Colors.GREEN}${self.balance:,.2f}{Colors.END}")
        self.mostrar_separador()
        print(f"{Colors.PURPLE}{Colors.BOLD}Gracias por operar en Banco Zarco{Colors.END}")
        print(f"{Colors.CYAN}Que tenga un excelente dia{Colors.END}")
        self.escribir_historial(f"SESION FINALIZADA - Balance final: ${self.balance:,.2f}")
        
    def ejecutar(self):
        try:
            self.solicitar_datos_iniciales()
            
            while True:
                self.mostrar_menu()
                opcion = input(f"{Colors.CYAN}Seleccione una opcion [D/R/H/S]: {Colors.WHITE}").upper().strip()
                
                if opcion == 'D':
                    self.procesar_deposito()
                elif opcion == 'R':
                    self.procesar_retiro()
                elif opcion == 'H':
                    self.limpiar_pantalla()
                    self.mostrar_header()
                    self.mostrar_historial()
                    input(f"{Colors.CYAN}\nPresione Enter para continuar...{Colors.END}")
                elif opcion == 'S':
                    self.mostrar_despedida()
                    break
                else:
                    print(f"{Colors.RED}Opcion invalida. Por favor seleccione D, R, H o S.{Colors.END}")
                    
        except KeyboardInterrupt:
            print(f"\n{Colors.RED}\nOperacion cancelada por el usuario{Colors.END}")
        except Exception as e:
            print(f"{Colors.RED}Error inesperado: {str(e)}{Colors.END}")
            
def main():
    banco = BancoSimulador()
    banco.ejecutar()

if __name__ == "__main__":
    main()