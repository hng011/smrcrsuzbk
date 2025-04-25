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
                erres = response.json()["error"]["message"]
                logerr = f"LOG ERR OR: {model} | {erres}"                
                return ("res", "", logerr)
            
        except Exception as e:
            return (e, "", "")       