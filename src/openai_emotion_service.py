import json
from openai import OpenAI

from src.config import OPEN_API_KEY

client = OpenAI(api_key=OPEN_API_KEY) if OPEN_API_KEY else None

def analisar_emocoes(texto:str) -> dict:
    if client is None:
        return {"aspectos_detectados": []}

    prompt = f"""
        Analise o texto abaixo em português brasileiro.
        
        Retorne apenas um JSON válido com os valores inteiros de 0 a 100 para cada emoção/aspecto.
        Os valores não precisam somar 100, pois cada aspecto representa intensidade independente.
        
        Texto:
        \"\"\"{texto}\"\"\"
        
    retorne apenas um JSON válido nesse formato: 
    
    {{
        "aspectos_detectados": [{{
            "nome": "frustração",
            "intensidade": 85
        }}]
    }}
    
    Regras: 
    - Se nenhum aspecto emocional claro for detectado, retorne "aspectos_detectados":[].
    - Não use markdown.
    - Não explique fora do JSON.
    - Não inclua aspectos com intensidade 0.
    """
   
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt,
        temperature=0
    )
    
    conteudo = response.output_text
    
    return json.loads(conteudo)
