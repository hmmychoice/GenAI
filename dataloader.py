from langchain_community.document_loaders import CSVLoader

file_path = r"C:\Users\mehta_co68f1g\Desktop\Employees_Q_A\EmployeesData.csv"

loader = CSVLoader(file_path=file_path)

data = loader.load()
