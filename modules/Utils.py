from .__init__ import *
from streamlit.components.v1 import html

def generate_text_from_transformer(model=""):
    ...

def generate_text(system_prompt, user_prompt, model="meta-llama/llama-3.3-70b-instruct:free"):        
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
                logerr = f"LOG ERR OR: {model} | {erres}"
                html(f"<script>console.log(\"{logerr}\");</script>", height=0,)
                
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