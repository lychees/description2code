from yapf.yapflib.yapf_api import FormatFile
import autopep8
import os
import json

id = 0

def read_file(file_path):
    with open(file_path, "r") as file:
        content = file.read()
    return content

def process_directory(root_path):
    global id
    jsonl_data = []
    
    for root, dirs, files in os.walk(root_path):
        if "description" in dirs and "solutions_python" in dirs and "solutions_c++" in dirs:
            description_path = os.path.join(root, "description", "description.txt")
            question = read_file(description_path)
            # question += " Solve it with Python."

            json_record = {
                "id": id,
                "question": question
            }
            id += 1
            if id >= 10:break

            answers = []

            # Add Python Solutions
            solutions_path = os.path.join(root, "solutions_python")
            solutions_files = [f for f in os.listdir(solutions_path) if os.path.isfile(os.path.join(solutions_path, f))]
            
            for solution_file in solutions_files:
                solution_path = os.path.join(solutions_path, solution_file)                
                answer = read_file(solution_path)
                print(answer)
                reformatted_code = autopep8.fix_code(answer, options={'aggressive': 3})
                print(reformatted_code)
                answers.append({"answer": reformatted_code, "lang": "python"})            
                # answer = read_file(solution_path)
                # answers.append({"answer": answer, "lang": "python"})
            # Add CPP Solutions
            solutions_path = os.path.join(root, "solutions_c++")
            solutions_files = [f for f in os.listdir(solutions_path) if os.path.isfile(os.path.join(solutions_path, f))]

            for solution_file in solutions_files:
                solution_path = os.path.join(solutions_path, solution_file)
                answer = read_file(solution_path)
                answers.append({"answer": answer, "lang": "c++"})            

            json_record["answers"] = answers
            json_record["source"] = "ethancaballero-description2code-codeforces.jsonl"
            jsonl_data.append(json_record)
    
    return json.dumps(jsonl_data, indent=2)

def write_to_file(jsonl_data, file_path):
    with open(file_path, "w") as file:
        file.write(jsonl_data)

def main():
    root_path = "codeforces/"
    jsonl_data = process_directory(root_path)
    write_to_file(jsonl_data, "ethancaballero-description2code-codeforces3.jsonl")

if __name__ == "__main__":
    main()
    