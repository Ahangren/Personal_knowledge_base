import os
from openai import OpenAI
from dotenv import load_dotenv,find_dotenv

# 加载环境变量，如果你电脑中以及配置了对应的变量这个则没有用
_=load_dotenv(find_dotenv())

def openai_embedding(text,model):
    # 加载环境变量
    API_KEY=os.environ['OPENAI_API_KEY']
    client=OpenAI(api_key=API_KEY)

    # 选用openai中的模型
    if not model:
        model='text-embedding-3-small'

    response=client.embeddings.create(
        model=model,
        input=text
    )
    return response

if __name__ == '__main__':
    response=openai_embedding("这里是openai中的embedding模块")


