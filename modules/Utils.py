from .__init__ import *

def generate_story_from_transformer(model=""):
    ...

def generate_story(system_prompt, user_prompt, model="qwen/qwq-32b:free"):        
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
            
            if "error" not in response.json().keys():
                return (str(response.json()["choices"][0]["message"]["content"]).strip(), 
                        model.split(":")[0], 
                        "Using OpenRouter")                
            else:               
                res, model_name = call_g(system_prompt, user_prompt)
                erres = response.json()["error"]["message"]
                logerr = f"LOG ERR OR: {model} | {erres}"                
                return (res, model_name, logerr)
            
        except Exception as e:
            return (e, "", "")       
        
        
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
                model
            )
        
        except Exception as e:
            return (e, model)