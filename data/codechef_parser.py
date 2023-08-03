import os
import json

bad_cases = [".DS_Store"]

def read_file(file_path):
    with open(file_path, "r") as file:
        content = file.read()
    return content

def process_directory(root_path):
    jsonl_data = []
    
    for root, dirs, files in os.walk(root_path):
        if "description" in dirs and "solutions_python" in dirs and "solutions_c++" in dirs:
            # print(root)
            description_path = os.path.join(root, "description", "description.txt")
            question = read_file(description_path)
            # question += " Solve it with Python."

            json_record = {"question": question}

            # print(question)

            answers = []

            # Add Python Solutions
            solutions_path = os.path.join(root, "solutions_python")
            solutions_files = [f for f in os.listdir(solutions_path) if os.path.isfile(os.path.join(solutions_path, f))]
            
            for solution_file in solutions_files:
                if solution_file in bad_cases: continue
                solution_path = os.path.join(solutions_path, solution_file)
                answer = read_file(solution_path)
                answers.append({"answer": answer, "lang": "python"})            

            # Add CPP Solutions
            solutions_path = os.path.join(root, "solutions_c++")
            solutions_files = [f for f in os.listdir(solutions_path) if os.path.isfile(os.path.join(solutions_path, f))]

            for solution_file in solutions_files:
                if solution_file in bad_cases: continue
                solution_path = os.path.join(solutions_path, solution_file)
                answer = read_file(solution_path)
                answers.append({"answer": answer, "lang": "c++"})            

            json_record["answers"] = answers
            jsonl_data.append(json_record)
    
    return json.dumps(jsonl_data, indent=2)

def write_to_file(jsonl_data, file_path):
    with open(file_path, "w") as file:
        file.write(jsonl_data)

def gen(d):
    root_path = "codechef/" + d
    jsonl_data = process_directory(root_path)
    write_to_file(jsonl_data, "description2code_codechef_problems_" + d + "_train.jsonl")    

def main():
    gen('easy')
    gen('medium')
    gen('hard')
    gen('harder')
    gen('hardest')
    gen('external')

if __name__ == "__main__":
    main()
    