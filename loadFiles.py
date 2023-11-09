import os
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Pinecone
from langchain.document_loaders import TextLoader
import pinecone


def main():
    files = ["docus/economia.txt", "docus/ingenieria-civil.txt", "docus/ingenieria-electrica.txt",
             "docus/ingenieria-electronica.txt", "docus/ingenieria-industrial.txt", "docus/ingenieria-sistemas.txt"]
    embeddings = OpenAIEmbeddings()
    for f in files:
        print("Estoy trabajando en subir: ",f)
        loader = TextLoader(f, "utf8")
        documents = loader.load()
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        docs = text_splitter.split_documents(documents)

        # initialize pinecone
        pinecone.init(
            api_key=os.getenv("PINECONE_API_KEY"),  # find at app.pinecone.io
            environment=os.getenv("PINECONE_ENV"),  # next to api key in console
        )

        index_name = "sainapsis"

        # First, check if our index already exists. If it doesn't, we create it
        #if index_name not in pinecone.list_indexes():
            # we create a new index
            # pinecone.create_index(name=index_name, metric="cosine", dimension=1536)
        # The OpenAI embedding model `text-embedding-ada-002 uses 1536 dimensions`
        docsearch = Pinecone.from_documents(docs, embeddings, index_name=index_name)

        # if you already have an index, you can load it like this
        docsearch = Pinecone.from_existing_index(index_name, embeddings)

        #query = "What did the president say about Ketanji Brown Jackson"
        #docs = docsearch.similarity_search(query)

        #print(docs[0].page_content)


if __name__ == '__main__':
    main()
