from fastmcp import FastMCP

# Crear instancia del servidor MCP
mcp = FastMCP("MCP Tools")

# Definir un tool simple de prueba
@mcp.tool()
def add(a: int, b: int) -> int:
    """Suma dos números"""
    return a + b

if __name__ == "__main__":
    # Ejecutar en modo HTTP para Cloud Run
    mcp.run(transport="http", host="0.0.0.0", port=8080, path="/mcp")
