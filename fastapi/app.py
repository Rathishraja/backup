from fastapi import FastAPI

app = FastAPI()
list_names = []

@app.get('/')
def home():
    return {"hello" :"world"}


@app.post('/')
def add_item(name: str):
    list_names.append(name)
    return "success"

@app.get('/list')
def list_all_names():
    return list_names

@app.delete('/')
def delete_item():
    deleted_item = list_names.pop()
    return deleted_item

if(__name__ == "__main__"):
    import uvicorn
    uvicorn.run(app)