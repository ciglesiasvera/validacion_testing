def calcular_total_ventas(ventas):
    """
    Calcula total de ventas por producto.
    
    Args:
        ventas (list): Lista de diccionarios con claves 'producto', 'cantidad', 'precio'.
        
    Returns:
        dict: Diccionario con el total monetario acumulado por producto.
    """
    totales = {}
    for venta in ventas:
        # Validación defensiva básica (Best Practice)
        if 'producto' not in venta or 'cantidad' not in venta or 'precio' not in venta:
            continue # O podríamos levantar un error (raise ValueError)
            
        producto = venta['producto']
        cantidad = venta['cantidad']
        precio = venta['precio']
        
        # Lógica de acumulación
        totales[producto] = totales.get(producto, 0) + (cantidad * precio)
    return totales

# --- SUITE DE TESTS ---

def test_calculo_totales_basico():
    """Prueba el escenario estándar (Happy Path)"""
    print("Ejecutando: test_calculo_totales_basico...")
    
    # 1. Arrange (Preparar datos)
    ventas = [
        {'producto': 'A', 'cantidad': 2, 'precio': 10}, # Total A: 20
        {'producto': 'B', 'cantidad': 1, 'precio': 20}, # Total B: 20
        {'producto': 'A', 'cantidad': 3, 'precio': 10}  # Total A: 20 + 30 = 50
    ]
    
    # 2. Act (Ejecutar función)
    resultado = calcular_total_ventas(ventas)
    
    # 3. Assert (Verificar resultados)
    assert resultado['A'] == 50, f"Error en Producto A: Esperado 50, obtenido {resultado.get('A')}"
    assert resultado['B'] == 20, f"Error en Producto B: Esperado 20, obtenido {resultado.get('B')}"
    
    print("✅ Test Básico PASADO")

def test_calculo_totales_vacio():
    """Prueba con lista vacía (Edge Case)"""
    print("Ejecutando: test_calculo_totales_vacio...")
    
    ventas = []
    resultado = calcular_total_ventas(ventas)
    
    assert resultado == {}, f"Esperado diccionario vacío, obtenido {resultado}"
    print("✅ Test Vacío PASADO")

def test_calculo_totales_decimales():
    """Prueba manejo de flotantes (Data Consistency)"""
    print("Ejecutando: test_calculo_totales_decimales...")
    
    ventas = [{'producto': 'C', 'cantidad': 1.5, 'precio': 10.0}]
    resultado = calcular_total_ventas(ventas)
    
    assert resultado['C'] == 15.0, f"Esperado 15.0, obtenido {resultado['C']}"
    print("✅ Test Decimales PASADO")

# --- EJECUCIÓN ---
if __name__ == "__main__":
    try:
        test_calculo_totales_basico()
        test_calculo_totales_vacio()
        test_calculo_totales_decimales()
        print("\n🚀 EXCELENTE: Todos los tests de la suite han pasado correctamente.")
    except AssertionError as e:
        print(f"\n❌ FALLO EN EL TEST: {e}")
    except Exception as e:
        print(f"\n❌ ERROR INESPERADO: {e}")