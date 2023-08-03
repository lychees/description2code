import autopep8
import os

def read_file(file_path):
    with open(file_path, "r", encoding='gbk') as file:
        content = file.read()
    return content

def gen(root_path):
    
    for root, dirs, files in os.walk(root_path):        
        if "description" in dirs and "solutions_python" in dirs and "solutions_c++" in dirs:
            print(root)
            # Add Python Solutions
            solutions_path = os.path.join(root, "solutions_python")
            reformatted_solutions_path = os.path.join(root, "reformatted_solutions_python")
            if not os.path.exists(reformatted_solutions_path):
                os.makedirs(reformatted_solutions_path)            
            
            solutions_files = [f for f in os.listdir(solutions_path) if os.path.isfile(os.path.join(solutions_path, f))]            
            for solution_file in solutions_files:
                solution_path = os.path.join(solutions_path, solution_file)   
                reformatted_solution_path = os.path.join(reformatted_solutions_path, solution_file)   
                try:
                    reformatted_code = autopep8.fix_code(read_file(solution_path), options={'aggressive': 3})
                    with open(reformatted_solution_path, "w", encoding="gbk") as file:
                        file.write(reformatted_code)
                except:
                    print(solution_file + " Error")
            
            # Add Cpp Solutions
            solutions_path = os.path.join(root, "solutions_c++")
            reformatted_solutions_path = os.path.join(root, "reformatted_solutions_c++")
            if not os.path.exists(reformatted_solutions_path):
                os.makedirs(reformatted_solutions_path)
            solutions_files = [f for f in os.listdir(solutions_path) if os.path.isfile(os.path.join(solutions_path, f))]            
            for solution_file in solutions_files:
                solution_path = os.path.join(solutions_path, solution_file)   
                reformatted_solution_path = os.path.join(reformatted_solutions_path, solution_file)
                os.system('clang-format ' + solution_path + " > " + reformatted_solution_path)
    return

def write_to_file(jsonl_data, file_path):
    with open(file_path, "w", encoding="gbk") as file:
        file.write(jsonl_data)

root_path = "..\\data\\codeforces\\"
gen(root_path)

