from .__init__ import *


def generate_text_from_transformer(model=""):
    ...

def generate_text(system_prompt, user_prompt, model="qwen/qwq-32b:free"):        
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
            
            erres = response.json()["error"]["message"]
            
            
            if not erres:
                return (str(response.json()["choices"][0]["message"]["content"]).strip(), model)
            else:
                print(f"LOG ERR OR: {erres}")
                res, status, model_name = call_g(system_prompt, user_prompt)
                if status == 200:
                    print(status)
                    return (res, model_name)
            
        except Exception as e:
            return e       
        
        
def call_g(system_prompt, user_prompt, model="gpt-4.1-nano"):        
        try:
            response = requests.post(
                url=G_API_ENDPOINT,
                headers={
                    "Authorization": f"Bearer {G_API_KEY}",
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
            
            return (
                str(response.json()["choices"][0]["message"]["content"]).strip(), 
                response.status_code,
                model
            )
        
        except Exception as e:
            return e