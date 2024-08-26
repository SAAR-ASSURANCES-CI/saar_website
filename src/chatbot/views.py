from django.shortcuts import render

# import os
# from flask import Flask, request, jsonify
# from pathlib import Path


from langchain_community.document_loaders.pdf import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain_community.vectorstores.chroma import Chroma

from transformers import pipeline

from langchain_chroma import Chroma
#from langchain_community.llms.ollama import Ollama
#from langchain_community.embeddings.ollama import OllamaEmbeddings

#from langchain.embeddings import HuggingFaceEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
#from langchain_community.embeddings import HuggingFaceEmbeddings


from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains.history_aware_retriever import create_history_aware_retriever
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain_core.messages import AIMessage, HumanMessage
from langchain.docstore.document import Document


# Create your views here.


