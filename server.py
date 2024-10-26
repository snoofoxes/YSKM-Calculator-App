from fastapi import FastAPI

app = FastAPI()

@app.get("/{num1}/{sign}/{num2}")
async def cal(num1: int,sign: str,num2: int):
    if sign == "plus":
        result = num1 + num2 
        return {"Result":result}
    elif sign == "minus":
        result = num1 - num2
        return {"Result":result}
    elif sign == "multiply":
        result = num1 * num2
        return {"Result":result}
    elif sign == "divide":
        result = num1 / num2
        return {"Result":result}
    else:
        result = "Invalid Input"