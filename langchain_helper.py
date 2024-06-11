import dataloader
import embeddings
import llm
from langchain_community.vectorstores import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from langchain.chains import RetrievalQA
from langchain.chains.qa_with_sources.retrieval import RetrievalQAWithSourcesChain

def createdb():
    db = Chroma.from_documents(documents=dataloader.data, 
                            embedding=embeddings.huggingface_embeddings)

    retriever = db.as_retriever()
    return retriever

#print(retriever.invoke("Provide me the joining date for the employee with employee name William Wang?")[0])

def create_qachain():
    retriever = createdb()
    template = """Given the following context and a question, generate an answer based on this context only.
    In the answer try to provide as much text as possible from "response" section in the source document context without making much changes.:
    {context}
    Question: {question}
    """

    prompt = ChatPromptTemplate.from_template(template)

    chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm.llm
        | StrOutputParser()
    )
    return chain

#print(chain.invoke("Provide me all the details for the employee with employee name John Doe?"))