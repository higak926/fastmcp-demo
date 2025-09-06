from fastmcp import FastMCP

mcp = FastMCP(name="Beer")


@mcp.tool
def want_beer() -> list[int]:
    return "ビールが飲みたい"


if __name__ == "__main__":
    mcp.run()
