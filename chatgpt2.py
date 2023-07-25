# import sys
import os
# import langchain

# from langchain.document_loaders import TextLoader
from langchain.document_loaders import DirectoryLoader
# from langchain.indexes import VectorstoreIndexCreator
# from langchain.prompts import PromptTemplate

from langchain.chat_models import ChatOpenAI
from langchain.text_splitter import CharacterTextSplitter
# from langchain.chains import ConversationChain
# from langchain.chains.conversation.memory import ConversationSummaryMemory
from langchain.vectorstores import FAISS
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
import json
# from langchain.document_transformers import Document
# from langchain import DirectoryLoader, VectorstoreIndexCreator, ConversationChain, ConversationSummaryMemory
# from langchain.schema import AIMessage , HumanMessage , SystemMessage
# from langchain.chains import LLMChain
# from langchain.prompts import ChatPromptTemplate
from langchain.embeddings import HuggingFaceInstructEmbeddings
# from InstructorEmbedding import INSTRUCTOR
# from langchain.agents import Agent, AgentType, initialize_agent


fileopen=open("api.txt","r")
APIKEY = fileopen.read()
fileopen.close()

os.environ["OPENAI_API_KEY"]=APIKEY


#loader = TextLoader("data.txt")
# loader = DirectoryLoader(".\\Database", glob= "*.txt")
# #docs = loader.load()
# index = VectorstoreIndexCreator().from_loaders([loader])

def faissbot2(input="", query_instruction="Represent the query for retrieval: ",llm=None, text_splitter=None, embeddings=None, vector_stores=None):
    loader = DirectoryLoader(".\\Database", glob="*.txt")
    docs = loader.load()
    document_string = str(docs[0])
    if len(document_string) > 500:
        document_string = document_string[250:-200]

    text_splitter = CharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
        length_function=len
    )

    llm = ChatOpenAI()
    chunks = text_splitter.split_text(text=document_string)
    # prompt = PromptTemplate.from_template(query_instruction)
    # chain = LLMChain(llm=llm, prompt=prompt)
    # embeddings = chain._call(input)

    embeddings = HuggingFaceInstructEmbeddings(
        query_instruction=query_instruction
    )
    vector_stores = FAISS.from_texts(chunks, embedding=embeddings)
    docs1 = vector_stores.similarity_search(query=input, k=1)
    chain = load_qa_chain(llm=llm, chain_type="stuff")
    response = chain.run(input_documents=docs1, question=input)

    return response

print(faissbot2("Who is Shaun?"))