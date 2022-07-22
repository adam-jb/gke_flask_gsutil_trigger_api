
import os
from flask import Flask

app = Flask(__name__)



@app.route('/<string:input_string>', methods=['GET'])
def main():
	
	# separate input file into two strings
	original_folder_path, new_folder_path = input_string.split('_')

	command_to_run = f'source edit_text_files_function.sh && edit_and_move_all_files_in_pathway "{original_folder_path}" "{new_folder_path}"'
	print(f'running command:\t{command_to_run}')
	os.system(command_to_run)
	return f'executed:\t{command_to_run}'


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))


