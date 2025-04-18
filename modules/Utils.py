from .__init__ import *

def call_openrouter(system_prompt, user_prompt, model="qwen/qwq-32b:free"):        
        try:
            response = requests.post(
                url=OPENROUTER_ENDPOINT,
                headers={
                    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                    "Content-Type": "application/json",
                },
                data=json.dumps({
                    "model": model,
                    "messages": [
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt},
                    ],
                })
            )
            
            return str(response.json()["choices"][0]["message"]["content"]).strip()
        
        except Exception as e:
            return e       