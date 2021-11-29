## Installation Instructions  
1. Install Python3: https://www.python.org/downloads/
2. Clone this repository
3. You need the requests and dotenv libraries. 
   * Enter the following in your terminal: `pip install requests python-dotenv`
4. Create a .env file with three keys: `URL`, `API_EMAIL`, and `API_TOKEN`
   * Set `URL` to your custom Zendesk domain with the `/api/v2/tickets.json` endpoint
   * Set `API_EMAIL` to your Zendesk email with `/token` appended to it
   * Set `API_TOKEN` to a valid Zendesk API Token

## Usage Instructions
1. Run main.py by navigating to the repository in your directory and entering the following in your terminal: `python main.py`
   * This command may be `python3 main.py` for some users
2. Simply follow the prompts in the command line, entering one of the proposed numbers.

## Example outputs
![image](https://user-images.githubusercontent.com/70153620/143906420-56b0fbe6-2800-4202-a115-66b9cf767376.png)  
![image](https://user-images.githubusercontent.com/70153620/143906646-2bba6d26-f471-4533-9ca5-903f20d54662.png)