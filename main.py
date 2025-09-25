from fastmcp import Client
from google import genai
from fastmcp import FastMCP

scraping_mcp_client = Client("scraping.py")
beer_mcp_client = Client("beer.py")
dice_mcp_client = Client("dice.py")
user_fetch_mcp_client = Client("user_fetch.py")
analyze_user_income_mcp_client = Client("analyze_user_income.py")
gemini_client = genai.Client()

mcp = FastMCP(name="main")


@mcp.tool
async def beer(contents: str):
    async with beer_mcp_client:
        response = await gemini_client.aio.models.generate_content(
            model="gemini-2.0-flash",
            contents=f"{contents}",
            config=genai.types.GenerateContentConfig(
                temperature=0,
                tools=[beer_mcp_client.session],
            ),
        )
        return response.text


@mcp.tool
async def dice(roll_num: str):
    print(f"startRoll {roll_num} dice!")
    async with dice_mcp_client:
        response = await gemini_client.aio.models.generate_content(
            model="gemini-2.0-flash",
            contents=f"Roll {roll_num} dice!",
            config=genai.types.GenerateContentConfig(
                temperature=0,
                tools=[dice_mcp_client.session],
            ),
        )
        return response.text


@mcp.tool
async def scraping(url: str):
    async with scraping_mcp_client:
        response = await gemini_client.aio.models.generate_content(
            model="gemini-2.0-flash",
            contents=f"{url}",
            config=genai.types.GenerateContentConfig(
                temperature=0,
                tools=[scraping_mcp_client.session],
            ),
        )
        return response.text


@mcp.tool
async def user_fetch(user_id: str):
    async with user_fetch_mcp_client:
        response = await gemini_client.aio.models.generate_content(
            model="gemini-2.0-flash",
            contents=f"fetch user to {user_id}",
            config=genai.types.GenerateContentConfig(
                temperature=0,
                tools=[user_fetch_mcp_client.session],
            ),
        )
    return response.text


@mcp.tool
async def analyze_user_income(context: str):
    async with analyze_user_income_mcp_client:
        response = await gemini_client.aio.models.generate_content(
            model="gemini-2.0-flash",
            contents=context,
            config=genai.types.GenerateContentConfig(
                temperature=0,
                tools=[analyze_user_income_mcp_client.session],
            ),
        )
    return response.text

if __name__ == "__main__":
    mcp.run(transport="sse")
