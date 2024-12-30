import asyncio
import aiohttp
import json

async def get_user_input(prompt: str) -> str:
    return input(prompt)

async def main():
    try:
        domain = await get_user_input("Enter domain: ")
        password = await get_user_input("Enter password: ")
        partner = await get_user_input("Enter partner: ")
        amount = int(await get_user_input("Enter amount: "))

        url = "https://api.viupremium.us.kg/create-account"

        payload = {
            "domain": domain,
            "password": password,
            "partner": partner,
            "amount": amount
        }

        headers = {
            "Content-Type": "application/json"
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload, headers=headers) as response:
                if response.status == 200:
                    result = await response.json()
                    if result.get('success'):
                        accounts = result.get('accounts', [])
                        print("Account created successfully. check result.txt")
                        
                        with open('result.txt', 'a') as f:
                            f.write('\n'.join(accounts) + '\n')
                    else:
                        print("Account creation failed. Response:")
                        print(result)
                else:
                    print(f"Failed to create account. HTTP Status Code: {response.status}")
                    print(await response.text())

    except Exception as error:
        print(f"An error occurred: {str(error)}")

if __name__ == "__main__":
    asyncio.run(main())
